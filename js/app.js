/**
 * SpikeFit - 前端交互逻辑与状态管理 (Vue 3)
 * 支持今日实时打卡、明日预排计划、多日期协同、AI饮食营养相机与能量天平
 */
const { createApp, ref, computed, onMounted, watch } = Vue;

// 预置：昨日练背归档记录（2026-11-23 已完成）
const YESTERDAY_BACK_LOG = {
  id: 'log_back_20261123',
  date: '2026-11-23',
  createdAt: '2026-11-23T20:30:00.000Z',
  totalCalories: 330,
  totalVolume: 3680,
  fatigue: { shoulder: 2, knee: 1 },
  volleyball: null,
  treadmill: { enabled: true, duration: 15, incline: 10, speed: 4.2 },
  exercises: [
    {
      id: 'pull_up',
      name: '正手引体向上',
      category: 'back',
      categoryName: '背部拉力',
      equipment: '龙门架单杠/引体架',
      whyForVolleyball: '【滞空与制动核心】背阔肌是扣球从高处引臂下拉的最强动力源与空中稳定器',
      sets: [
        { setNumber: 1, weight: 0, reps: 8, completed: true },
        { setNumber: 2, weight: 0, reps: 8, completed: true },
        { setNumber: 3, weight: 0, reps: 6, completed: true },
        { setNumber: 4, weight: 0, reps: 6, completed: true }
      ]
    },
    {
      id: 'lat_pulldown',
      name: '宽握高位下拉',
      category: 'back',
      categoryName: '背部拉力',
      equipment: '高位下拉机/龙门架',
      whyForVolleyball: '安全积累背阔肌容量，增强扣球挥臂终末段的减速制动肌力',
      sets: [
        { setNumber: 1, weight: 45, reps: 10, completed: true },
        { setNumber: 2, weight: 50, reps: 10, completed: true },
        { setNumber: 3, weight: 50, reps: 8, completed: true },
        { setNumber: 4, weight: 45, reps: 10, completed: true }
      ]
    },
    {
      id: 'cable_seated_row',
      name: '坐姿绳索划船',
      category: 'back',
      categoryName: '背部拉力',
      equipment: '龙门架/坐姿划船机',
      whyForVolleyball: '强化上背厚度与躯干直立耐力，扣球后落地维持躯干中立不弯腰',
      sets: [
        { setNumber: 1, weight: 40, reps: 10, completed: true },
        { setNumber: 2, weight: 40, reps: 10, completed: true },
        { setNumber: 3, weight: 45, reps: 8, completed: true },
        { setNumber: 4, weight: 40, reps: 10, completed: true }
      ]
    },
    {
      id: 'cable_face_pull',
      name: '绳索面拉 (Face Pull)',
      category: 'back',
      categoryName: '背部拉力',
      equipment: '龙门架绳索/三头肌绳',
      whyForVolleyball: '【排球防伤第一神技】对抗频繁扣球带来的圆肩与肩峰撞击，保护肩关节长久健康',
      sets: [
        { setNumber: 1, weight: 15, reps: 15, completed: true },
        { setNumber: 2, weight: 15, reps: 15, completed: true },
        { setNumber: 3, weight: 15, reps: 15, completed: true },
        { setNumber: 4, weight: 15, reps: 15, completed: true }
      ]
    }
  ]
};

// 预置：明日（排球实战前·胸部推力与扣球转体核心）专训方案
const TOMORROW_PRESET_PLAN = {
  volleyball: {
    enabled: true,
    duration: 90,
    intensity: 'competitive',
    shoulderFatigue: 2,
    kneeFatigue: 2,
    notes: '明日排球实战对抗赛'
  },
  treadmill: {
    enabled: true,
    duration: 15,
    incline: 8,
    speed: 4.0
  },
  exercises: [
    {
      id: 'pushup_plus',
      name: '前锯肌俯卧撑 (Push-up Plus)',
      category: 'chest',
      categoryName: '胸部推力',
      equipment: '自重',
      targetMuscle: '前锯肌 (Serratus)、胸肌',
      whyForVolleyball: '【排球黄金动作】强化肩胛骨前引能力，防止扣球肩胛翼状突起，护肩必练',
      met: 4.0,
      note: '推至顶点用力含胸前引肩胛骨，唤醒前锯肌，保护肩关节',
      sets: [
        { setNumber: 1, weight: 0, reps: 12, completed: false },
        { setNumber: 2, weight: 0, reps: 12, completed: false }
      ]
    },
    {
      id: 'cable_external_rotation',
      name: '绳索肩外旋 (肩袖专项)',
      category: 'shoulder',
      categoryName: '肩部立体推力',
      equipment: '龙门架绳索',
      targetMuscle: '冈下肌、小圆肌 (肩袖肌群)',
      whyForVolleyball: '【扣球刹车皮】频繁扣球内旋发力后，外旋肩袖必须提供足够的刹车力，否则撕裂',
      met: 3.5,
      note: '极轻重量 2.5-5kg，仅作关节润滑与神经激活，不可力竭',
      sets: [
        { setNumber: 1, weight: 5, reps: 15, completed: false },
        { setNumber: 2, weight: 5, reps: 15, completed: false }
      ]
    },
    {
      id: 'incline_db_press',
      name: '上斜哑铃卧推',
      category: 'chest',
      categoryName: '胸部推力',
      equipment: '哑铃/上斜凳',
      targetMuscle: '胸肌上束、前锯肌',
      whyForVolleyball: '强化上举推力，提升扣球高点触球时肩胸上部的支撑爆发力',
      met: 5.5,
      note: '斜凳 30°，上斜角度契合网前双手上举拦网与高点触球支撑',
      sets: [
        { setNumber: 1, weight: 20, reps: 10, completed: false },
        { setNumber: 2, weight: 20, reps: 10, completed: false },
        { setNumber: 3, weight: 20, reps: 8, completed: false },
        { setNumber: 4, weight: 20, reps: 8, completed: false }
      ]
    },
    {
      id: 'cable_fly',
      name: '龙门架绳索中位夹胸',
      category: 'chest',
      categoryName: '胸部推力',
      equipment: '龙门架绳索',
      targetMuscle: '胸大肌内侧与中缝',
      whyForVolleyball: '提供全程持续张力，模拟扣球挥臂向前内收时的肌肉控制感',
      met: 4.5,
      note: '持续恒定张力，强化扣球包球内收力量',
      sets: [
        { setNumber: 1, weight: 15, reps: 12, completed: false },
        { setNumber: 2, weight: 15, reps: 12, completed: false },
        { setNumber: 3, weight: 15, reps: 12, completed: false }
      ]
    },
    {
      id: 'cable_woodchopper_high_low',
      name: '龙门架高位斜向伐木 (Cable Woodchopper)',
      category: 'volleyball_core',
      categoryName: '扣球核心爆发力',
      equipment: '龙门架绳索/手柄',
      targetMuscle: '腹内外斜肌、前侧核心、髋转子',
      whyForVolleyball: '【扣球发力动作孪生版】高位起手往斜下方砍下，完美重现扣球空中转体收腹的动能爆发',
      met: 5.5,
      note: '后脚蹬地转髋带动核心，斜向挥击伐木，打磨扣球转体鞭打感',
      sets: [
        { setNumber: 1, weight: 15, reps: 12, completed: false },
        { setNumber: 2, weight: 15, reps: 12, completed: false },
        { setNumber: 3, weight: 15, reps: 12, completed: false }
      ]
    },
    {
      id: 'pallof_press',
      name: '帕洛夫抗旋转推举 (Pallof Press)',
      category: 'volleyball_core',
      categoryName: '扣球核心爆发力',
      equipment: '龙门架绳索/弹力带',
      targetMuscle: '深层横突肌、腹横肌、抗旋转肌群',
      whyForVolleyball: '扣球空中身体若发生不必要的晃动会直接丢失击球点，此动作打造绝对躯干刚度',
      met: 4.5,
      note: '双手推出停顿 2 秒，打造空中绝对躯干刚度，防止受力晃动变形',
      sets: [
        { setNumber: 1, weight: 12, reps: 10, completed: false },
        { setNumber: 2, weight: 12, reps: 10, completed: false },
        { setNumber: 3, weight: 12, reps: 10, completed: false }
      ]
    },
    {
      id: 'pogo_hops',
      name: '踝关节弹性小跳 (Pogo Hops)',
      category: 'vertical_jump',
      categoryName: '垂直弹跳与跟腱',
      equipment: '自重平地',
      targetMuscle: '跟腱刚度、腓肠肌、足弓',
      whyForVolleyball: '【跟腱弹簧化】缩短触地时间（GCT），将跟腱变成高弹性弹簧，强化排球二次起跳反应速度',
      met: 7.0,
      note: '低疲劳唤醒跟腱弹性，膝盖微屈锁角，前脚掌快速反弹',
      sets: [
        { setNumber: 1, weight: 0, reps: 20, completed: false },
        { setNumber: 2, weight: 0, reps: 20, completed: false }
      ]
    },
    {
      id: 'tibialis_raise',
      name: '胫骨前肌抬脚尖 (Tibialis Raise)',
      category: 'legs',
      categoryName: '下肢基石力量',
      equipment: '自重靠墙/杠铃片',
      targetMuscle: '胫骨前肌 (小腿前侧)',
      whyForVolleyball: '【防跳跃膝秘密武器】排球落地第一道刹车吸震器，强化它可有效缓解髌腱炎痛感',
      met: 3.5,
      note: '靠墙站立用力勾脚尖，起跳落地第一道吸震器，防伤护膝必练',
      sets: [
        { setNumber: 1, weight: 0, reps: 15, completed: false },
        { setNumber: 2, weight: 0, reps: 15, completed: false }
      ]
    }
  ]
};

const app = createApp({
  setup() {
    // 视图导航
    const activeTab = ref('today'); // 'today' | 'recommend' | 'nutrition' | 'library' | 'history' | 'sync'
    
    // 日期计算工具
    const formatDate = (d) => {
      const year = d.getFullYear();
      const month = String(d.getMonth() + 1).padStart(2, '0');
      const day = String(d.getDate()).padStart(2, '0');
      return `${year}-${month}-${day}`;
    };

    const now = new Date();
    const todayDate = ref(formatDate(now));
    
    const tomorrowObj = new Date(now);
    tomorrowObj.setDate(tomorrowObj.getDate() + 1);
    const tomorrowDate = ref(formatDate(tomorrowObj));

    // 计划日期模式：'today' (今日打卡，默认) | 'tomorrow' (明日预排)
    const planDateMode = ref('today');

    // 短格式日期展示
    const todayDateShort = computed(() => {
      const parts = todayDate.value.split('-');
      return `${Number(parts[1])}月${Number(parts[2])}日`;
    });

    const tomorrowDateShort = computed(() => {
      const parts = tomorrowDate.value.split('-');
      return `${Number(parts[1])}月${Number(parts[2])}日`;
    });

    // 当前活跃日期
    const activePlanDate = computed(() => {
      return planDateMode.value === 'today' ? todayDate.value : tomorrowDate.value;
    });

    // 用户基础资料与体能参数 (按用户实际设定：身高 174cm，体重 78kg，三大营养素：3倍碳水 / 1.7倍蛋白 / 1倍脂肪)
    const userProfile = ref({
      gender: 'male',
      age: 25,
      height: 174,
      weight: 78,
      weeklyVolleyballTarget: 5,
      macroCarbsRatio: 3.0,    // 碳水系数 (g/kg) - 3.0x
      macroProteinRatio: 1.7,  // 蛋白质系数 (g/kg) - 1.7x
      macroFatRatio: 1.0       // 脂肪系数 (g/kg) - 1.0x
    });

    // 基础代谢率 (BMR) - 运动生理学黄金 Mifflin-St Jeor 算法
    const bmrCalories = computed(() => {
      return CalorieCalculator.calculateBMR(
        userProfile.value.gender,
        userProfile.value.weight,
        userProfile.value.height,
        userProfile.value.age
      );
    });

    // 身体疲劳监控 (1-5 星)
    const fatigue = ref({
      shoulder: 2,
      knee: 1
    });

    // 跨日期多计划容器字典 { 'YYYY-MM-DD': { volleyball, treadmill, exercises } }
    const dailyPlans = ref({});

    // 跨日期多餐食容器字典 { 'YYYY-MM-DD': [ { id, time, dishName, calories, carbs, protein, fat, fiber, advice } ] }
    const dailyMeals = ref({
      '2026-11-23': [
        {
          id: 'meal_20261123_1',
          time: '12:30',
          dishName: '熟瘦牛肉配优质米饭与时蔬',
          calories: 650,
          carbs: 80,
          protein: 45,
          fat: 12,
          fiber: 4,
          advice: '练背日核心正餐：高蛋白与高复合碳水，迅速补充肌糖原，促进背阔肌超量恢复'
        },
        {
          id: 'meal_20261123_2',
          time: '21:00',
          dishName: '乳清蛋白粉冲水',
          calories: 140,
          carbs: 3,
          protein: 26,
          fat: 2,
          fiber: 0,
          advice: '力量训练后半小时内快速吸收，提升肌肉蛋白质合成效率'
        }
      ],
      '2026-11-24': [
        {
          id: 'meal_20261124_1',
          time: '08:00',
          dishName: '燕麦片水牛奶香蕉坚果力量能量碗',
          calories: 548,
          carbs: 72,
          protein: 18.5,
          fat: 22,
          fiber: 7.2,
          advice: '排球实战前最佳运动早餐：水牛奶优质慢消化酪蛋白，香蕉高钾防小腿抽筋，燕麦缓释充盈肌糖原，坚果提供持久稳定供能'
        }
      ]
    });

    // 当前视图绑定的活动计划表单数据
    const todayVolleyball = ref({
      enabled: true,
      duration: 90,
      intensity: 'competitive',
      shoulderFatigue: 2,
      kneeFatigue: 2,
      notes: ''
    });

    const todayTreadmill = ref({
      enabled: true,
      duration: 15,
      incline: 8,
      speed: 4.0
    });

    const todayExercises = ref([]);

    // 历史训练记录归档
    const historyLogs = ref([]);

    // AI 饮食与营养相机模块状态
    const geminiApiKey = ref(NutritionAI.DEFAULT_GEMINI_KEY);
    const mealImageBase64 = ref('');
    const mealTextDescription = ref('燕麦40g + 水牛奶200ml + 香蕉1根 + 坚果15g');
    const isAnalyzingMeal = ref(false);
    const mealAnalysisResult = ref(null);
    const pastedAiText = ref('');
    const showPasteAiModal = ref(false);
    const todayMeals = ref([]);

    // 同步口令与状态
    const syncCode = ref('');
    const inputSyncCode = ref('');
    const syncStatus = ref({ loading: false, message: '', type: '' });
    const showQrModal = ref(false);
    const mobileLanUrl = ref(window.location.href);

    // 动作库检索与过滤
    const librarySearch = ref('');
    const libraryCategory = ref('all');
    const libraryEquipment = ref('all');
    const selectedExerciseDetail = ref(null);

    // 动作教学示意图弹窗与状态
    const showExerciseIllustrationModal = ref(false);
    const currentIllustration = ref(null);
    const currentIllustrationExercise = ref(null);

    const openExerciseIllustration = (exerciseOrId) => {
      let exId = '';
      let exObj = null;
      if (typeof exerciseOrId === 'string') {
        exId = exerciseOrId;
        exObj = EXERCISE_DATABASE.find(e => e.id === exId) || null;
      } else if (exerciseOrId && typeof exerciseOrId === 'object') {
        exId = exerciseOrId.id || exerciseOrId.exerciseId || '';
        exObj = exerciseOrId;
      }
      if (!exId) return;

      const illus = (typeof getExerciseIllustration === 'function') ? getExerciseIllustration(exId) : (typeof EXERCISE_ILLUSTRATIONS !== 'undefined' ? EXERCISE_ILLUSTRATIONS[exId] : null);
      if (illus) {
        currentIllustration.value = illus;
        currentIllustrationExercise.value = exObj || { id: exId, name: illus.title };
        showExerciseIllustrationModal.value = true;
      } else {
        showToast('该动作教学图解正在生成中');
      }
    };

    const closeExerciseIllustration = () => {
      showExerciseIllustrationModal.value = false;
    };

    const getIllustrationSvg = (exId) => {
      if (typeof EXERCISE_ILLUSTRATIONS !== 'undefined' && EXERCISE_ILLUSTRATIONS[exId]) {
        return EXERCISE_ILLUSTRATIONS[exId].svg;
      }
      return '';
    };

    // Toast 提示
    const toast = ref({ show: false, message: '' });

    const showToast = (msg) => {
      toast.value.message = msg;
      toast.value.show = true;
      setTimeout(() => {
        toast.value.show = false;
      }, 2500);
    };

    // ================= 计算属性：实时能耗与训练量 =================
    // 爬坡机卡路里
    const treadmillCalories = computed(() => {
      if (!todayTreadmill.value.enabled) return 0;
      const res = CalorieCalculator.calculateInclineTreadmill(
        userProfile.value.weight,
        todayTreadmill.value.speed,
        todayTreadmill.value.incline,
        todayTreadmill.value.duration
      );
      return res.calories;
    });

    // 爬坡机 MET 与 Kcal/min 详情
    const treadmillDetails = computed(() => {
      return CalorieCalculator.calculateInclineTreadmill(
        userProfile.value.weight,
        todayTreadmill.value.speed,
        todayTreadmill.value.incline,
        todayTreadmill.value.duration
      );
    });

    // 排球实战卡路里
    const volleyballCalories = computed(() => {
      if (!todayVolleyball.value.enabled) return 0;
      const res = CalorieCalculator.calculateVolleyball(
        userProfile.value.weight,
        todayVolleyball.value.intensity,
        todayVolleyball.value.duration
      );
      return res.calories;
    });

    // 力量与弹跳动作卡路里与总搬运容积 (Volume)
    const strengthStats = computed(() => {
      let totalCals = 0;
      let totalVolume = 0;
      let totalSetsDone = 0;

      todayExercises.value.forEach(item => {
        const res = CalorieCalculator.calculateStrengthExercise(
          userProfile.value.weight,
          item,
          item.sets || []
        );
        totalCals += res.calories;
        totalVolume += res.totalVolume;
        totalSetsDone += res.completedSets;
      });

      return {
        calories: totalCals,
        volume: totalVolume,
        setsDone: totalSetsDone
      };
    });

    // 当前视图日期总能量消耗 (kcal)
    const todayTotalCalories = computed(() => {
      return treadmillCalories.value + volleyballCalories.value + strengthStats.value.calories;
    });

    // 等价食物/补给提示
    const calorieEquivalents = computed(() => {
      return CalorieCalculator.getEquivalents(todayTotalCalories.value);
    });

    // 今日饮食总摄入统计
    const todayNutritionTotal = computed(() => {
      let cals = 0;
      let carbs = 0;
      let protein = 0;
      let fat = 0;
      let fiber = 0;
      todayMeals.value.forEach(m => {
        cals += Number(m.calories) || 0;
        carbs += Number(m.carbs) || 0;
        protein += Number(m.protein) || 0;
        fat += Number(m.fat) || 0;
        fiber += Number(m.fiber) || 0;
      });
      return {
        calories: Math.round(cals),
        carbs: Math.round(carbs),
        protein: Math.round(protein),
        fat: Math.round(fat),
        fiber: Math.round(fiber)
      };
    });

    // 每日能量天平与热量缺口核心算法：
    // 用户指定公式：基础代谢 (BMR) + 当日运动消耗 - 饮食摄入 = 热量缺口
    const dailyEnergyDeficit = computed(() => {
      return CalorieCalculator.calculateCalorieDeficit(
        bmrCalories.value,
        todayTotalCalories.value,
        todayNutritionTotal.value.calories
      );
    });

    // 兼容原 netEnergyBalance 绑定
    const netEnergyBalance = computed(() => {
      const def = dailyEnergyDeficit.value;
      return {
        intake: def.intakeCalories,
        burn: def.exerciseBurn,
        bmr: def.bmr,
        tdee: def.tdee,
        balance: def.deficit,
        statusText: def.statusText,
        summary: def.summary
      };
    });

    // 三大营养素科学目标摄入量与达成对比 (用户设定：体重 78kg，3倍碳水，1.7倍蛋白质，1倍脂肪)
    const targetMacros = computed(() => {
      return CalorieCalculator.calculateTargetMacros(
        userProfile.value.weight,
        userProfile.value.macroCarbsRatio,
        userProfile.value.macroProteinRatio,
        userProfile.value.macroFatRatio
      );
    });

    const macrosComparison = computed(() => {
      return CalorieCalculator.compareMacros(
        todayNutritionTotal.value,
        targetMacros.value
      );
    });

    // 营养方案预设切换与参数抽屉控制
    const activeMacroPreset = ref('volleyball'); // 'volleyball' | 'lean' | 'carb_loading' | 'custom'
    const showMacroConfigDrawer = ref(false);

    const applyMacroPreset = (preset) => {
      activeMacroPreset.value = preset;
      if (preset === 'volleyball') {
        userProfile.value.macroCarbsRatio = 3.0;
        userProfile.value.macroProteinRatio = 1.7;
        userProfile.value.macroFatRatio = 1.0;
        showToast('已切换至【排球专项高能与恢复】配比 (3.0x 碳水 / 1.7x 蛋白 / 1.0x 脂肪)');
      } else if (preset === 'lean') {
        userProfile.value.macroCarbsRatio = 2.0;
        userProfile.value.macroProteinRatio = 2.0;
        userProfile.value.macroFatRatio = 0.8;
        showToast('已切换至【低脂紧致/减脂塑形】配比 (2.0x 碳水 / 2.0x 蛋白 / 0.8x 脂肪)');
      } else if (preset === 'carb_loading') {
        userProfile.value.macroCarbsRatio = 4.5;
        userProfile.value.macroProteinRatio = 1.5;
        userProfile.value.macroFatRatio = 0.8;
        showToast('已切换至【重大比赛/赛前爆发充碳】配比 (4.5x 碳水 / 1.5x 蛋白 / 0.8x 脂肪)');
      }
      saveState();
    };

    // 二维码图片链接
    const qrCodeImageUrl = computed(() => {
      const urlToEncode = mobileLanUrl.value || window.location.href;
      return `https://api.qrserver.com/v1/create-qr-code/?size=220x220&margin=10&color=000000&bgcolor=ffffff&data=${encodeURIComponent(urlToEncode)}`;
    });

    // 智能推荐方案 (基于历史记录与疲劳度)
    const recommendedWorkout = computed(() => {
      return WorkoutRecommender.generateDailyRecommendation(historyLogs.value, fatigue.value);
    });

    // 动作库列表筛选过滤
    const filteredExercises = computed(() => {
      return EXERCISE_DATABASE.filter(ex => {
        const matchesCategory = libraryCategory.value === 'all' || ex.category === libraryCategory.value;
        const matchesEquipment = libraryEquipment.value === 'all' || ex.equipment.includes(libraryEquipment.value);
        const matchesSearch = !librarySearch.value.trim() ||
          ex.name.toLowerCase().includes(librarySearch.value.toLowerCase()) ||
          ex.targetMuscle.toLowerCase().includes(librarySearch.value.toLowerCase()) ||
          ex.whyForVolleyball.toLowerCase().includes(librarySearch.value.toLowerCase());
        return matchesCategory && matchesEquipment && matchesSearch;
      });
    });

    // ================= 多日期切换与同步 =================
    const syncCurrentFormToDict = () => {
      dailyPlans.value[activePlanDate.value] = {
        volleyball: JSON.parse(JSON.stringify(todayVolleyball.value)),
        treadmill: JSON.parse(JSON.stringify(todayTreadmill.value)),
        exercises: JSON.parse(JSON.stringify(todayExercises.value))
      };
    };

    const loadPlanFromDict = (dateStr) => {
      let targetPlan = dailyPlans.value[dateStr];
      // 关键修复：若当前日期没有记录或为空，且是今日(2026-11-24)或预排日，自动载入量身定制的排球实战前胸部推力与核心方案
      if (!targetPlan || (!targetPlan.exercises?.length && !targetPlan.volleyball?.enabled)) {
        if (dateStr === todayDate.value || dateStr === '2026-11-24' || dateStr === tomorrowDate.value) {
          targetPlan = JSON.parse(JSON.stringify(TOMORROW_PRESET_PLAN));
          dailyPlans.value[dateStr] = targetPlan;
        } else {
          targetPlan = {
            volleyball: { enabled: false, duration: 90, intensity: 'competitive', shoulderFatigue: 2, kneeFatigue: 2, notes: '' },
            treadmill: { enabled: false, duration: 20, incline: 10, speed: 4.5 },
            exercises: []
          };
        }
      }

      todayVolleyball.value = JSON.parse(JSON.stringify(targetPlan.volleyball || { enabled: false }));
      todayTreadmill.value = JSON.parse(JSON.stringify(targetPlan.treadmill || { enabled: false }));
      todayExercises.value = JSON.parse(JSON.stringify(targetPlan.exercises || []));
      loadMealsFromDict(dateStr);
    };

    const syncMealsToDict = () => {
      dailyMeals.value[activePlanDate.value] = JSON.parse(JSON.stringify(todayMeals.value));
    };

    const loadMealsFromDict = (dateStr) => {
      if (dailyMeals.value[dateStr]) {
        todayMeals.value = JSON.parse(JSON.stringify(dailyMeals.value[dateStr]));
      } else {
        todayMeals.value = [];
        dailyMeals.value[dateStr] = [];
      }
    };

    const switchPlanDate = (mode) => {
      syncCurrentFormToDict();
      syncMealsToDict();
      planDateMode.value = mode;
      loadPlanFromDict(activePlanDate.value);
      saveState();
      showToast(mode === 'tomorrow' ? '已进入【明日预排】模式' : '已返回【今日打卡】模式');
    };

    // ==================== 训练与饮食综合日历引擎 ====================
    const calendarYear = ref(now.getFullYear());
    const calendarMonth = ref(now.getMonth());
    const selectedCalendarDate = ref(todayDate.value);

    const calendarTitle = computed(() => {
      return `${calendarYear.value}年 ${calendarMonth.value + 1}月`;
    });

    const prevMonth = () => {
      if (calendarMonth.value === 0) {
        calendarMonth.value = 11;
        calendarYear.value -= 1;
      } else {
        calendarMonth.value -= 1;
      }
    };

    const nextMonth = () => {
      if (calendarMonth.value === 11) {
        calendarMonth.value = 0;
        calendarYear.value += 1;
      } else {
        calendarMonth.value += 1;
      }
    };

    const goToTodayCalendar = () => {
      const d = new Date();
      calendarYear.value = d.getFullYear();
      calendarMonth.value = d.getMonth();
      selectedCalendarDate.value = formatDate(d);
    };

    const selectCalendarDate = (dateStr) => {
      selectedCalendarDate.value = dateStr;
    };

    // 辅助：获取任意一天的训练数据（从 dailyPlans 或 historyLogs 或当前表单）
    const getDayWorkoutData = (dateStr) => {
      if (dateStr === activePlanDate.value) {
        return {
          volleyball: todayVolleyball.value.enabled ? { ...todayVolleyball.value } : null,
          treadmill: todayTreadmill.value.enabled ? { ...todayTreadmill.value } : null,
          exercises: [...todayExercises.value],
          totalCalories: todayTotalCalories.value,
          totalVolume: strengthStats.value.volume
        };
      }
      const hist = historyLogs.value.find(l => l.date === dateStr);
      if (hist) {
        return {
          volleyball: hist.volleyball,
          treadmill: hist.treadmill,
          exercises: hist.exercises || [],
          totalCalories: hist.totalCalories || 0,
          totalVolume: hist.totalVolume || 0
        };
      }
      const plan = dailyPlans.value[dateStr];
      if (plan) {
        let cal = 0;
        let vol = 0;
        if (plan.volleyball && plan.volleyball.enabled) {
          cal += CalorieCalculator.calculateVolleyball(userProfile.value.weight, plan.volleyball.intensity, plan.volleyball.duration).calories;
        }
        if (plan.treadmill && plan.treadmill.enabled) {
          cal += CalorieCalculator.calculateInclineTreadmill(userProfile.value.weight, plan.treadmill.speed, plan.treadmill.incline, plan.treadmill.duration).calories;
        }
        (plan.exercises || []).forEach(ex => {
          const res = CalorieCalculator.calculateStrengthExercise(userProfile.value.weight, ex, ex.sets || []);
          cal += res.calories;
          vol += res.totalVolume;
        });
        return {
          volleyball: (plan.volleyball && plan.volleyball.enabled) ? plan.volleyball : null,
          treadmill: (plan.treadmill && plan.treadmill.enabled) ? plan.treadmill : null,
          exercises: plan.exercises || [],
          totalCalories: cal,
          totalVolume: vol
        };
      }
      return {
        volleyball: null,
        treadmill: null,
        exercises: [],
        totalCalories: 0,
        totalVolume: 0
      };
    };

    // 辅助：获取任意一天的餐食数据
    const getDayMealsData = (dateStr) => {
      if (dateStr === activePlanDate.value && todayMeals.value && todayMeals.value.length) {
        return todayMeals.value;
      }
      return dailyMeals.value[dateStr] || [];
    };

    // 日历网格计算属性 (周一起始)
    const calendarGrid = computed(() => {
      const y = calendarYear.value;
      const m = calendarMonth.value;

      const firstDayOfMonth = new Date(y, m, 1);
      const lastDayOfMonth = new Date(y, m + 1, 0);

      const daysInMonth = lastDayOfMonth.getDate();
      const startDayOfWeek = (firstDayOfMonth.getDay() + 6) % 7; // 0: 周一, ... 6: 周日

      const bmr = bmrCalories.value;
      const grid = [];

      // 上月占位天数
      const prevMonthLastDay = new Date(y, m, 0).getDate();
      for (let i = startDayOfWeek - 1; i >= 0; i--) {
        const dayNum = prevMonthLastDay - i;
        const prevDate = new Date(y, m - 1, dayNum);
        const dateStr = formatDate(prevDate);
        grid.push({
          dateStr,
          dayNum,
          isCurrentMonth: false,
          isToday: dateStr === todayDate.value,
          isSelected: dateStr === selectedCalendarDate.value,
          workout: null,
          meals: [],
          burn: 0,
          intake: 0,
          deficitStats: null
        });
      }

      // 当月真实天数
      for (let d = 1; d <= daysInMonth; d++) {
        const dateObj = new Date(y, m, d);
        const dateStr = formatDate(dateObj);
        const workout = getDayWorkoutData(dateStr);
        const meals = getDayMealsData(dateStr);

        let intake = 0;
        meals.forEach(meal => {
          intake += Number(meal.calories) || 0;
        });

        const hasData = (workout.totalCalories > 0 || workout.exercises.length > 0 || (workout.volleyball && workout.volleyball.enabled) || meals.length > 0);
        const deficitStats = hasData ? CalorieCalculator.calculateCalorieDeficit(bmr, workout.totalCalories, intake) : null;

        grid.push({
          dateStr,
          dayNum: d,
          isCurrentMonth: true,
          isToday: dateStr === todayDate.value,
          isSelected: dateStr === selectedCalendarDate.value,
          workout,
          meals,
          burn: workout.totalCalories,
          intake,
          hasData,
          deficitStats
        });
      }

      // 下月填充至 7 的倍数 (保持整齐矩形网格)
      const remaining = (7 - (grid.length % 7)) % 7;
      for (let j = 1; j <= remaining; j++) {
        const nextDate = new Date(y, m + 1, j);
        const dateStr = formatDate(nextDate);
        grid.push({
          dateStr,
          dayNum: j,
          isCurrentMonth: false,
          isToday: dateStr === todayDate.value,
          isSelected: dateStr === selectedCalendarDate.value,
          workout: null,
          meals: [],
          burn: 0,
          intake: 0,
          deficitStats: null
        });
      }

      return grid;
    });

    // 选中日期的综合全景档案
    const selectedDayDetail = computed(() => {
      const dateStr = selectedCalendarDate.value;
      const workout = getDayWorkoutData(dateStr);
      const meals = getDayMealsData(dateStr);

      const bmr = bmrCalories.value;

      let intake = 0;
      let carbs = 0;
      let protein = 0;
      let fat = 0;
      let fiber = 0;
      meals.forEach(m => {
        intake += Number(m.calories) || 0;
        carbs += Number(m.carbs) || 0;
        protein += Number(m.protein) || 0;
        fat += Number(m.fat) || 0;
        fiber += Number(m.fiber) || 0;
      });

      const deficitStats = CalorieCalculator.calculateCalorieDeficit(bmr, workout.totalCalories, intake);

      return {
        dateStr,
        workout,
        meals,
        bmr,
        exerciseBurn: workout.totalCalories,
        totalVolume: workout.totalVolume,
        nutritionTotal: {
          calories: Math.round(intake),
          carbs: Math.round(carbs),
          protein: Math.round(protein),
          fat: Math.round(fat),
          fiber: Math.round(fiber)
        },
        deficitStats
      };
    });

    const jumpToPlanFromCalendar = (dateStr) => {
      syncCurrentFormToDict();
      syncMealsToDict();
      if (dateStr === todayDate.value) {
        planDateMode.value = 'today';
      } else if (dateStr === tomorrowDate.value) {
        planDateMode.value = 'tomorrow';
      } else {
        planDateMode.value = 'today';
      }
      loadPlanFromDict(dateStr);
      loadMealsFromDict(dateStr);
      activeTab.value = 'today';
      showToast(`已切换至【${dateStr}】训练计划`);
    };

    const jumpToNutritionFromCalendar = (dateStr) => {
      syncCurrentFormToDict();
      syncMealsToDict();
      loadMealsFromDict(dateStr);
      activeTab.value = 'nutrition';
      showToast(`已切换至【${dateStr}】饮食记录`);
    };

    // ================= AI 饮食与营养相机 =================
    const onMealImageSelected = (e) => {
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = (event) => {
        mealImageBase64.value = event.target.result;
        showToast('餐食图片已加载');
      };
      reader.readAsDataURL(file);
    };

    const clearMealImage = () => {
      mealImageBase64.value = '';
    };

    const triggerAnalyzeMeal = async () => {
      if (!mealImageBase64.value && !mealTextDescription.value.trim()) {
        showToast('请上传餐食照片或输入食材说明');
        return;
      }

      isAnalyzingMeal.value = true;
      try {
        const res = await NutritionAI.analyzeWithGemini(
          geminiApiKey.value.trim(),
          mealImageBase64.value,
          mealTextDescription.value.trim()
        );
        if (res.success && res.data) {
          mealAnalysisResult.value = res.data;
          showToast('🎉 AI 营养分析完成！');
        } else {
          showToast('分析暂未完成，请重试');
        }
      } catch (err) {
        showToast('分析出错：' + err.message);
      } finally {
        isAnalyzingMeal.value = false;
      }
    };

    const logMealToToday = (result) => {
      if (!result) return;
      const mealEntry = {
        id: 'meal_' + Date.now(),
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        dishName: result.dishName || '自选餐食',
        calories: Number(result.calories) || 0,
        carbs: Number(result.carbs) || 0,
        protein: Number(result.protein) || 0,
        fat: Number(result.fat) || 0,
        fiber: Number(result.fiber) || 0,
        advice: result.volleyballAdvice || ''
      };
      todayMeals.value.unshift(mealEntry);
      syncMealsToDict();
      saveState();
      showToast(`已将【${mealEntry.dishName}】记入今日摄入！`);
    };

    const removeMeal = (index) => {
      todayMeals.value.splice(index, 1);
      syncMealsToDict();
      saveState();
      showToast('已移除餐食');
    };

    const jumpToWebGemini = () => {
      NutritionAI.generateWebPromptAndJump(mealTextDescription.value);
      showToast('📋 营养提示词已复制！正在打开 Gemini 网页版...');
    };

    const applyPastedAiResult = () => {
      if (!pastedAiText.value.trim()) return;
      const parsed = NutritionAI.parsePastedAiText(pastedAiText.value);
      if (parsed) {
        mealAnalysisResult.value = parsed;
        showPasteAiModal.value = false;
        pastedAiText.value = '';
        showToast('已成功提取网页端 AI 营养数据！');
      } else {
        showToast('未能识别出营养数值，请核对文字');
      }
    };

    // ================= 动作管理与组数记录 =================
    const addExerciseToToday = (ex) => {
      const existing = todayExercises.value.find(e => e.id === ex.id);
      if (existing) {
        showToast(`已在计划列表中，可直接调整组数`);
        activeTab.value = 'today';
        return;
      }

      const sets = [];
      const count = ex.defaultSets || 4;
      for (let i = 1; i <= count; i++) {
        sets.push({
          setNumber: i,
          weight: ex.defaultWeight || 0,
          reps: ex.defaultReps || 10,
          completed: false
        });
      }

      todayExercises.value.push({
        ...ex,
        sets
      });

      showToast(`已加入${planDateMode.value === 'tomorrow' ? '明日' : '今日'}计划`);
      syncCurrentFormToDict();
      saveState();
    };

    const removeExercise = (index) => {
      todayExercises.value.splice(index, 1);
      syncCurrentFormToDict();
      saveState();
      showToast('已移除动作');
    };

    const addSet = (exercise) => {
      const nextNum = (exercise.sets.length || 0) + 1;
      const lastSet = exercise.sets[exercise.sets.length - 1];
      exercise.sets.push({
        setNumber: nextNum,
        weight: lastSet ? lastSet.weight : (exercise.defaultWeight || 0),
        reps: lastSet ? lastSet.reps : (exercise.defaultReps || 10),
        completed: false
      });
      syncCurrentFormToDict();
      saveState();
    };

    const removeSet = (exercise, setIndex) => {
      exercise.sets.splice(setIndex, 1);
      exercise.sets.forEach((s, idx) => s.setNumber = idx + 1);
      syncCurrentFormToDict();
      saveState();
    };

    const toggleAllSets = (exercise) => {
      const allCompleted = exercise.sets.every(s => s.completed);
      exercise.sets.forEach(s => s.completed = !allCompleted);
      syncCurrentFormToDict();
      saveState();
    };

    const toggleSet = (set) => {
      set.completed = !set.completed;
      syncCurrentFormToDict();
      saveState();
    };

    // ================= 智能推荐应用 =================
    const applyRecommendation = () => {
      const rec = recommendedWorkout.value;
      if (!rec || !rec.exercises) return;

      const cardioItem = rec.exercises.find(e => e.isCardio);
      if (cardioItem) {
        todayTreadmill.value.enabled = true;
        todayTreadmill.value.duration = cardioItem.duration || 25;
        todayTreadmill.value.incline = cardioItem.incline || 12;
        todayTreadmill.value.speed = cardioItem.speed || 4.5;
      }

      rec.exercises.forEach(recItem => {
        if (recItem.isCardio) return;
        const exDb = EXERCISE_DATABASE.find(e => e.id === recItem.exerciseId);
        if (!exDb) return;

        const alreadyIn = todayExercises.value.find(e => e.id === exDb.id);
        if (!alreadyIn) {
          const sets = [];
          for (let i = 1; i <= recItem.sets; i++) {
            sets.push({
              setNumber: i,
              weight: recItem.weight,
              reps: recItem.reps,
              completed: false
            });
          }
          todayExercises.value.push({
            ...exDb,
            note: recItem.note,
            sets
          });
        }
      });

      activeTab.value = 'today';
      syncCurrentFormToDict();
      saveState();
      showToast(`已成功载入【${rec.title}】！`);
    };

    // ================= 归档与历史记录 =================
    const saveTodayAsLog = () => {
      syncCurrentFormToDict();

      if (todayTotalCalories.value === 0 && todayExercises.value.length === 0) {
        showToast('当前计划尚未添加任何动作或排球');
        return;
      }

      if (todayVolleyball.value.enabled) {
        fatigue.value.shoulder = todayVolleyball.value.shoulderFatigue;
        fatigue.value.knee = todayVolleyball.value.kneeFatigue;
      }

      const logEntry = {
        id: 'log_' + Date.now(),
        date: activePlanDate.value,
        createdAt: new Date().toISOString(),
        totalCalories: todayTotalCalories.value,
        totalVolume: strengthStats.value.volume,
        fatigue: { ...fatigue.value },
        volleyball: todayVolleyball.value.enabled ? { ...todayVolleyball.value } : null,
        treadmill: todayTreadmill.value.enabled ? { ...todayTreadmill.value } : null,
        exercises: JSON.parse(JSON.stringify(todayExercises.value))
      };

      const existingIdx = historyLogs.value.findIndex(l => l.date === activePlanDate.value);
      if (existingIdx >= 0) {
        historyLogs.value[existingIdx] = logEntry;
      } else {
        historyLogs.value.unshift(logEntry);
      }

      saveState();
      showToast(planDateMode.value === 'tomorrow' ? '🎉 明日预排计划已成功保存！' : '🎉 今日训练已成功归档保存！');
    };

    const resetTodayPlan = () => {
      if (confirm(`确定要清空${planDateMode.value === 'tomorrow' ? '明日' : '今日'}的计划吗？`)) {
        todayExercises.value = [];
        todayVolleyball.value.enabled = false;
        todayTreadmill.value.enabled = false;
        syncCurrentFormToDict();
        saveState();
        showToast('已重置计划');
      }
    };

    // ================= 数据持久化与云同步 =================
    const saveState = () => {
      syncCurrentFormToDict();
      syncMealsToDict();
      const stateToSave = {
        userProfile: userProfile.value,
        fatigue: fatigue.value,
        todayDate: todayDate.value,
        planDateMode: planDateMode.value,
        dailyPlans: dailyPlans.value,
        dailyMeals: dailyMeals.value,
        todayVolleyball: todayVolleyball.value,
        todayTreadmill: todayTreadmill.value,
        todayExercises: todayExercises.value,
        todayMeals: todayMeals.value,
        geminiApiKey: geminiApiKey.value,
        historyLogs: historyLogs.value
      };
      SyncEngine.saveLocalData(stateToSave);
    };

    const loadState = () => {
      syncCode.value = SyncEngine.getOrCreateSyncCode();
      const localData = SyncEngine.loadLocalData();
      
      if (localData) {
        if (localData.userProfile) {
          userProfile.value = { ...userProfile.value, ...localData.userProfile };
          if (typeof userProfile.value.macroCarbsRatio === 'undefined') userProfile.value.macroCarbsRatio = 3.0;
          if (typeof userProfile.value.macroProteinRatio === 'undefined') userProfile.value.macroProteinRatio = 1.7;
          if (typeof userProfile.value.macroFatRatio === 'undefined') userProfile.value.macroFatRatio = 1.0;
          if (userProfile.value.weight === 76) {
            userProfile.value.weight = 78;
          }
        }
        if (localData.fatigue) fatigue.value = { ...fatigue.value, ...localData.fatigue };
        if (localData.historyLogs && Array.isArray(localData.historyLogs)) {
          historyLogs.value = localData.historyLogs;
        }
        if (localData.dailyPlans) {
          dailyPlans.value = localData.dailyPlans;
        }
        if (localData.dailyMeals) {
          dailyMeals.value = localData.dailyMeals;
        }
        if (localData.todayMeals) {
          todayMeals.value = localData.todayMeals;
        }
        if (localData.geminiApiKey) {
          geminiApiKey.value = localData.geminiApiKey;
        }
      }

      // 归档昨日（2026-11-23）练背记录
      const hasYesterdayLog = historyLogs.value.some(l => l.date === '2026-11-23');
      if (!hasYesterdayLog) {
        historyLogs.value.unshift(YESTERDAY_BACK_LOG);
      }

      // 确保今日（2026-11-24）计划已有实战推力与核心方案
      if (!dailyPlans.value[todayDate.value] || (!dailyPlans.value[todayDate.value].exercises?.length && !dailyPlans.value[todayDate.value].volleyball?.enabled)) {
        dailyPlans.value[todayDate.value] = dailyPlans.value['2026-11-24'] || JSON.parse(JSON.stringify(TOMORROW_PRESET_PLAN));
      }

      // 默认模式锁定为【今日打卡】
      planDateMode.value = 'today';

      // 载入今日打卡计划与今日餐食
      loadPlanFromDict(todayDate.value);
      loadMealsFromDict(todayDate.value);
    };

    const pushSync = async () => {
      syncStatus.value = { loading: true, message: '正在同步上传至云端...', type: 'info' };
      syncCurrentFormToDict();
      syncMealsToDict();
      const currentData = {
        userProfile: userProfile.value,
        fatigue: fatigue.value,
        todayDate: todayDate.value,
        planDateMode: planDateMode.value,
        dailyPlans: dailyPlans.value,
        dailyMeals: dailyMeals.value,
        todayVolleyball: todayVolleyball.value,
        todayTreadmill: todayTreadmill.value,
        todayExercises: todayExercises.value,
        todayMeals: todayMeals.value,
        geminiApiKey: geminiApiKey.value,
        historyLogs: historyLogs.value
      };
      const res = await SyncEngine.pushToCloud(currentData, syncCode.value);
      syncStatus.value = { 
        loading: false, 
        message: res.message, 
        type: res.success ? 'success' : 'warning' 
      };
      showToast(res.message);
    };

    const pullSync = async () => {
      const codeToPull = inputSyncCode.value.trim() || syncCode.value;
      syncStatus.value = { loading: true, message: `正在从云端拉取口令【${codeToPull.toUpperCase()}】数据...`, type: 'info' };
      
      const res = await SyncEngine.pullFromCloud(codeToPull);
      if (res.success && res.data) {
        const cloudData = res.data;
        if (cloudData.userProfile) userProfile.value = cloudData.userProfile;
        if (cloudData.fatigue) fatigue.value = cloudData.fatigue;
        if (cloudData.historyLogs) historyLogs.value = cloudData.historyLogs;
        if (cloudData.dailyPlans) dailyPlans.value = cloudData.dailyPlans;
        if (cloudData.dailyMeals) dailyMeals.value = cloudData.dailyMeals;
        if (cloudData.todayMeals) todayMeals.value = cloudData.todayMeals;
        if (cloudData.geminiApiKey) geminiApiKey.value = cloudData.geminiApiKey;

        loadPlanFromDict(activePlanDate.value);

        if (inputSyncCode.value.trim()) {
          syncCode.value = SyncEngine.setSyncCode(inputSyncCode.value.trim());
          inputSyncCode.value = '';
        }

        saveState();
        syncStatus.value = { loading: false, message: '✅ 同步拉取完成！数据已更新', type: 'success' };
        showToast('✅ 数据已成功同步！');
      } else {
        syncStatus.value = { loading: false, message: res.message, type: 'error' };
        showToast(res.message);
      }
    };

    const copySyncCode = () => {
      navigator.clipboard.writeText(syncCode.value);
      showToast(`已复制同步口令：${syncCode.value}`);
    };

    const exportBackupFile = () => {
      syncCurrentFormToDict();
      const dataStr = SyncEngine.exportJson({
        userProfile: userProfile.value,
        fatigue: fatigue.value,
        dailyPlans: dailyPlans.value,
        todayMeals: todayMeals.value,
        historyLogs: historyLogs.value
      });
      const blob = new Blob([dataStr], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `SpikeFit_Backup_${todayDate.value}.json`;
      a.click();
      URL.revokeObjectURL(url);
      showToast('备份文件已下载');
    };

    const importBackupFile = (event) => {
      const file = event.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = (e) => {
        const res = SyncEngine.importJson(e.target.result);
        if (res.success) {
          loadState();
          showToast('备份导入成功！');
        } else {
          showToast('导入失败：' + res.message);
        }
      };
      reader.readAsText(file);
    };

    const forceClearCacheAndReload = async () => {
      showToast('正在清理缓存并同步最新版本...');
      try {
        if ('caches' in window) {
          const keys = await caches.keys();
          await Promise.all(keys.map(k => caches.delete(k)));
        }
        if ('serviceWorker' in navigator) {
          const regs = await navigator.serviceWorker.getRegistrations();
          await Promise.all(regs.map(r => r.unregister()));
        }
      } catch (e) {
        console.error(e);
      }
      setTimeout(() => {
        window.location.reload(true);
      }, 500);
    };

    const checkServerInfo = async () => {
      try {
        const resp = await fetch('/api/server_info');
        if (resp.ok) {
          const info = await resp.json();
          if (info && info.mobileUrl) {
            mobileLanUrl.value = info.mobileUrl;
          }
        }
      } catch (e) {
        // 静态文件忽略
      }
    };

    onMounted(() => {
      loadState();
      checkServerInfo();
      if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('./sw.js?v=20261124_02').then(reg => {
          reg.update();
        }).catch(err => {
          console.log('SW registration note:', err);
        });
      }
    });

    return {
      activeTab,
      todayDate,
      tomorrowDate,
      todayDateShort,
      tomorrowDateShort,
      planDateMode,
      activePlanDate,
      switchPlanDate,
      userProfile,
      fatigue,
      todayVolleyball,
      todayTreadmill,
      todayExercises,
      historyLogs,
      geminiApiKey,
      mealImageBase64,
      mealTextDescription,
      isAnalyzingMeal,
      mealAnalysisResult,
      pastedAiText,
      showPasteAiModal,
      todayMeals,
      todayNutritionTotal,
      netEnergyBalance,
      bmrCalories,
      dailyEnergyDeficit,
      targetMacros,
      macrosComparison,
      activeMacroPreset,
      showMacroConfigDrawer,
      applyMacroPreset,
      dailyMeals,
      calendarYear,
      calendarMonth,
      calendarTitle,
      selectedCalendarDate,
      selectedDayDetail,
      calendarGrid,
      prevMonth,
      nextMonth,
      goToTodayCalendar,
      selectCalendarDate,
      jumpToPlanFromCalendar,
      jumpToNutritionFromCalendar,
      onMealImageSelected,
      clearMealImage,
      triggerAnalyzeMeal,
      logMealToToday,
      removeMeal,
      jumpToWebGemini,
      applyPastedAiResult,
      syncCode,
      inputSyncCode,
      syncStatus,
      showQrModal,
      mobileLanUrl,
      qrCodeImageUrl,
      librarySearch,
      libraryCategory,
      libraryEquipment,
      selectedExerciseDetail,
      showExerciseIllustrationModal,
      currentIllustration,
      currentIllustrationExercise,
      openExerciseIllustration,
      closeExerciseIllustration,
      getIllustrationSvg,
      toast,
      showToast,
      treadmillCalories,
      treadmillDetails,
      volleyballCalories,
      strengthStats,
      todayTotalCalories,
      calorieEquivalents,
      recommendedWorkout,
      filteredExercises,
      addExerciseToToday,
      removeExercise,
      addSet,
      removeSet,
      toggleAllSets,
      toggleSet,
      applyRecommendation,
      saveTodayAsLog,
      resetTodayPlan,
      pushSync,
      pullSync,
      copySyncCode,
      exportBackupFile,
      importBackupFile,
      forceClearCacheAndReload
    };
  }
});

app.mount('#app');
