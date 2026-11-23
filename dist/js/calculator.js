/**
 * SpikeFit - 科学能量消耗与运动生理算法计算器
 * 涵盖：ACSM 爬坡机公式、排球不同强度对抗能耗、力量与弹跳总负荷计算
 */

const CalorieCalculator = {
  /**
   * ACSM 运动医学会标准爬坡跑步机能量消耗方程
   * @param {number} weight - 体重 (kg)
   * @param {number} speedKmh - 时速 (km/h)，例如 4.5
   * @param {number} inclinePercent - 坡度百分比 (%)，例如 12 代表 12%
   * @param {number} durationMinutes - 运动时长 (分钟)
   * @returns {object} { calories: number, met: number, vo2: number, kcalPerMin: number }
   */
  calculateInclineTreadmill(weight = 70, speedKmh = 4.5, inclinePercent = 12, durationMinutes = 30) {
    // 转换为米/分钟 (m/min)
    const speedMpm = speedKmh * (1000 / 60);
    const grade = Math.max(0, inclinePercent) / 100;

    // ACSM 坡度步行摄氧量方程 (ml/kg/min): VO2 = 0.1 * S + 1.8 * S * G + 3.5
    const vo2 = (0.1 * speedMpm) + (1.8 * speedMpm * grade) + 3.5;
    
    // 换算为 MET (1 MET = 3.5 ml/kg/min)
    const met = vo2 / 3.5;

    // 每分钟消耗卡路里: VO2 * 体重 / 1000 * 5.0 (每升氧气约产生 5 kcal)
    const kcalPerMin = (vo2 * weight / 1000) * 5.0;
    const totalCalories = Math.round(kcalPerMin * durationMinutes);

    return {
      calories: totalCalories,
      met: Number(met.toFixed(1)),
      vo2: Number(vo2.toFixed(1)),
      kcalPerMin: Number(kcalPerMin.toFixed(2))
    };
  },

  /**
   * 排球专项能量消耗计算
   * @param {number} weight - 体重 (kg)
   * @param {string} intensity - 'casual' (休闲传垫), 'spiking_drills' (扣球专项摸高), 'competitive' (激烈对抗赛)
   * @param {number} durationMinutes - 时长 (分钟)
   * @returns {object} { calories: number, met: number }
   */
  calculateVolleyball(weight = 70, intensity = 'competitive', durationMinutes = 60) {
    let met = 6.0;
    if (intensity === 'casual') met = 4.0;
    else if (intensity === 'spiking_drills') met = 6.5;
    else if (intensity === 'competitive') met = 8.0;

    // 卡路里 = MET * 体重 * (分钟 / 60)
    const calories = Math.round(met * weight * (durationMinutes / 60));
    return {
      calories,
      met
    };
  },

  /**
   * 力量/弹跳/核心动作单项能耗与负荷计算
   * @param {number} weight - 体重 (kg)
   * @param {object} exercise - 动作对象
   * @param {Array} setsData - 每组数据 [{ weight: 60, reps: 8, completed: true }]
   * @returns {object} { calories: number, totalVolume: number, completedSets: number }
   */
  calculateStrengthExercise(weight = 70, exercise, setsData = []) {
    const completedSets = setsData.filter(s => s.completed !== false);
    if (!completedSets.length) return { calories: 0, totalVolume: 0, completedSets: 0 };

    let totalVolume = 0;
    completedSets.forEach(s => {
      const setWeight = Number(s.weight) || 0;
      const setReps = Number(s.reps) || 0;
      totalVolume += setWeight * setReps;
    });

    const met = exercise.met || 5.0;
    // 每组平均耗时（动作40秒 + 组间间歇60-90秒）按约 2.0 分钟/组核算代谢窗口
    const estimatedMinutes = completedSets.length * 2.0;
    
    // 基础代谢能耗
    let baseCalories = met * weight * (estimatedMinutes / 60);

    // 考虑负荷容积的 EPOC (运动后过量耗氧) 能量追加 (每 1000kg 容量补充约 15 kcal)
    const volumeBonus = (totalVolume / 1000) * 15;
    const finalCalories = Math.round(baseCalories + volumeBonus);

    return {
      calories: Math.max(1, finalCalories),
      totalVolume: Math.round(totalVolume),
      completedSets: completedSets.length
    };
  },

  /**
   * 基础代谢率 (BMR) 计算 - Mifflin-St Jeor 运动生理黄金方程
   * 男：10 * 体重(kg) + 6.25 * 身高(cm) - 5 * 年龄 + 5
   * 女：10 * 体重(kg) + 6.25 * 身高(cm) - 5 * 年龄 - 161
   * @param {string} gender - 'male' | 'female'
   * @param {number} weight - 体重 (kg)，默认 76
   * @param {number} height - 身高 (cm)，默认 174
   * @param {number} age - 年龄 (岁)，默认 25
   * @returns {number} 基础代谢 (kcal)
   */
  calculateBMR(gender = 'male', weight = 76, height = 174, age = 25) {
    const w = Number(weight) || 76;
    const h = Number(height) || 174;
    const a = Number(age) || 25;
    let bmr = (10 * w) + (6.25 * h) - (5 * a);
    if (gender === 'female') {
      bmr -= 161;
    } else {
      bmr += 5;
    }
    return Math.round(bmr);
  },

  /**
   * 计算每日总能耗支出 (TDEE) 与热量缺口 / 盈余
   * 公式：热量缺口 = (基础代谢 BMR + 当日运动消耗) - 当日饮食摄入
   * @param {number} bmr - 基础代谢
   * @param {number} exerciseBurn - 当日运动消耗 (排球 + 爬坡机 + 力量)
   * @param {number} intakeCalories - 当日饮食总摄入
   * @returns {object}
   */
  calculateCalorieDeficit(bmr, exerciseBurn, intakeCalories) {
    const bmrVal = Math.round(Number(bmr) || 0);
    const burnVal = Math.round(Number(exerciseBurn) || 0);
    const intakeVal = Math.round(Number(intakeCalories) || 0);
    const tdee = bmrVal + burnVal; // 当日总消耗
    const deficit = tdee - intakeVal; // 热量缺口: 总支出减摄入

    let status = 'balanced';
    let statusText = '能量收支平衡';
    let summary = '今日摄入与总消耗完全平衡！';

    if (deficit > 0) {
      status = 'deficit';
      statusText = `热量缺口 +${deficit} kcal`;
      summary = `今日总消耗高于饮食摄入 ${deficit} kcal，正处于高效燃脂塑形与脂肪分解状态！`;
    } else if (deficit < 0) {
      status = 'surplus';
      statusText = `热量盈余 ${Math.abs(deficit)} kcal`;
      summary = `今日饮食摄入高于总消耗 ${Math.abs(deficit)} kcal，适合大负荷训练后超量恢复与肌纤维生长！`;
    }

    return {
      bmr: bmrVal,
      exerciseBurn: burnVal,
      tdee,
      intakeCalories: intakeVal,
      deficit,
      status,
      statusText,
      summary
    };
  },

  /**
   * 估算消耗卡路里对应的食物等价值（更直观的成就反馈）
   * @param {number} totalCalories
   * @returns {string}
   */
  getEquivalents(totalCalories) {
    if (totalCalories <= 0) return '尚未产生消耗';
    const bowlOfRice = (totalCalories / 230).toFixed(1); // 1 碗米饭约 230 kcal
    const electrolyteDrink = (totalCalories / 120).toFixed(1); // 1 瓶运动饮料约 120 kcal
    return `相当于消耗了 ≈ ${bowlOfRice} 碗白米饭，或 ${electrolyteDrink} 瓶运动电解质水`;
  }
};

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { CalorieCalculator };
}
