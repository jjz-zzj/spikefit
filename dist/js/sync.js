/**
 * SpikeFit - 多端同步与持久化引擎 (v2.0 极简分片高可用版)
 * 支持：LocalStorage 纯离线优先、动态数据脱敏轻量化、450字节智能分片中继、全自动后台静默双向同步
 */

const SyncEngine = {
  STORAGE_KEY: 'spikefit_data_v1',
  SYNC_CODE_KEY: 'spikefit_sync_code',
  REMOTE_PARTS_KEY: 'spikefit_remote_parts',
  API_BASE: 'https://api.restful-api.dev/objects',
  CHUNK_SIZE: 450, // 严控单片在 450 字符以内，彻底规避免费数据库 900 字节物理上限

  /**
   * 生成随机 6 位同步口令 (数字与大写字母组合)
   */
  generateSyncCode() {
    const chars = '23456789ABCDEFGHJKLMNPQRSTUVWXYZ';
    let code = '';
    for (let i = 0; i < 6; i++) {
      code += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return code;
  },

  /**
   * 获取或初始化本机同步口令
   */
  getOrCreateSyncCode() {
    let code = localStorage.getItem(this.SYNC_CODE_KEY);
    if (!code) {
      code = this.generateSyncCode();
      localStorage.setItem(this.SYNC_CODE_KEY, code);
    }
    return code;
  },

  /**
   * 设置新的同步口令（用于另一台设备配对接入）
   */
  setSyncCode(newCode) {
    if (!newCode || newCode.trim().length < 4) return false;
    const cleanCode = newCode.trim().toUpperCase();
    localStorage.setItem(this.SYNC_CODE_KEY, cleanCode);
    return cleanCode;
  },

  /**
   * 从 LocalStorage 读取全部本地数据
   */
  loadLocalData() {
    try {
      const raw = localStorage.getItem(this.STORAGE_KEY);
      if (!raw) return null;
      return JSON.parse(raw);
    } catch (e) {
      console.error('读取本地数据失败:', e);
      return null;
    }
  },

  /**
   * 保存数据到 LocalStorage
   */
  saveLocalData(data) {
    try {
      data.updatedAt = new Date().toISOString();
      localStorage.setItem(this.STORAGE_KEY, JSON.stringify(data));
      return true;
    } catch (e) {
      console.error('保存本地数据失败:', e);
      return false;
    }
  },

  /**
   * 极简脱敏压缩：去除静态庞大图解与文本说明，仅保留动态核心数据
   * 数据体积从 10,000+ 字符暴降至 300~900 字符
   */
  compress(fullData) {
    if (!fullData) return {};
    return {
      v: 2,
      ts: Date.now(),
      clientTime: new Date().toISOString(),
      // 用户生理与营养目标参数
      u: {
        w: fullData.userProfile?.weight || 78,
        h: fullData.userProfile?.height || 174,
        g: fullData.userProfile?.gender || 'male',
        c: fullData.userProfile?.macroCarbsRatio || 3.0,
        p: fullData.userProfile?.macroProteinRatio || 1.7,
        f: fullData.userProfile?.macroFatRatio || 1.0,
        vt: fullData.userProfile?.weeklyVolleyballTarget || 5
      },
      // 疲劳状态
      ft: fullData.fatigue || { shoulder: 2, knee: 1 },
      // 今日日期与模式
      td: fullData.todayDate,
      pm: fullData.planDateMode || 'today',
      // 排球打卡
      vb: fullData.todayVolleyball ? {
        e: fullData.todayVolleyball.enabled ? 1 : 0,
        d: fullData.todayVolleyball.duration || 60,
        i: fullData.todayVolleyball.intensity || 'competitive'
      } : null,
      // 爬坡打卡
      tm: fullData.todayTreadmill ? {
        e: fullData.todayTreadmill.enabled ? 1 : 0,
        d: fullData.todayTreadmill.duration || 30,
        s: fullData.todayTreadmill.speed || 4.5,
        inc: fullData.todayTreadmill.incline || 12
      } : null,
      // 今日训练动作 (仅存动作id与每组数据，不存静态庞大描述)
      ex: (fullData.todayExercises || []).map(e => ({
        id: e.id,
        name: e.name,
        sets: (e.sets || []).map(s => ({
          sn: s.setNumber,
          w: s.weight,
          r: s.reps,
          c: s.completed ? 1 : 0
        }))
      })),
      // 今日餐食 (仅存数值与菜名)
      ml: (fullData.todayMeals || []).map(m => ({
        id: m.id,
        t: m.time,
        n: m.dishName,
        cal: m.calories,
        c: m.carbs,
        p: m.protein,
        f: m.fat,
        fib: m.fiber || 0
      })),
      // 历史记录精简 (最近 7 条)
      hl: (fullData.historyLogs || []).slice(0, 7).map(h => ({
        id: h.id,
        d: h.date,
        n: h.name,
        tc: h.totalCalories,
        exs: (h.exercises || []).map(e => ({ id: e.id, name: e.name, setsCount: e.sets?.length || 0 }))
      })),
      // 日历日常餐食汇总 (精简版)
      dm: fullData.dailyMeals ? Object.keys(fullData.dailyMeals).reduce((acc, k) => {
        acc[k] = (fullData.dailyMeals[k] || []).map(m => ({
          id: m.id,
          t: m.time,
          n: m.dishName,
          cal: m.calories,
          c: m.carbs,
          p: m.protein,
          f: m.fat
        }));
        return acc;
      }, {}) : {}
    };
  },

  /**
   * 解码并还原完整业务对象
   */
  decompress(compactData) {
    if (!compactData) return null;
    if (compactData.v !== 2) return compactData; // 兼容旧版

    const u = compactData.u || {};
    const vb = compactData.vb || {};
    const tm = compactData.tm || {};

    return {
      userProfile: {
        weight: u.w || 78,
        height: u.h || 174,
        gender: u.g || 'male',
        macroCarbsRatio: u.c || 3.0,
        macroProteinRatio: u.p || 1.7,
        macroFatRatio: u.f || 1.0,
        weeklyVolleyballTarget: u.vt || 5
      },
      fatigue: compactData.ft || { shoulder: 2, knee: 1 },
      todayDate: compactData.td,
      planDateMode: compactData.pm || 'today',
      todayVolleyball: {
        enabled: vb.e === 1,
        duration: vb.d || 60,
        intensity: vb.i || 'competitive'
      },
      todayTreadmill: {
        enabled: tm.e === 1,
        duration: tm.d || 30,
        speed: tm.s || 4.5,
        incline: tm.inc || 12
      },
      // 结合本地 EXERCISE_DATABASE 还原动作完整属性
      todayExercises: (compactData.ex || []).map(item => {
        const dbEx = (typeof EXERCISE_DATABASE !== 'undefined') ? EXERCISE_DATABASE.find(e => e.id === item.id) : null;
        return {
          ...(dbEx || {}),
          id: item.id,
          name: item.name || dbEx?.name || item.id,
          sets: (item.sets || []).map(s => ({
            setNumber: s.sn,
            weight: s.w,
            reps: s.r,
            completed: s.c === 1
          }))
        };
      }),
      todayMeals: (compactData.ml || []).map(m => ({
        id: m.id,
        time: m.t,
        dishName: m.n,
        calories: m.cal,
        carbs: m.c,
        protein: m.p,
        fat: m.f,
        fiber: m.fib || 0
      })),
      historyLogs: (compactData.hl || []).map(h => ({
        id: h.id,
        date: h.d,
        name: h.n,
        totalCalories: h.tc,
        exercises: (h.exs || []).map(e => ({ id: e.id, name: e.name, sets: new Array(e.setsCount || 0).fill({ completed: true }) }))
      })),
      dailyMeals: compactData.dm || {}
    };
  },

  /**
   * 推送数据到云端中继 (多片安全存储，彻底规避 900 字节上限)
   */
  async pushToCloud(data, syncCode) {
    const code = (syncCode || this.getOrCreateSyncCode()).toUpperCase();
    const compactObj = this.compress(data);
    const jsonStr = JSON.stringify(compactObj);

    // 切分为不超过 CHUNK_SIZE 的小分片
    const chunks = [];
    for (let i = 0; i < jsonStr.length; i += this.CHUNK_SIZE) {
      chunks.push(jsonStr.substring(i, i + this.CHUNK_SIZE));
    }

    const totalParts = chunks.length;
    let savedPartIds = [];
    try {
      const rawStoredIds = localStorage.getItem(this.REMOTE_PARTS_KEY + '_' + code);
      if (rawStoredIds) savedPartIds = JSON.parse(rawStoredIds);
    } catch (e) {}

    const newPartIds = [];

    try {
      // 逐片并发/顺序上传
      for (let i = 0; i < totalParts; i++) {
        const payload = {
          name: `spikefit_${code}_p${i}`,
          data: {
            syncCode: code,
            partIdx: i,
            totalParts: totalParts,
            clientTime: new Date().toISOString(),
            chunk: chunks[i]
          }
        };

        const existingId = savedPartIds[i];
        let resp = null;
        if (existingId) {
          try {
            resp = await fetch(`${this.API_BASE}/${existingId}`, {
              method: 'PUT',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(payload)
            });
          } catch (err) {}
        }

        if (!resp || !resp.ok) {
          resp = await fetch(this.API_BASE, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
          });
        }

        if (resp && resp.ok) {
          const resData = await resp.json();
          newPartIds.push(resData.id || existingId);
        } else {
          throw new Error(`分片 ${i} 上传失败 (HTTP ${resp ? resp.status : 'ERR'})`);
        }
      }

      localStorage.setItem(this.REMOTE_PARTS_KEY + '_' + code, JSON.stringify(newPartIds));
      return { success: true, message: `已成功同步至云端 (${totalParts} 分片极速中继)` };
    } catch (err) {
      console.warn('云端推送异常:', err);
      return { 
        success: false, 
        message: '云端同步暂不可用或网络超时，本地数据已安全保存在设备中。' 
      };
    }
  },

  /**
   * 从云端拉取并重装拼接
   */
  async pullFromCloud(syncCode) {
    const code = (syncCode || this.getOrCreateSyncCode()).toUpperCase();
    let savedPartIds = [];
    try {
      const raw = localStorage.getItem(this.REMOTE_PARTS_KEY + '_' + code);
      if (raw) savedPartIds = JSON.parse(raw);
    } catch (e) {}

    try {
      let chunks = [];
      let lastTime = '';

      // 方式 1：如果有已记录的 partIds，直接并发拉取
      if (savedPartIds && savedPartIds.length > 0) {
        const fetchPromises = savedPartIds.map(id => 
          fetch(`${this.API_BASE}/${id}`)
            .then(r => r.ok ? r.json() : null)
            .catch(() => null)
        );
        const results = await Promise.all(fetchPromises);
        const validResults = results.filter(r => r && r.data && r.data.syncCode === code);
        if (validResults.length === savedPartIds.length) {
          validResults.sort((a, b) => (a.data.partIdx || 0) - (b.data.partIdx || 0));
          chunks = validResults.map(r => r.data.chunk);
          lastTime = validResults[0].data.clientTime || '';
        }
      }

      // 方式 2：若方式 1 未能拼齐，从公共列表按名称前缀匹配
      if (chunks.length === 0) {
        const resp = await fetch(this.API_BASE);
        if (resp.ok) {
          const list = await resp.json();
          if (Array.isArray(list)) {
            const matched = list.filter(item => item.name && item.name.startsWith(`spikefit_${code}_p`));
            if (matched.length > 0) {
              matched.sort((a, b) => (a.data?.partIdx || 0) - (b.data?.partIdx || 0));
              chunks = matched.map(m => m.data?.chunk || '');
              lastTime = matched[0]?.data?.clientTime || '';
              // 缓存对应 part IDs
              localStorage.setItem(this.REMOTE_PARTS_KEY + '_' + code, JSON.stringify(matched.map(m => m.id)));
            }
          }
        }
      }

      if (chunks.length > 0) {
        const fullJsonStr = chunks.join('');
        const parsed = JSON.parse(fullJsonStr);
        const restored = this.decompress(parsed);
        return { success: true, data: restored, updatedAt: lastTime };
      }

      return { success: false, message: `未在云端找到口令【${code}】的数据，请确认另一端是否已同步。` };
    } catch (err) {
      console.warn('云端拉取提示:', err);
      return { success: false, message: '网络连接失败，请检查手机网络或稍后重试。' };
    }
  },

  /**
   * 一键导出为 JSON 备份文本
   */
  exportJson(data) {
    return JSON.stringify(data, null, 2);
  },

  /**
   * 从 JSON 文本恢复导入
   */
  importJson(jsonString) {
    try {
      const parsed = JSON.parse(jsonString);
      if (parsed && typeof parsed === 'object') {
        this.saveLocalData(parsed);
        return { success: true, data: parsed };
      }
      return { success: false, message: 'JSON 格式不合法' };
    } catch (e) {
      return { success: false, message: '解析错误: ' + e.message };
    }
  }
};

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { SyncEngine };
}