/**
 * SpikeFit - 排球专项体能与健身动作库
 * 专为 24h 健身房（杠铃、哑铃、龙门架、固定器械、弹力带、爬坡机）量身定制
 */
const EXERCISE_DATABASE = [
  // ===================== 胸部力量 (CHEST) =====================
  {
    id: 'bench_press',
    name: '平板杠铃卧推',
    category: 'chest',
    categoryName: '胸部推力',
    equipment: '杠铃',
    targetMuscle: '胸大肌、肱三头肌、三角肌前束',
    whyForVolleyball: '构建基础推力底座，增强扣球挥臂力量与网前争顶对抗能力',
    defaultSets: 4,
    defaultReps: 8,
    defaultWeight: 60,
    met: 6.0,
    tips: '沉肩收胛，握距约 1.5 倍肩宽，杠铃下落至胸骨下沿，发力推起但肘关节不超伸锁死。'
  },
  {
    id: 'incline_db_press',
    name: '上斜哑铃卧推',
    category: 'chest',
    categoryName: '胸部推力',
    equipment: '哑铃/上斜凳',
    targetMuscle: '胸肌上束、前锯肌',
    whyForVolleyball: '强化上举推力，提升扣球高点触球时肩胸上部的支撑爆发力',
    defaultSets: 4,
    defaultReps: 10,
    defaultWeight: 20,
    met: 5.5,
    tips: '斜凳角度设为 30°-45°，下放时充分感受上胸拉伸，推至顶点微内合。'
  },
  {
    id: 'cable_fly',
    name: '龙门架绳索中位夹胸',
    category: 'chest',
    categoryName: '胸部推力',
    equipment: '龙门架绳索',
    targetMuscle: '胸大肌内侧与中缝',
    whyForVolleyball: '提供全程持续张力，模拟扣球挥臂向前内收时的肌肉控制感',
    defaultSets: 3,
    defaultReps: 12,
    defaultWeight: 15,
    met: 4.5,
    tips: '弓步微前倾，肘部微屈固定，意念集中在胸大肌将双臂环抱内收。'
  },
  {
    id: 'pushup_plus',
    name: '前锯肌俯卧撑 (Push-up Plus)',
    category: 'chest',
    categoryName: '胸部推力',
    equipment: '自重',
    targetMuscle: '前锯肌 (Serratus)、胸肌',
    whyForVolleyball: '【排球黄金动作】强化肩胛骨前引能力，防止扣球肩胛翼状突起，护肩必练',
    defaultSets: 3,
    defaultReps: 15,
    defaultWeight: 0,
    met: 4.0,
    tips: '推到最高点后，继续用力含胸推地，使肩胛骨完全分开贴紧胸廓。'
  },

  // ===================== 背部拉力 (BACK) =====================
  {
    id: 'pull_up',
    name: '正手引体向上',
    category: 'back',
    categoryName: '背部拉力',
    equipment: '龙门架单杠/引体架',
    targetMuscle: '背阔肌、大圆肌、二头肌',
    whyForVolleyball: '【滞空与制动核心】背阔肌是扣球从高处引臂下拉的最强动力源与空中稳定器',
    defaultSets: 4,
    defaultReps: 8,
    defaultWeight: 0,
    met: 7.0,
    tips: '沉肩启动，不要耸肩，挺胸将胸口贴近单杠，下放保持离心张力。'
  },
  {
    id: 'lat_pulldown',
    name: '宽握高位下拉',
    category: 'back',
    categoryName: '背部拉力',
    equipment: '高位下拉机/龙门架',
    targetMuscle: '背阔肌上外侧',
    whyForVolleyball: '安全积累背阔肌容量，增强扣球挥臂终末段的减速制动肌力',
    defaultSets: 4,
    defaultReps: 10,
    defaultWeight: 45,
    met: 5.5,
    tips: '身体微后倾，下拉至上胸锁骨位置，手肘朝向侧下方压紧。'
  },
  {
    id: 'cable_face_pull',
    name: '绳索面拉 (Face Pull)',
    category: 'back',
    categoryName: '背部拉力',
    equipment: '龙门架绳索/三头肌绳',
    targetMuscle: '三角肌后束、肩袖冈下肌、菱形肌',
    whyForVolleyball: '【排球防伤第一神技】对抗频繁扣球带来的圆肩与肩峰撞击，保护肩关节长久健康',
    defaultSets: 4,
    defaultReps: 15,
    defaultWeight: 15,
    met: 4.5,
    tips: '滑轮调至面部高度，大拇指朝后拉向眼睛两侧，终末段手腕向上翻做出外旋展开。'
  },
  {
    id: 'cable_seated_row',
    name: '坐姿绳索划船',
    category: 'back',
    categoryName: '背部拉力',
    equipment: '龙门架/坐姿划船机',
    targetMuscle: '中背部、菱形肌、竖脊肌',
    whyForVolleyball: '强化上背厚度与躯干直立耐力，扣球后落地维持躯干中立不弯腰',
    defaultSets: 4,
    defaultReps: 10,
    defaultWeight: 40,
    met: 5.0,
    tips: '保持脊柱中立，蹬实脚踏，后拉时挤压双侧肩胛骨，不要过度后仰借力。'
  },

  // ===================== 肩部与肩袖 (SHOULDER) =====================
  {
    id: 'overhead_press',
    name: '站姿杠铃推举 (OHP)',
    category: 'shoulder',
    categoryName: '肩部立体推力',
    equipment: '杠铃',
    targetMuscle: '三角肌前/中束、上胸、核心',
    whyForVolleyball: '将地面反作用力经核心传导至肩部过顶伸展，增强空中拦网与扣球顶峰刚度',
    defaultSets: 4,
    defaultReps: 8,
    defaultWeight: 40,
    met: 6.0,
    tips: '收紧臀部与核心，杠铃贴脸部垂直推起，头微前移锁定，切忌腰椎过度反弓。'
  },
  {
    id: 'db_lateral_raise',
    name: '哑铃侧平举',
    category: 'shoulder',
    categoryName: '肩部立体推力',
    equipment: '哑铃',
    targetMuscle: '三角肌中束',
    whyForVolleyball: '打造饱满肩部侧向防撞装甲，增强挥臂侧向动作稳定性',
    defaultSets: 4,
    defaultReps: 12,
    defaultWeight: 8,
    met: 4.5,
    tips: '肘微屈，手腕低于或平齐于手肘，抬至大臂与地面水平即可，下放慢节奏。'
  },
  {
    id: 'cable_external_rotation',
    name: '绳索肩外旋 (肩袖专项)',
    category: 'shoulder',
    categoryName: '肩部立体推力',
    equipment: '龙门架绳索',
    targetMuscle: '冈下肌、小圆肌 (肩袖肌群)',
    whyForVolleyball: '【扣球刹车皮】频繁扣球内旋发力后，外旋肩袖必须提供足够的刹车力，否则撕裂',
    defaultSets: 3,
    defaultReps: 15,
    defaultWeight: 5,
    met: 3.5,
    tips: '肘关节夹紧身体侧面（可夹毛巾），前臂从腹前向外侧平行转动，轻重量慢动作。'
  },
  {
    id: 'band_ytwl',
    name: '弹力带 Y-T-W-L 激活',
    category: 'shoulder',
    categoryName: '肩部立体推力',
    equipment: '弹力带',
    targetMuscle: '下斜方肌、菱形肌、肩袖',
    whyForVolleyball: '排球比赛或力量训练前的极佳肩关节唤醒热身，消除弹响',
    defaultSets: 2,
    defaultReps: 10,
    defaultWeight: 0,
    met: 3.5,
    tips: '双手执轻弹力带，依次做出 Y 字上举、T 字侧拉、W 字屈肘后夹、L 字外旋。'
  },

  // ===================== 下肢力量 (LEGS) =====================
  {
    id: 'barbell_squat',
    name: '杠铃深蹲',
    category: 'legs',
    categoryName: '下肢基石力量',
    equipment: '杠铃/深蹲架',
    targetMuscle: '股四头肌、臀大肌、内收肌、核心',
    whyForVolleyball: '【弹跳力量基石】深蹲 1RM 重量与垂直纵跳高度直接正相关，打下最高发力天花板',
    defaultSets: 4,
    defaultReps: 6,
    defaultWeight: 80,
    met: 7.5,
    tips: '双脚略宽于肩，脚尖外展 20°-30°，屈髋屈膝同步，膝盖对准第二脚趾，下蹲至大腿平齐或略低。'
  },
  {
    id: 'romanian_deadlift',
    name: '罗马尼亚硬拉 (RDL)',
    category: 'legs',
    categoryName: '下肢基石力量',
    equipment: '杠铃/哑铃',
    targetMuscle: '腘绳肌、臀大肌、竖脊肌',
    whyForVolleyball: '【蓄力屈髋引擎】排球双脚助跑起跳蓄力完全依靠后侧链弹簧蓄能，极度重要',
    defaultSets: 4,
    defaultReps: 8,
    defaultWeight: 70,
    met: 6.5,
    tips: '微屈膝锁定角度，主动向后推臀折叠髋关节，杠铃紧贴小腿下放至小腿中部拉紧腘绳肌。'
  },
  {
    id: 'bulgarian_split_squat',
    name: '保加利亚分腿蹲',
    category: 'legs',
    categoryName: '下肢基石力量',
    equipment: '哑铃/卧推凳',
    targetMuscle: '单侧股四头肌、臀中肌、稳定肌群',
    whyForVolleyball: '消除单双侧起跳力量失衡，纠正扣球落地晃动，增强单腿制动稳定性',
    defaultSets: 3,
    defaultReps: 10,
    defaultWeight: 12,
    met: 6.0,
    tips: '后脚脚背搭在卧推凳上，重心落在前脚脚后跟偏外侧，直上直下，躯干微前倾。'
  },
  {
    id: 'standing_calf_raise',
    name: '提踵力量训练',
    category: 'legs',
    categoryName: '下肢基石力量',
    equipment: '哑铃/史密斯机/踏板',
    targetMuscle: '腓肠肌、比目鱼肌、跟腱',
    whyForVolleyball: '起跳终末瞬间脚踝的瞬间蹬伸输出最后 15-20% 的弹跳推力',
    defaultSets: 4,
    defaultReps: 15,
    defaultWeight: 20,
    met: 4.5,
    tips: '脚前掌踩在踏板边缘，下落到最低充分拉伸跟腱，爆发推起在最高点顶峰收缩 1 秒。'
  },
  {
    id: 'tibialis_raise',
    name: '胫骨前肌抬脚尖 (Tibialis Raise)',
    category: 'legs',
    categoryName: '下肢基石力量',
    equipment: '自重靠墙/杠铃片',
    targetMuscle: '胫骨前肌 (小腿前侧)',
    whyForVolleyball: '【防跳跃膝秘密武器】排球落地第一道刹车吸震器，强化它可有效缓解髌腱炎痛感',
    defaultSets: 3,
    defaultReps: 20,
    defaultWeight: 0,
    met: 3.5,
    tips: '背靠墙站立双腿向前跨出半步，脚跟着地，尽可能用力将脚尖向上勾起，停顿 1 秒。'
  },

  // ===================== 扣球核心专项 (SPIKING CORE) =====================
  {
    id: 'cable_woodchopper_high_low',
    name: '龙门架高位斜向伐木 (Cable Woodchopper)',
    category: 'volleyball_core',
    categoryName: '扣球核心爆发力',
    equipment: '龙门架绳索/手柄',
    targetMuscle: '腹内外斜肌、前侧核心、髋转子',
    whyForVolleyball: '【扣球发力动作孪生版】高位起手往斜下方砍下，完美重现扣球空中转体收腹的动能爆发',
    defaultSets: 4,
    defaultReps: 12,
    defaultWeight: 15,
    met: 5.5,
    tips: '滑轮调至最高，侧对龙门架双手握把手，后脚蹬地转髋带动核心，将绳索斜下拉向对侧膝盖外侧。'
  },
  {
    id: 'hanging_knee_twist',
    name: '单杠悬垂收腹转体',
    category: 'volleyball_core',
    categoryName: '扣球核心爆发力',
    equipment: '单杠/引体杆',
    targetMuscle: '腹直肌下段、腹斜肌、髂腰肌',
    whyForVolleyball: '完全脱离地面支撑，训练身体悬空时对抗重力快速卷腹扣球的收缩力量',
    defaultSets: 3,
    defaultReps: 12,
    defaultWeight: 0,
    met: 5.0,
    tips: '双手握单杠身体自然悬垂，腹部发力将膝盖抬起并向左/右斜向旋转收卷，控制下放速度。'
  },
  {
    id: 'pallof_press',
    name: '帕洛夫抗旋转推举 (Pallof Press)',
    category: 'volleyball_core',
    categoryName: '扣球核心爆发力',
    equipment: '龙门架绳索/弹力带',
    targetMuscle: '深层横突肌、腹横肌、抗旋转肌群',
    whyForVolleyball: '扣球空中身体若发生不必要的晃动会直接丢失击球点，此动作打造绝对躯干刚度',
    defaultSets: 3,
    defaultReps: 12,
    defaultWeight: 12,
    met: 4.5,
    tips: '侧对龙门架，双手握把手置于胸前，抵抗绳索侧向拉力，平稳向前推出手臂停留 2 秒收回。'
  },
  {
    id: 'band_rotational_punch',
    name: '弹力带/绳索爆发转体冲拳',
    category: 'volleyball_core',
    categoryName: '扣球核心爆发力',
    equipment: '弹力带/龙门架',
    targetMuscle: '旋转肌链、三角肌前束、腹斜肌',
    whyForVolleyball: '训练从脚掌蹬地经转髋、转躯干瞬间传导至上肢打手出球的鞭打传动速度',
    defaultSets: 4,
    defaultReps: 10,
    defaultWeight: 10,
    met: 5.5,
    tips: '背对锚点呈击球准备姿态，后脚转髋蹬地，核心暴发性旋转同时单手向前挥击冲拳。'
  },
  {
    id: 'barbell_rollout',
    name: '杠铃推腹抗伸展 (Barbell Rollout)',
    category: 'volleyball_core',
    categoryName: '扣球核心爆发力',
    equipment: '杠铃杆+轻片',
    targetMuscle: '腹直肌全段、背阔肌、骨盆稳定肌',
    whyForVolleyball: '模拟扣球时极度拉弓展开后的防过伸保护，避免脊椎超伸拉伤，提供强大收腹拉力',
    defaultSets: 3,
    defaultReps: 10,
    defaultWeight: 10,
    met: 5.0,
    tips: '双膝跪地，双手握杠铃杆向前推出至身体接近平直，核心收紧不塌腰，靠腹肌力量拉回。'
  },

  // ===================== 垂直弹跳专项 (VERTICAL JUMP) =====================
  {
    id: 'pogo_hops',
    name: '踝关节弹性小跳 (Pogo Hops)',
    category: 'vertical_jump',
    categoryName: '垂直弹跳与跟腱',
    equipment: '自重平地',
    targetMuscle: '跟腱刚度、腓肠肌、足弓',
    whyForVolleyball: '【跟腱弹簧化】缩短触地时间（GCT），将跟腱变成高弹性弹簧，强化排球二次起跳反应速度',
    defaultSets: 4,
    defaultReps: 25,
    defaultWeight: 0,
    met: 7.0,
    tips: '膝关节微屈但锁定角度不深蹲，主要依靠脚踝与前脚掌快速蹬地小跳，像蹦床一样弹性反弹。'
  },
  {
    id: 'db_jump_squat',
    name: '哑铃轻负重深蹲跳',
    category: 'vertical_jump',
    categoryName: '垂直弹跳与跟腱',
    equipment: '轻哑铃 (3-8kg)',
    targetMuscle: '下肢三关节快速伸展爆发力',
    whyForVolleyball: '在力量向速度转化的黄金区间（20% 1RM）训练最大功率输出（Peak Power）',
    defaultSets: 4,
    defaultReps: 5,
    defaultWeight: 5,
    met: 8.0,
    tips: '手持轻哑铃，快速半蹲蓄力（不可蹲太深），立即全力向上暴发跃起，落地轻柔。'
  },
  {
    id: 'box_jump_soft_landing',
    name: '跳箱/稳固踏板跳 + 柔和落地',
    category: 'vertical_jump',
    categoryName: '垂直弹跳与跟腱',
    equipment: '踏板/跳箱 (40-60cm)',
    targetMuscle: '垂直爆发力、离心缓冲',
    whyForVolleyball: '跳上高处大幅消除落地的地面对膝盖关节的冲击力，是排球摸高安全训练首选',
    defaultSets: 4,
    defaultReps: 6,
    defaultWeight: 0,
    met: 7.5,
    tips: '双臂充分后摆后蹬地暴发起跳，落在跳箱上时像猫一样轻盈安静，站直后走下来而非跳下。'
  },
  {
    id: 'single_leg_drop_freeze',
    name: '单腿着地制动缓冲 (Drop & Freeze)',
    category: 'vertical_jump',
    categoryName: '垂直弹跳与跟腱',
    equipment: '台阶/自重',
    targetMuscle: '臀中肌、膝周稳定肌群',
    whyForVolleyball: '排球比赛很多救球或网口拼抢是单脚落地，此动作是防止膝盖内扣、前交叉韧带扭伤的关键',
    defaultSets: 3,
    defaultReps: 8,
    defaultWeight: 0,
    met: 5.0,
    tips: '从小台阶迈下单脚落地，瞬间屈髋屈膝“凝固”静止 2 秒，膝盖坚决不向内扣。'
  },

  // ===================== 有氧与实战 (CARDIO & VOLLEYBALL) =====================
  {
    id: 'incline_treadmill',
    name: '健身房坡度爬坡 (Incline Treadmill)',
    category: 'cardio',
    categoryName: '有氧与能耗',
    equipment: '爬坡跑步机',
    targetMuscle: '心肺耐力、臀大肌、小腿后链',
    whyForVolleyball: '【极佳低冲击有氧】完全避免了公路慢跑对跳跃膝盖的反复震荡，同时强化臀部后链发力',
    defaultDuration: 30, // 分钟
    defaultIncline: 12,  // 坡度 %
    defaultSpeed: 4.5,   // 时速 km/h
    met: 8.5,            // 动态计算
    tips: '握把尽量少扶或只用于保持平衡，挺胸收腹，大步用脚后跟过渡到脚掌蹬伸。'
  },
  {
    id: 'volleyball_casual',
    name: '排球休闲对抗 / 基础传垫',
    category: 'cardio',
    categoryName: '有氧与能耗',
    equipment: '排球场',
    targetMuscle: '全身协调、灵敏步伐、低强度有氧',
    whyForVolleyball: '维持球感与步法移动，属于主动恢复与低负荷练习',
    defaultDuration: 60,
    met: 4.0,
    tips: '注意热身脚踝与肩部，以动作手感与脚底移动到位为主。'
  },
  {
    id: 'volleyball_competitive',
    name: '排球高强度实战对抗 / 扣球比赛',
    category: 'cardio',
    categoryName: '有氧与能耗',
    equipment: '排球场',
    targetMuscle: '全身无氧间歇、爆发起跳、肩臂挥击',
    whyForVolleyball: '真刀真枪的实战体能消耗，高频起跳与暴力扣杀',
    defaultDuration: 90,
    met: 8.0,
    tips: '赛后务必进行肩袖拉伸、泡沫轴滚压大腿与小腿放松。'
  },
  {
    id: 'volleyball_spike_session',
    name: '排球扣球弹跳专项打靶测试',
    category: 'cardio',
    categoryName: '有氧与能耗',
    equipment: '排球场/网口',
    targetMuscle: '极限摸高、起跳速度、扣球精准爆发',
    whyForVolleyball: '将力量房训练成果转化为网前进攻杀伤力',
    defaultDuration: 45,
    met: 6.0,
    tips: '质量优于数量，当明显感到弹跳高度下降或肩部乏力时及时收手。'
  }
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { EXERCISE_DATABASE };
}
