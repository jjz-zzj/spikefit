/**
 * SpikeFit - 多端同步与持久化引擎
 * 支持：LocalStorage 纯离线优先、6位口令跨网络免登录云同步、JSON 备份与导出
 */

const SyncEngine = {
  STORAGE_KEY: 'spikefit_data_v1',
  SYNC_CODE_KEY: 'spikefit_sync_code',
  REMOTE_OBJECT_ID_KEY: 'spikefit_remote_obj_id',
  API_BASE: 'https://api.restful-api.dev/objects',

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
   * 推送数据到免注册云端中继 (通过 6 位口令关联)
   */
  async pushToCloud(data, syncCode) {
    const code = (syncCode || this.getOrCreateSyncCode()).toUpperCase();
    const payload = {
      name: `spikefit_user_${code}`,
      data: {
        syncCode: code,
        clientTime: new Date().toISOString(),
        payloadJson: JSON.stringify(data)
      }
    };

    let remoteId = localStorage.getItem(this.REMOTE_OBJECT_ID_KEY + '_' + code);

    try {
      let resp;
      if (remoteId) {
        // 尝试覆盖更新现有远程对象
        resp = await fetch(`${this.API_BASE}/${remoteId}`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
      }

      // 若没有 remoteId 或更新失败（对象可能过期），则创建新对象
      if (!resp || !resp.ok) {
        resp = await fetch(this.API_BASE, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
        if (resp.ok) {
          const resData = await resp.json();
          if (resData && resData.id) {
            localStorage.setItem(this.REMOTE_OBJECT_ID_KEY + '_' + code, resData.id);
          }
        }
      }

      if (resp && resp.ok) {
        return { success: true, message: '已成功同步至云端！' };
      } else {
        throw new Error('云端服务响应异常: ' + (resp ? resp.status : '无响应'));
      }
    } catch (err) {
      console.warn('云端推送提示:', err);
      return { 
        success: false, 
        message: '云端同步暂不可用或网络受限，本地数据已安全保存在手机/电脑中。' 
      };
    }
  },

  /**
   * 从云端拉取匹配口令的数据
   */
  async pullFromCloud(syncCode) {
    const code = (syncCode || this.getOrCreateSyncCode()).toUpperCase();
    let remoteId = localStorage.getItem(this.REMOTE_OBJECT_ID_KEY + '_' + code);

    try {
      let targetObj = null;

      if (remoteId) {
        const resp = await fetch(`${this.API_BASE}/${remoteId}`);
        if (resp.ok) {
          const item = await resp.json();
          if (item && item.data && item.data.syncCode === code) {
            targetObj = item;
          }
        }
      }

      // 如果未找到，尝试查询最近对象
      if (!targetObj) {
        const resp = await fetch(this.API_BASE);
        if (resp.ok) {
          const list = await resp.json();
          if (Array.isArray(list)) {
            const matched = list.filter(item => item.name === `spikefit_user_${code}`);
            if (matched.length > 0) {
              targetObj = matched[matched.length - 1]; // 取最新的
              if (targetObj && targetObj.id) {
                localStorage.setItem(this.REMOTE_OBJECT_ID_KEY + '_' + code, targetObj.id);
              }
            }
          }
        }
      }

      if (targetObj && targetObj.data && targetObj.data.payloadJson) {
        const parsed = JSON.parse(targetObj.data.payloadJson);
        return { success: true, data: parsed, updatedAt: targetObj.data.clientTime };
      }

      return { success: false, message: `未在云端找到口令【${code}】的数据，请确认另一端是否已点击“上传同步”。` };
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
