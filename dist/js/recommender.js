/**
 * SpikeFit - 排球运动员智能动态推荐引擎
 * 针对：每周打球 5-7 天、肩膝负荷监控、关节保护与弹跳力量互补
 */

const WorkoutRecommender = {
  /**
   * 根据历史训练记录与疲劳状态，智能推荐今日最优训练方案
   * @param {Array} historyLogs - 最近的训练日志（按日期倒序）
   * @param {object} currentFatigue - { shoulder: 1~5, knee: 1~5 }
   * @returns {object} { title, type, reason, targetFocus, exercises: [] }
   */
  generateDailyRecommendation(historyLogs = [], currentFatigue = { shoulder: 1, knee: 1 }) {
    // 提取过去 3 天的排球与力量记录
    const recentLogs = historyLogs.slice(0, 3);
    
    let recentVolleyballCount = 0;
    let recentHighIntensityVolleyball = false;
    let trainedLegsRecently = false;
    let trainedUpperRecently = false;

    recentLogs.forEach(log => {
      if (log.volleyball && log.volleyball.duration > 0) {
        recentVolleyballCount++;
        if (log.volleyball.intensity === 'competitive') {
          recentHighIntensityVolleyball = true;
        }
      }
      if (log.exercises && log.exercises.length) {
        log.exercises.forEach(ex => {
          if (ex.category === 'legs' || ex.category === 'vertical_jump') trainedLegsRecently = true;
          if (ex.category === 'chest' || ex.category === 'back' || ex.category === 'shoulder') trainedUpperRecently = true;
        });
      }
    });

    const shoulderFatigue = Number(currentFatigue.shoulder) || 1;
    const kneeFatigue = Number(currentFatigue.knee) || 1;

    // 决策逻辑分支 1：肩部或膝盖疲劳偏高 (>=3)，或过去3天打了2场以上高强度球
    if (shoulderFatigue >= 3 || kneeFatigue >= 3 || recentVolleyballCount >= 2) {
      return {
        id: 'protection_rehab',
        title: '🛡️ 保护性互补：肩袖离心刹车 + 跟腱维护 + 爬坡燃脂',
        badge: '高频排球保护模式',
        badgeColor: 'amber',
        reason: `检测到你近期排球频次较高或局部关节有疲劳感（肩部 ${shoulderFatigue} 星 / 膝盖 ${kneeFatigue} 星）。扣球与反复起跳对肩峰与髌腱压力大，今日避开大重量推举与高落差跳跃，专注加固“刹车系统”与核心抗扭转。`,
        targetFocus: '肩袖离心制动、跟腱刚度、空中抗旋转稳定、低冲击爬坡',
        exercises: [
          {
            exerciseId: 'cable_face_pull',
            name: '绳索面拉 (Face Pull)',
            sets: 4,
            reps: 15,
            weight: 15,
            note: '扣球防伤神技，终末端大臂外旋展开'
          },
          {
            exerciseId: 'cable_external_rotation',
            name: '绳索肩外旋 (肩袖专项)',
            sets: 3,
            reps: 15,
            weight: 5,
            note: '强化冈下肌/小圆肌，为扣球快速挥臂提供刹车制动'
          },
          {
            exerciseId: 'cable_woodchopper_high_low',
            name: '龙门架高位斜向伐木',
            sets: 4,
            reps: 12,
            weight: 15,
            note: '强化腹斜肌与转体鞭打发力'
          },
          {
            exerciseId: 'tibialis_raise',
            name: '胫骨前肌抬脚尖 (Tibialis Raise)',
            sets: 3,
            reps: 20,
            weight: 0,
            note: '排球落地第一吸震器，有效缓解与预防跳跃膝'
          },
          {
            exerciseId: 'pogo_hops',
            name: '踝关节弹性小跳 (Pogo Hops)',
            sets: 3,
            reps: 20,
            weight: 0,
            note: '仅靠脚踝小幅反弹，保持跟腱弹簧刚度'
          },
          {
            exerciseId: 'incline_treadmill',
            name: '健身房坡度爬坡 (12% 坡度 / 4.5km/h)',
            isCardio: true,
            duration: 25,
            incline: 12,
            speed: 4.5,
            note: '零膝盖冲击，强化臀大肌与心肺代谢'
          }
        ]
      };
    }

    // 决策逻辑分支 2：下肢关节状态良好，近期未进行大重量下肢轰击
    if (!trainedLegsRecently && kneeFatigue < 3) {
      return {
        id: 'legs_vertical_jump',
        title: '⚡ 下肢重炮：垂直弹跳爆发力与起跳三伸展',
        badge: '弹跳突破模式',
        badgeColor: 'emerald',
        reason: '关节状态优良且近期未进行下肢大强度训练，是冲击深蹲力量基石与垂直摸高爆发力的黄金窗口！深蹲打底、硬拉蓄能、爆发跳释能。',
        targetFocus: '深蹲最大力量、RDL 屈髋助跑蓄能、轻负重爆发跳跃、落地吸震缓冲',
        exercises: [
          {
            exerciseId: 'barbell_squat',
            name: '杠铃深蹲',
            sets: 4,
            reps: 6,
            weight: 70,
            note: '起跳力量天花板，下蹲至大腿与地面平行'
          },
          {
            exerciseId: 'romanian_deadlift',
            name: '罗马尼亚硬拉 (RDL)',
            sets: 4,
            reps: 8,
            weight: 60,
            note: '折叠屈髋，拉紧臀大肌与腘绳肌，扣球助跑蓄力发动机'
          },
          {
            exerciseId: 'db_jump_squat',
            name: '哑铃轻负重深蹲跳',
            sets: 4,
            reps: 5,
            weight: 5,
            note: '释放最大功率，落地轻柔屈膝缓冲'
          },
          {
            exerciseId: 'box_jump_soft_landing',
            name: '跳箱/踏板跳 + 柔和落地',
            sets: 3,
            reps: 6,
            weight: 0,
            note: '像猫一样轻柔跳上踏板，保护膝关节'
          },
          {
            exerciseId: 'barbell_rollout',
            name: '杠铃推腹抗伸展 (Barbell Rollout)',
            sets: 3,
            reps: 10,
            weight: 10,
            note: '扣球充分拉弓后的抗过伸保护，收紧核心拉回'
          },
          {
            exerciseId: 'incline_treadmill',
            name: '放松整理：高坡慢速爬坡',
            isCardio: true,
            duration: 15,
            incline: 10,
            speed: 4.0,
            note: '乳酸冲洗，平稳心率'
          }
        ]
      };
    }

    // 决策逻辑分支 3：上肢推拉平衡与扣球核心轰炸
    return {
      id: 'upper_core_power',
      title: '🔥 上肢核心：扣球挥臂力量 + 背阔下压 + 滞空收腹',
      badge: '扣球进攻强化',
      badgeColor: 'cyan',
      reason: '构建强大的上肢扣杀推拉复合系统。以引体向上提供扣球下压动力，卧推增强推力对抗，高位伐木强化转体鞭打。',
      targetFocus: '背阔肌下拉制动、上胸高点支撑、空中悬垂卷腹、肩关节稳定',
      exercises: [
        {
          exerciseId: 'pull_up',
          name: '正手引体向上',
          sets: 4,
          reps: 8,
          weight: 0,
          note: '扣球滞空与下压之王，挺胸将胸口迎向单杠'
        },
        {
          exerciseId: 'incline_db_press',
          name: '上斜哑铃卧推',
          sets: 4,
          reps: 10,
          weight: 20,
          note: '强化上胸，支撑高点触球'
        },
        {
          exerciseId: 'cable_woodchopper_high_low',
          name: '龙门架高位斜向伐木',
          sets: 4,
          reps: 12,
          weight: 15,
          note: '转体鞭打核心扣杀动作'
        },
        {
          exerciseId: 'hanging_knee_twist',
          name: '单杠悬垂收腹转体',
          sets: 3,
          reps: 12,
          weight: 0,
          note: '空中悬空状态下的腹斜肌收紧与转体控制'
        },
        {
          exerciseId: 'cable_face_pull',
          name: '绳索面拉 (Face Pull)',
          sets: 4,
          reps: 15,
          weight: 15,
          note: '平衡前侧推力，护肩防撞击'
        },
        {
          exerciseId: 'incline_treadmill',
          name: '健身房爬坡燃脂',
          isCardio: true,
          duration: 20,
          incline: 12,
          speed: 4.5,
          note: '强化体能储备与有氧心肺'
        }
      ]
    };
  }
};

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { WorkoutRecommender };
}
