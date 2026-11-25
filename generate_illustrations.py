# -*- coding: utf-8 -*-
"""
生成 SpikeFit 全部 30 个排球与健身专项动作的高清 SVG 教学示意图与要领库
"""
import json
import os

ILLUSTRATIONS = {
    # 1. 平板杠铃卧推
    "bench_press": {
        "title": "平板杠铃卧推 (Barbell Bench Press)",
        "equipment": "杠铃 / 平板卧推凳",
        "target": "胸大肌整体、肱三头肌、三角肌前束",
        "volleyballFocus": "排球推力底座 · 扣球终末挥臂与网前拼抢支撑力",
        "breathing": "杠铃下放时深吸气蓄力，推起越过粘滞点时有力呼气。",
        "steps": [
            "双脚蹬实地面，臀部、上背部紧贴凳面，沉肩收紧肩胛骨，腰部自然微弓。",
            "双手采用全握，握距约 1.5 倍肩宽，将杠铃垂直起出置于胸部正上方。",
            "控制杠铃以微弧形轨迹离心下落至乳头下沿微触胸，保持手肘与躯干约 45°-60° 夹角。",
            "胸大肌发力向上爆发推起至顶点，肘关节保持微屈不锁死超伸。"
        ],
        "mistakes": [
            "双肩耸起或肩胛骨前引松懈，导致三角肌前束严重代偿压迫关节囊。",
            "手肘向两侧 90° 极度外展，极易引发肩峰撞击综合征。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0b1120"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <filter id="glowVolt" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <marker id="arrowUp" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto">
      <path d="M0,6 L3,0 L6,6 Z" fill="#00f59b"/>
    </marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad)"/>
  <line x1="20" y1="200" x2="380" y2="200" stroke="#1e293b" stroke-width="2"/>
  <!-- 卧推凳 -->
  <rect x="100" y="145" width="200" height="14" rx="4" fill="#334155"/>
  <rect x="130" y="159" width="12" height="41" fill="#1e293b"/>
  <rect x="258" y="159" width="12" height="41" fill="#1e293b"/>
  <rect x="70" y="90" width="14" height="110" rx="3" fill="#475569"/>
  <!-- 躺卧人物躯干 -->
  <circle cx="120" cy="138" r="13" fill="#cbd5e1"/>
  <rect x="132" y="132" width="115" height="15" rx="5" fill="#94a3b8"/>
  <!-- 发力胸大肌高亮 -->
  <ellipse cx="168" cy="132" rx="20" ry="10" fill="#00f59b" opacity="0.85" filter="url(#glowVolt)"/>
  <!-- 下肢屈膝踩地 -->
  <polyline points="247,137 285,155 288,200" fill="none" stroke="#64748b" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  <!-- 手臂推举轨迹 -->
  <polyline points="168,132 165,85" fill="none" stroke="#e2e8f0" stroke-width="6" stroke-linecap="round"/>
  <polyline points="175,132 175,85" fill="none" stroke="#e2e8f0" stroke-width="6" stroke-linecap="round"/>
  <!-- 杠铃杆与铃片 -->
  <line x1="70" y1="80" x2="270" y2="80" stroke="#cbd5e1" stroke-width="5"/>
  <rect x="75" y="60" width="10" height="40" rx="2" fill="#ef4444"/>
  <rect x="87" y="66" width="6" height="28" rx="2" fill="#3b82f6"/>
  <rect x="249" y="66" width="6" height="28" rx="2" fill="#3b82f6"/>
  <rect x="257" y="60" width="10" height="40" rx="2" fill="#ef4444"/>
  <!-- 发力运动箭头与标注 -->
  <line x1="170" y1="115" x2="170" y2="92" stroke="#00f59b" stroke-width="3" marker-end="url(#arrowUp)" stroke-dasharray="4,2"/>
  <text x="178" y="110" fill="#00f59b" font-size="11" font-weight="bold">推起发力</text>
  <text x="145" y="120" fill="#cbd5e1" font-size="10">胸大肌收缩</text>
  <text x="210" y="175" fill="#94a3b8" font-size="10">沉肩收胛 · 握距1.5倍肩宽</text>
</svg>"""
    },

    # 2. 上斜哑铃卧推
    "incline_db_press": {
        "title": "上斜哑铃卧推 (Incline DB Press)",
        "equipment": "哑铃 / 30°-45°可调节斜凳",
        "target": "胸大肌上束、三角肌前束、前锯肌",
        "volleyballFocus": "高点扣球与网前拦网举臂抗对抗的核心推力爆发源",
        "breathing": "哑铃在胸前沉降吸气充分拉伸上胸，推至高点微呼气夹胸。",
        "steps": [
            "调节可调凳角度为 30°-45°（角度过高易变成练肩），双脚平稳踩地。",
            "双手对握哑铃坐在凳上，借由大腿顶起哑铃，上背贴实，沉肩挺胸收腹。",
            "沿自然内收角度（与上身约 45°-60°）缓慢下放哑铃至上胸外侧拉伸点。",
            "发力将哑铃沿弧形轨迹向内上方推起，在最高点保持肘关节微屈顶峰收紧。"
        ],
        "mistakes": [
            "椅背角度过陡（如 60°-70°），会导致训练负荷几乎全落到肩部前束上。",
            "哑铃下落到底部时手腕过度背屈或手肘过度向后，造成前肩关节撕扯感。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad2" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowVolt2"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowUp2" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,6 L3,0 L6,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad2)"/>
  <line x1="20" y1="200" x2="380" y2="200" stroke="#1e293b" stroke-width="2"/>
  <!-- 35度上斜卧推凳 -->
  <line x1="90" y1="170" x2="200" y2="105" stroke="#334155" stroke-width="14" stroke-linecap="round"/>
  <rect x="75" y="165" width="40" height="12" rx="3" fill="#334155"/>
  <rect x="85" y="177" width="10" height="23" fill="#1e293b"/>
  <rect x="180" y="150" width="10" height="50" fill="#1e293b"/>
  <!-- 斜卧人物 -->
  <circle cx="195" cy="88" r="13" fill="#cbd5e1"/>
  <line x1="185" y1="98" x2="110" y2="148" stroke="#94a3b8" stroke-width="16" stroke-linecap="round"/>
  <!-- 上胸高亮 -->
  <ellipse cx="165" cy="110" rx="14" ry="9" fill="#00f59b" opacity="0.9" filter="url(#glowVolt2)"/>
  <!-- 下肢固定 -->
  <polyline points="105,155 125,185 140,200" fill="none" stroke="#64748b" stroke-width="7" stroke-linecap="round"/>
  <!-- 双臂上举与哑铃 -->
  <line x1="162" y1="110" x2="182" y2="55" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <rect x="168" y="45" width="28" height="10" rx="3" fill="#f59e0b"/>
  <line x1="172" y1="50" x2="192" y2="50" stroke="#ffffff" stroke-width="3"/>
  <!-- 发力弧度 -->
  <path d="M 155,95 Q 165,70 178,56" fill="none" stroke="#00f59b" stroke-width="2.5" stroke-dasharray="3,2" marker-end="url(#arrowUp2)"/>
  <text x="210" y="60" fill="#00f59b" font-size="11" font-weight="bold">上斜弧形上推</text>
  <text x="210" y="78" fill="#38bdf8" font-size="10">斜凳黄金 30°-45°</text>
  <text x="210" y="96" fill="#cbd5e1" font-size="10">胸大肌上束专注</text>
</svg>"""
    },

    # 3. 龙门架中位绳索夹胸
    "cable_fly": {
        "title": "龙门架中位绳索夹胸 (Cable Chest Fly)",
        "equipment": "龙门架 (双侧滑轮调至胸部高度) / D型手柄",
        "target": "胸大肌内侧中缝、胸肌整体持续张力",
        "volleyballFocus": "强化扣球挥臂中后段内收包球动作的肌肉控制力",
        "breathing": "双臂向外打开时吸气扩胸，双臂向前环抱汇合时呼气挤压。",
        "steps": [
            "将龙门架双侧滑轮调至与肩同高或略低，双手各握一把手，向前跨出一步呈弓步稳固站立。",
            "躯干微前倾，收紧核心，背部挺直，双肘保持微屈锁定（肘角全程不改变）。",
            "深吸气感受胸大肌被绳索水平向两侧充分拉伸。",
            "呼气，意念集中在胸肌将双臂像抱大树一样向前内侧弧形环抱，在身前相距10cm处顶峰收缩 1 秒。"
        ],
        "mistakes": [
            "将夹胸做成卧推推胸（肘部反复折叠弯曲借力三头肌）。",
            "身体剧烈前后晃动借用惯性甩动绳索。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad3" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowVolt3"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowIn" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,6 L3,0 L6,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad3)"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <!-- 龙门架双侧立柱 -->
  <rect x="40" y="40" width="12" height="165" fill="#334155"/>
  <rect x="348" y="40" width="12" height="165" fill="#334155"/>
  <circle cx="46" cy="110" r="7" fill="#64748b"/>
  <circle cx="354" cy="110" r="7" fill="#64748b"/>
  <!-- 人物站姿弓步俯视图微倾 -->
  <circle cx="200" cy="85" r="13" fill="#cbd5e1"/>
  <line x1="200" y1="98" x2="195" y2="148" stroke="#94a3b8" stroke-width="16" stroke-linecap="round"/>
  <polyline points="195,148 175,175 160,205" fill="none" stroke="#64748b" stroke-width="6" stroke-linecap="round"/>
  <polyline points="195,148 220,180 230,205" fill="none" stroke="#64748b" stroke-width="6" stroke-linecap="round"/>
  <!-- 胸大肌发力点高亮 -->
  <ellipse cx="200" cy="112" rx="16" ry="10" fill="#00f59b" opacity="0.9" filter="url(#glowVolt3)"/>
  <!-- 双臂环抱弧线 -->
  <path d="M 52,110 Q 130,120 185,120" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="4,2"/>
  <path d="M 348,110 Q 270,120 215,120" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="4,2"/>
  <polyline points="188,112 160,125 185,120" fill="none" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <polyline points="212,112 240,125 215,120" fill="none" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <circle cx="200" cy="120" r="6" fill="#38bdf8"/>
  <!-- 环抱轨迹箭头 -->
  <path d="M 140,135 Q 170,140 190,132" fill="none" stroke="#00f59b" stroke-width="2.5" marker-end="url(#arrowIn)"/>
  <path d="M 260,135 Q 230,140 210,132" fill="none" stroke="#00f59b" stroke-width="2.5" marker-end="url(#arrowIn)"/>
  <text x="160" y="55" fill="#00f59b" font-size="11" font-weight="bold">环抱向内挤压</text>
  <text x="145" y="70" fill="#cbd5e1" font-size="10">手肘微屈锁定 · 持续恒定张力</text>
</svg>"""
    },

    # 4. 前锯肌俯卧撑
    "pushup_plus": {
        "title": "前锯肌俯卧撑 (Push-up Plus)",
        "equipment": "自重 / 平整瑜伽垫",
        "target": "前锯肌 (Serratus Anterior)、肩胛胸壁动力稳定",
        "volleyballFocus": "【排球黄金动作】消除翼状肩胛，扣球挥臂肩胛骨贴紧胸廓防伤神技",
        "breathing": "常规下放吸气，推起至顶点并用力前引肩胛骨时完全吐气。",
        "steps": [
            "呈标准平板俯卧撑姿势，双手撑于肩正下方，双脚并拢，核心与臀部收紧成一条直线。",
            "屈肘下落至胸部接近地面，再正常推回到常规起始姿态。",
            "【关键Plus阶段】：保持手臂完全伸直，继续用力含胸推离地面，主动让两侧肩胛骨充分拉开并紧贴肋骨。",
            "在最高点维持顶峰前引 1-2 秒，充分感知肋骨两侧前锯肌的酸胀收缩。"
        ],
        "mistakes": [
            "塌腰骨盆前倾借力，导致腰椎代偿受力。",
            "在 Plus 阶段通过耸肩（抬起斜方肌）代替肩胛骨前引。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad4" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowVolt4"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowUp4" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,6 L3,0 L6,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad4)"/>
  <line x1="20" y1="200" x2="380" y2="200" stroke="#1e293b" stroke-width="2"/>
  <!-- 俯卧撑身体直线 -->
  <circle cx="100" cy="125" r="12" fill="#cbd5e1"/>
  <line x1="108" y1="130" x2="280" y2="165" stroke="#94a3b8" stroke-width="16" stroke-linecap="round"/>
  <!-- 前锯肌高亮 (胸侧肋骨) -->
  <ellipse cx="140" cy="138" rx="16" ry="10" fill="#00f59b" opacity="0.9" filter="url(#glowVolt4)"/>
  <!-- 笔直支撑双臂 -->
  <line x1="128" y1="134" x2="128" y2="200" stroke="#e2e8f0" stroke-width="6" stroke-linecap="round"/>
  <!-- 双脚蹬地 -->
  <circle cx="282" cy="168" r="5" fill="#64748b"/>
  <line x1="282" y1="168" x2="286" y2="200" stroke="#64748b" stroke-width="5"/>
  <!-- 额外推起 Plus 箭头与弧线 -->
  <line x1="135" y1="118" x2="135" y2="92" stroke="#00f59b" stroke-width="3" marker-end="url(#arrowUp4)"/>
  <path d="M 115,115 Q 135,95 155,115" fill="none" stroke="#00f59b" stroke-width="2" stroke-dasharray="3,2"/>
  <text x="145" y="88" fill="#00f59b" font-size="12" font-weight="black">PLUS 前引拱背</text>
  <text x="145" y="105" fill="#cbd5e1" font-size="10">肩胛骨贴紧胸壁 · 唤醒前锯肌</text>
  <text x="15" y="35" fill="#f59e0b" font-size="11" font-weight="bold">★ 排球护肩防撞击黄金动作</text>
</svg>"""
    },

    # 5. 正手引体向上
    "pull_up": {
        "title": "正手引体向上 (Pull-Up)",
        "equipment": "龙门架单杠 / 稳固引体单杠",
        "target": "背阔肌、大圆肌、二头肌、菱形肌",
        "volleyballFocus": "【扣球最强下压动力源】高点起跳后挥臂制动与空中身体稳定核心",
        "breathing": "身体悬垂时吸气收腹，发力向上拉起至过杠时匀速呼气。",
        "steps": [
            "正手抓握单杠，握距略宽于肩宽，双腿微屈交叉，身体自然下垂完全伸展背阔肌。",
            "沉肩启动（先下拉肩胛骨），挺胸仰头，眼睛看向单杠上方。",
            "背部两侧背阔肌主导发力，驱动手肘垂直向身体后侧下方挤压拉起身体。",
            "直至下巴过杠或胸口触及单杠，顶峰挤压 1 秒后，匀速离心下放复原。"
        ],
        "mistakes": [
            "借助前后大幅甩腿摆荡（借惯性），背阔肌受力大打折扣。",
            "上拉时耸肩含胸缩头，不仅无法刺激背阔肌，还会造成颈椎肩关节压迫。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad5" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowVolt5"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowUp5" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,6 L3,0 L6,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad5)"/>
  <!-- 单杠 -->
  <line x1="40" y1="45" x2="360" y2="45" stroke="#cbd5e1" stroke-width="6" stroke-linecap="round"/>
  <!-- 抓杠双手 -->
  <rect x="150" y="42" width="10" height="8" rx="2" fill="#94a3b8"/>
  <rect x="240" y="42" width="10" height="8" rx="2" fill="#94a3b8"/>
  <!-- 双臂弯曲下拉姿态 -->
  <polyline points="155,48 165,75 185,90" fill="none" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <polyline points="245,48 235,75 215,90" fill="none" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <!-- 头部与挺胸躯干 -->
  <circle cx="200" cy="65" r="13" fill="#cbd5e1"/>
  <path d="M 185,85 L 215,85 L 208,160 L 192,160 Z" fill="#94a3b8"/>
  <!-- 背阔肌双侧翼状高亮 -->
  <path d="M 185,85 L 170,115 L 192,145 Z" fill="#00f59b" opacity="0.9" filter="url(#glowVolt5)"/>
  <path d="M 215,85 L 230,115 L 208,145 Z" fill="#00f59b" opacity="0.9" filter="url(#glowVolt5)"/>
  <!-- 双下肢微屈 -->
  <polyline points="196,160 190,195 200,215" fill="none" stroke="#64748b" stroke-width="6" stroke-linecap="round"/>
  <!-- 发力上升箭头 -->
  <line x1="200" y1="120" x2="200" y2="82" stroke="#00f59b" stroke-width="3" marker-end="url(#arrowUp5)"/>
  <text x="245" y="105" fill="#00f59b" font-size="11" font-weight="bold">手肘向下夹紧</text>
  <text x="245" y="122" fill="#cbd5e1" font-size="10">背阔肌完全收缩</text>
</svg>"""
    },

    # 6. 宽握高位下拉
    "lat_pulldown": {
        "title": "宽握高位下拉 (Lat Pulldown)",
        "equipment": "高位下拉机 / 长横杆",
        "target": "背阔肌上外侧、大圆肌",
        "volleyballFocus": "安全积累背部容量，增强扣球挥臂终末段的减速制动肌力",
        "breathing": "横杆下拉到锁骨时呼气收紧，手臂随横杆缓缓回放时充分吸气。",
        "steps": [
            "调节大腿挡板紧贴大腿上方固定下肢，双手宽握抓横杆外弯处。",
            "挺胸直立，身体微后倾约 10°-15°，沉肩挺胸，手臂完全伸直悬挂启动。",
            "背阔肌发力，手肘向外向下沿弧线将横杆下拉至上胸锁骨位置。",
            "在底部感受背阔肌深度挤压夹紧，再用 2-3 秒匀速控制横杆升回起点。"
        ],
        "mistakes": [
            "身体过度后仰（变成水平划船），借用下背部和体重下坠拉动重量。",
            "将横杆拉至颈后，极度容易磨损肩关节盂唇和颈椎。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad6" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowVolt6"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowDown6" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,0 L3,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad6)"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <!-- 高位下拉机钢架 -->
  <line x1="160" y1="30" x2="160" y2="70" stroke="#f59e0b" stroke-width="3"/>
  <path d="M 90,70 L 230,70" stroke="#cbd5e1" stroke-width="5" stroke-linecap="round"/>
  <!-- 坐姿人物 (微后仰) -->
  <circle cx="160" cy="105" r="12" fill="#cbd5e1"/>
  <line x1="160" y1="117" x2="152" y2="170" stroke="#94a3b8" stroke-width="16" stroke-linecap="round"/>
  <!-- 背部发力高亮 -->
  <polygon points="144,120 130,140 152,160" fill="#00f59b" opacity="0.9" filter="url(#glowVolt6)"/>
  <!-- 大腿卡垫与座位 -->
  <rect x="135" y="165" width="40" height="10" rx="3" fill="#334155"/>
  <polyline points="152,168 180,172 185,205" fill="none" stroke="#64748b" stroke-width="6" stroke-linecap="round"/>
  <!-- 双臂下拉至锁骨 -->
  <polyline points="100,72 130,105 150,118" fill="none" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <polyline points="220,72 190,105 170,118" fill="none" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <!-- 下拉箭头 -->
  <line x1="160" y1="65" x2="160" y2="92" stroke="#00f59b" stroke-width="3" marker-end="url(#arrowDown6)"/>
  <text x="240" y="85" fill="#00f59b" font-size="11" font-weight="bold">沉肩下拉至锁骨</text>
  <text x="240" y="103" fill="#cbd5e1" font-size="10">手肘朝向侧下方压紧</text>
</svg>"""
    },

    # 7. 绳索面拉 (Face Pull)
    "cable_face_pull": {
        "title": "绳索面拉 (Face Pull)",
        "equipment": "龙门架高位绳索 / 三头肌绳",
        "target": "三角肌后束、肩袖冈下肌、菱形肌",
        "volleyballFocus": "【排球防伤第一神技】对抗频繁扣球带来的圆肩与肩峰撞击，保护肩关节长久健康",
        "breathing": "拉向面部并外旋展开时呼气挺胸，向前回放时吸气控制节奏。",
        "steps": [
            "将滑轮调至面部高度或略高，握住三头肌绳把手，大拇指指向后方。",
            "向后退两步拉紧绳索，双脚前后呈弓步站稳，挺胸微前倾。",
            "沉肩启动，向面部拉回绳索，终末段手肘向两侧拉开，大拇指朝后上方翻转外旋。",
            "让绳结靠近鼻尖或眼睛两侧，手腕处于高于手肘的姿态，顶峰停顿 1-2 秒后匀速回放。"
        ],
        "mistakes": [
            "盲目加大重量，导致头颈前探、身体后仰猛拉借力。",
            "末端未完成“外旋展开”（仅直上直下拉），失去对肩袖外旋肌群的锻炼价值。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad7" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowVolt7"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowRight7" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad7)"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <!-- 龙门架滑轮 (面部高度) -->
  <rect x="40" y="30" width="10" height="175" fill="#334155"/>
  <circle cx="45" cy="80" r="8" fill="#64748b"/>
  <!-- 站立人物 -->
  <circle cx="240" cy="85" r="12" fill="#cbd5e1"/>
  <line x1="238" y1="97" x2="230" y2="155" stroke="#94a3b8" stroke-width="16" stroke-linecap="round"/>
  <!-- 三角肌后束与上背高亮 -->
  <circle cx="230" cy="100" r="10" fill="#00f59b" opacity="0.9" filter="url(#glowVolt7)"/>
  <!-- 绳索与拉向眼睛外旋手臂 -->
  <line x1="53" y1="80" x2="215" y2="82" stroke="#f59e0b" stroke-width="2.5"/>
  <polyline points="230,100 205,80 218,65" fill="none" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <!-- 弓步下肢 -->
  <polyline points="230,155 210,180 205,205" fill="none" stroke="#64748b" stroke-width="6" stroke-linecap="round"/>
  <polyline points="230,155 255,185 265,205" fill="none" stroke="#64748b" stroke-width="6" stroke-linecap="round"/>
  <!-- 外旋展开箭头 -->
  <path d="M 205,85 Q 220,75 220,62" fill="none" stroke="#00f59b" stroke-width="2.5" marker-end="url(#arrowRight7)"/>
  <text x="250" y="55" fill="#00f59b" font-size="12" font-weight="bold">手腕翻转外旋</text>
  <text x="250" y="73" fill="#cbd5e1" font-size="10">大拇指朝后拉向眼睛</text>
  <text x="250" y="90" fill="#f59e0b" font-size="10">护肩防伤第一神技</text>
</svg>"""
    },

    # 8. 坐姿绳索划船
    "cable_seated_row": {
        "title": "坐姿绳索划船 (Seated Cable Row)",
        "equipment": "坐姿划船机 / V型窄握把手",
        "target": "中背菱形肌、中下斜方肌、竖脊肌",
        "volleyballFocus": "强化上背厚度与躯干直立耐力，扣球后落地维持躯干中立不弯腰",
        "breathing": "拉向腹部挺胸挤压时呼气，手臂回放拉伸背部时吸气。",
        "steps": [
            "双脚踩紧踏板，双膝微屈（切忌过度锁死膝盖），双手握紧V型把手。",
            "挺胸立腰，保持脊柱绝对中立，双肩自然下沉。",
            "手肘贴近身体两侧向后下方拉动把手，直至把手触及下腹肋弓处。",
            "有意识地向中间用力挤压紧闭两侧肩胛骨，停顿 1 秒后控制还原。"
        ],
        "mistakes": [
            "过度挺身甚至借后仰 45° 的身体摆动甩拉重物，严重损害腰椎 L4-L5。",
            "含胸圆背拉动，导致斜方肌上束耸起酸痛。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad8" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowVolt8"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowRow" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad8)"/>
  <line x1="20" y1="200" x2="380" y2="200" stroke="#1e293b" stroke-width="2"/>
  <!-- 滑轮与踏板 -->
  <rect x="50" y="100" width="12" height="100" fill="#334155"/>
  <circle cx="56" cy="140" r="7" fill="#64748b"/>
  <polygon points="120,130 130,130 115,165 105,165" fill="#475569"/>
  <!-- 坐姿滑轨板 -->
  <rect x="150" y="165" width="100" height="12" fill="#334155"/>
  <!-- 坐姿人物挺胸立腰 -->
  <circle cx="215" cy="100" r="12" fill="#cbd5e1"/>
  <line x1="213" y1="112" x2="205" y2="165" stroke="#94a3b8" stroke-width="16" stroke-linecap="round"/>
  <!-- 中背菱形肌高亮 -->
  <ellipse cx="205" cy="125" rx="10" ry="14" fill="#00f59b" opacity="0.9" filter="url(#glowVolt8)"/>
  <!-- 微屈双腿踩踏板 -->
  <polyline points="205,165 160,150 118,145" fill="none" stroke="#64748b" stroke-width="7" stroke-linecap="round"/>
  <!-- 绳索与手肘后拉 -->
  <line x1="63" y1="140" x2="185" y2="140" stroke="#f59e0b" stroke-width="2.5"/>
  <polyline points="208,118 190,140 180,140" fill="none" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <!-- 后拉箭头 -->
  <line x1="165" y1="130" x2="195" y2="130" stroke="#00f59b" stroke-width="3" marker-end="url(#arrowRow)"/>
  <text x="235" y="105" fill="#00f59b" font-size="11" font-weight="bold">后拉挤压肩胛骨</text>
  <text x="235" y="122" fill="#cbd5e1" font-size="10">挺胸立腰 · 脊柱中立不晃动</text>
</svg>"""
    },

    # 9. 站姿杠铃推举 (OHP)
    "overhead_press": {
        "title": "站姿杠铃推举 (Overhead Press)",
        "equipment": "杠铃 / 深蹲架",
        "target": "三角肌前中束、上胸、核心、肱三头肌",
        "volleyballFocus": "将地面反作用力经核心传导至肩部过顶伸展，增强空中拦网与扣球顶峰刚度",
        "breathing": "起杠深吸气绷紧腹横肌，推过头顶锁定后呼气。",
        "steps": [
            "双手握杠略宽于肩，将杠铃架在锁骨与三角肌前束上方，手肘处于杠铃正前方。",
            "双脚与肩同宽站立，收紧臀部大肌与核心腹肌，头部微后仰让出杠铃上升通道。",
            "发力将杠铃垂直向上推起，杠铃过头顶后头部自然回正微前移，在手臂完全伸直处锁定。",
            "匀速受控下放至锁骨上方初始位置。"
        ],
        "mistakes": [
            "核心松懈导致腰椎极度反弓（挺肚子借力），重压腰椎下段。",
            "握距过宽，使手肘在推起时外旋失稳。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad9" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowVolt9"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowUp9" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,6 L3,0 L6,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad9)"/>
  <line x1="20" y1="210" x2="380" y2="210" stroke="#1e293b" stroke-width="2"/>
  <!-- 站立挺拔人物 -->
  <circle cx="170" cy="70" r="12" fill="#cbd5e1"/>
  <line x1="170" y1="82" x2="170" y2="150" stroke="#94a3b8" stroke-width="16" stroke-linecap="round"/>
  <!-- 站立双腿绷紧 -->
  <line x1="164" y1="150" x2="160" y2="210" stroke="#64748b" stroke-width="7" stroke-linecap="round"/>
  <line x1="176" y1="150" x2="180" y2="210" stroke="#64748b" stroke-width="7" stroke-linecap="round"/>
  <!-- 三角肌过顶发力高亮 -->
  <ellipse cx="170" cy="88" rx="16" ry="8" fill="#00f59b" opacity="0.9" filter="url(#glowVolt9)"/>
  <!-- 双臂推举过顶 -->
  <polyline points="158,88 152,48 150,28" fill="none" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <polyline points="182,88 188,48 190,28" fill="none" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <!-- 杠铃杆与铃片 -->
  <line x1="90" y1="26" x2="250" y2="26" stroke="#cbd5e1" stroke-width="5"/>
  <rect x="95" y="10" width="8" height="32" rx="2" fill="#ef4444"/>
  <rect x="237" y="10" width="8" height="32" rx="2" fill="#ef4444"/>
  <!-- 上推箭头 -->
  <line x1="170" y1="65" x2="170" y2="38" stroke="#00f59b" stroke-width="3" marker-end="url(#arrowUp9)"/>
  <text x="210" y="55" fill="#00f59b" font-size="11" font-weight="bold">过顶垂直推举</text>
  <text x="210" y="73" fill="#cbd5e1" font-size="10">收紧腹臀 · 腰椎中立不反弓</text>
</svg>"""
    },

    # 10. 哑铃侧平举
    "db_lateral_raise": {
        "title": "哑铃侧平举 (Dumbbell Lateral Raise)",
        "equipment": "轻哑铃对",
        "target": "三角肌中束",
        "volleyballFocus": "打造饱满肩部侧向防撞装甲，增强挥臂侧向动作稳定性",
        "breathing": "侧平举起至水平时呼气，下放至体侧时吸气缓慢下沉。",
        "steps": [
            "双手各持轻哑铃，挺胸收腹，双脚与肩同宽站立，身体微前倾 5°。",
            "手肘保持微屈锁定，意念集中在手肘外侧向上抬起。",
            "将哑铃平稳向身体两侧举起，手肘与大臂抬至与地面水平平行位置。",
            "顶点停顿 1 秒强化中束充血，用 2 秒离心平缓下落。"
        ],
        "mistakes": [
            "耸起斜方肌将哑铃甩起，完全由颈背部代偿。",
            "手腕高于手肘（倒水动作幅度过大引起冈上肌挤压）。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad10" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowVolt10"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowArc" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,6 L3,0 L6,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad10)"/>
  <line x1="20" y1="210" x2="380" y2="210" stroke="#1e293b" stroke-width="2"/>
  <!-- 站立人物 -->
  <circle cx="200" cy="70" r="12" fill="#cbd5e1"/>
  <line x1="200" y1="82" x2="200" y2="150" stroke="#94a3b8" stroke-width="16" stroke-linecap="round"/>
  <line x1="194" y1="150" x2="190" y2="210" stroke="#64748b" stroke-width="6"/>
  <line x1="206" y1="150" x2="210" y2="210" stroke="#64748b" stroke-width="6"/>
  <!-- 三角肌中束高亮 -->
  <circle cx="184" cy="90" r="7" fill="#00f59b" opacity="0.9" filter="url(#glowVolt10)"/>
  <circle cx="216" cy="90" r="7" fill="#00f59b" opacity="0.9" filter="url(#glowVolt10)"/>
  <!-- 双臂侧平举平飞 -->
  <polyline points="184,90 135,95 100,105" fill="none" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <polyline points="216,90 265,95 300,105" fill="none" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <rect x="85" y="98" width="14" height="14" rx="2" fill="#f59e0b"/>
  <rect x="300" y="98" width="14" height="14" rx="2" fill="#f59e0b"/>
  <!-- 向上抬起弧线箭头 -->
  <path d="M 120,135 Q 110,115 105,110" fill="none" stroke="#00f59b" stroke-width="2" marker-end="url(#arrowArc)"/>
  <path d="M 280,135 Q 290,115 295,110" fill="none" stroke="#00f59b" stroke-width="2" marker-end="url(#arrowArc)"/>
  <text x="145" y="45" fill="#00f59b" font-size="11" font-weight="bold">手肘微屈 · 侧向平行举起</text>
  <text x="140" y="60" fill="#cbd5e1" font-size="10">大臂与地面水平 · 绝不耸肩</text>
</svg>"""
    },

    # 11. 绳索肩外旋 (肩袖专项)
    "cable_external_rotation": {
        "title": "绳索肩外旋 (Cable External Rotation)",
        "equipment": "龙门架低位绳索 / 弹力带",
        "target": "冈下肌、小圆肌 (肩袖关键刹车肌群)",
        "volleyballFocus": "【扣球刹车皮】频繁扣球内旋发力后，外旋肩袖必须提供足够的刹车力，否则撕裂",
        "breathing": "外展向外旋转时呼气，平稳向腹前内收时吸气。",
        "steps": [
            "将滑轮调至肘部高度，侧向面对龙门架，近侧臂或远侧臂屈肘90度。",
            "在肘关节与体侧之间可夹一块毛巾，确保手肘全程紧贴躯干不离开。",
            "以大臂为轴心，前臂平缓向外侧水平旋转 45°-60°。",
            "极轻重量（2.5-5kg），感受肩胛骨下方深层肌肉紧绷，慢速复位。"
        ],
        "mistakes": [
            "使用大重量，手肘离开身体侧面变成飞鸟或侧平举。",
            "快速甩动手腕，不仅无效果还会损伤腕关节。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad11" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowVolt11"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowOut11" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad11)"/>
  <line x1="20" y1="210" x2="380" y2="210" stroke="#1e293b" stroke-width="2"/>
  <!-- 龙门架滑轮 -->
  <rect x="40" y="50" width="10" height="155" fill="#334155"/>
  <circle cx="45" cy="120" r="7" fill="#64748b"/>
  <!-- 站立人物 -->
  <circle cx="180" cy="75" r="12" fill="#cbd5e1"/>
  <line x1="180" y1="87" x2="180" y2="155" stroke="#94a3b8" stroke-width="16" stroke-linecap="round"/>
  <!-- 肩袖冈下肌高亮 -->
  <ellipse cx="174" cy="98" rx="8" ry="12" fill="#00f59b" opacity="0.9" filter="url(#glowVolt11)"/>
  <!-- 肘部紧贴夹毛巾 -->
  <rect x="187" y="112" width="6" height="14" fill="#38bdf8"/>
  <line x1="52" y1="120" x2="190" y2="120" stroke="#f59e0b" stroke-width="2.5"/>
  <!-- 前臂向外旋转轨迹 -->
  <polyline points="188,95 190,120 235,120" fill="none" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <line x1="180" y1="155" x2="175" y2="210" stroke="#64748b" stroke-width="6"/>
  <line x1="180" y1="155" x2="188" y2="210" stroke="#64748b" stroke-width="6"/>
  <!-- 外旋弧线箭头 -->
  <path d="M 210,132 Q 230,130 240,122" fill="none" stroke="#00f59b" stroke-width="2.5" marker-end="url(#arrowOut11)"/>
  <text x="220" y="85" fill="#00f59b" font-size="12" font-weight="bold">手肘夹紧 · 水平外旋</text>
  <text x="220" y="103" fill="#cbd5e1" font-size="10">极轻重量 2.5-5kg · 激活肩袖</text>
  <text x="220" y="145" fill="#38bdf8" font-size="10">夹毛巾固定肘关节</text>
</svg>"""
    },

    # 12. 弹力带 Y-T-W-L 激活
    "band_ytwl": {
        "title": "弹力带 Y-T-W-L 肩关节激活",
        "equipment": "轻阻力圈 / 小弹力带",
        "target": "下斜方肌、菱形肌、肩袖整体",
        "volleyballFocus": "排球比赛或力量训练前的极佳肩关节唤醒热身，消除弹响",
        "breathing": "每个字母展开定型时呼气挺胸，收拢时平缓吸气。",
        "steps": [
            "双手套上轻弹力带，站姿微收核心挺胸。",
            "【Y字】：双手伸直向上举至135度夹角，拇指朝后挺起唤醒下斜方肌。",
            "【T字】：水平展开双臂向两侧拉开呈一条直线，挤压肩胛骨。",
            "【W字】：屈肘收至肋侧后拉，小臂与大臂呈W形强化中背。",
            "【L字】：肘部贴侧呈90度，前臂向外翻转做出最大外旋。"
        ],
        "mistakes": [
            "使用太硬的大弹力带导致颈椎代偿耸肩。",
            "动作过快甩动，没有在每个字母顶点停顿 1 秒。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad12" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad12)"/>
  <!-- 四格展示 Y T W L -->
  <rect x="25" y="30" width="75" height="175" rx="8" fill="#1e293b" opacity="0.6"/>
  <rect x="115" y="30" width="75" height="175" rx="8" fill="#1e293b" opacity="0.6"/>
  <rect x="205" y="30" width="75" height="175" rx="8" fill="#1e293b" opacity="0.6"/>
  <rect x="295" y="30" width="75" height="175" rx="8" fill="#1e293b" opacity="0.6"/>
  <!-- Y -->
  <text x="52" y="55" fill="#00f59b" font-size="16" font-weight="black">Y</text>
  <circle cx="62" cy="85" r="7" fill="#cbd5e1"/>
  <polyline points="45,70 62,95 80,70" fill="none" stroke="#00f59b" stroke-width="4" stroke-linecap="round"/>
  <line x1="62" y1="95" x2="62" y2="150" stroke="#94a3b8" stroke-width="8"/>
  <text x="35" y="180" fill="#94a3b8" font-size="9">下斜方肌</text>
  <!-- T -->
  <text x="142" y="55" fill="#38bdf8" font-size="16" font-weight="black">T</text>
  <circle cx="152" cy="85" r="7" fill="#cbd5e1"/>
  <line x1="125" y1="95" x2="180" y2="95" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>
  <line x1="152" y1="95" x2="152" y2="150" stroke="#94a3b8" stroke-width="8"/>
  <text x="127" y="180" fill="#94a3b8" font-size="9">菱形肌后收</text>
  <!-- W -->
  <text x="230" y="55" fill="#f59e0b" font-size="16" font-weight="black">W</text>
  <circle cx="242" cy="85" r="7" fill="#cbd5e1"/>
  <polyline points="225,85 235,105 242,98 250,105 260,85" fill="none" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
  <line x1="242" y1="98" x2="242" y2="150" stroke="#94a3b8" stroke-width="8"/>
  <text x="217" y="180" fill="#94a3b8" font-size="9">屈肘后夹</text>
  <!-- L -->
  <text x="323" y="55" fill="#ef4444" font-size="16" font-weight="black">L</text>
  <circle cx="332" cy="85" r="7" fill="#cbd5e1"/>
  <polyline points="315,90 325,105 340,105 350,90" fill="none" stroke="#ef4444" stroke-width="4" stroke-linecap="round"/>
  <line x1="332" y1="98" x2="332" y2="150" stroke="#94a3b8" stroke-width="8"/>
  <text x="312" y="180" fill="#94a3b8" font-size="9">肩外旋</text>
</svg>"""
    },

    # 13. 杠铃深蹲
    "barbell_squat": {
        "title": "杠铃深蹲 (Barbell Back Squat)",
        "equipment": "杠铃 / 深蹲架",
        "target": "股四头肌、臀大肌、内收肌、核心刚度",
        "volleyballFocus": "【弹跳第一基石】深蹲力量与垂直纵跳极限高度高度正相关，筑牢发力下盘",
        "breathing": "下蹲前深吸气瓦式呼吸憋气闭气锁死核心，起立过半后呼气。",
        "steps": [
            "杠铃稳妥置于上斜方肌（高杠位）或肩胛骨棘上（低杠位），双脚与肩同宽微外展。",
            "深吸气腹肌鼓起锁死核心，屈髋向后推臀同时屈膝平稳下蹲。",
            "膝盖指向脚尖方向，下蹲至大腿与地面平行或略低于水平面。",
            "脚跟与前脚掌三点蹬地，臀大肌与股四头肌强力伸髋伸膝站起。"
        ],
        "mistakes": [
            "下蹲过程中膝盖向内扣（Knee Valgus），极度容易撕裂前交叉韧带或髌腱受压。",
            "骨盆后倾“眨眼”（Butt Wink），导致腰椎在最深处代偿承重。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad13" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowVolt13"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowUp13" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,6 L3,0 L6,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad13)"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <!-- 深蹲深处姿态 -->
  <circle cx="160" cy="95" r="12" fill="#cbd5e1"/>
  <line x1="160" y1="107" x2="140" y2="145" stroke="#94a3b8" stroke-width="16" stroke-linecap="round"/>
  <!-- 大腿股四头肌与臀大肌高亮 -->
  <line x1="140" y1="145" x2="190" y2="148" stroke="#00f59b" stroke-width="14" stroke-linecap="round" filter="url(#glowVolt13)"/>
  <!-- 小腿脚踝 -->
  <line x1="190" y1="148" x2="185" y2="205" stroke="#64748b" stroke-width="7" stroke-linecap="round"/>
  <!-- 背负杠铃杆 -->
  <line x1="120" y1="98" x2="200" y2="98" stroke="#cbd5e1" stroke-width="6"/>
  <circle cx="130" cy="98" r="14" fill="#ef4444"/>
  <circle cx="190" cy="98" r="14" fill="#ef4444"/>
  <!-- 蹬伸向上箭头 -->
  <line x1="155" y1="175" x2="155" y2="115" stroke="#00f59b" stroke-width="3.5" marker-end="url(#arrowUp13)"/>
  <text x="215" y="95" fill="#00f59b" font-size="12" font-weight="black">蹬地爆发伸髋</text>
  <text x="215" y="115" fill="#cbd5e1" font-size="10">大腿与地面平行</text>
  <text x="215" y="132" fill="#f59e0b" font-size="10">膝盖坚决不内扣</text>
</svg>"""
    },

    # 14. 罗马尼亚硬拉 (RDL)
    "romanian_deadlift": {
        "title": "罗马尼亚硬拉 (Romanian Deadlift)",
        "equipment": "杠铃 / 哑铃",
        "target": "腘绳肌、臀大肌、竖脊肌 (后侧动力链)",
        "volleyballFocus": "【蓄力屈髋弹簧】排球起跳前的两步助跑最后蓄力完全依赖后侧链拉伸蓄能",
        "breathing": "屈髋下放时吸气绷紧后链，推髋起立时呼气夹紧臀部。",
        "steps": [
            "双手抓握杠铃立正站直，双脚与髋同宽，双膝微屈固定（全程锁死膝角不再变动）。",
            "主动将臀部向后方远端推去，上身自然前倾折叠髋关节。",
            "杠铃杆紧贴大腿前侧滑落至膝盖下方小腿中部，充分感受腘绳肌被紧绷拉长。",
            "臀部发力向前顶髋，将身体拉直站立，在顶端收紧臀肌。"
        ],
        "mistakes": [
            "把 RDL 做成深蹲（膝盖过度前屈下弯）。",
            "圆背弯腰去抓杠铃，对腰椎间盘造成剪切力。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad14" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowVolt14"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowHip" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad14)"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <!-- 屈髋折叠人物姿态 -->
  <circle cx="120" cy="110" r="12" fill="#cbd5e1"/>
  <line x1="130" y1="115" x2="205" y2="135" stroke="#94a3b8" stroke-width="15" stroke-linecap="round"/>
  <!-- 紧绷拉长的腘绳肌与臀肌高亮 -->
  <line x1="205" y1="135" x2="200" y2="175" stroke="#00f59b" stroke-width="12" stroke-linecap="round" filter="url(#glowVolt14)"/>
  <line x1="200" y1="175" x2="195" y2="205" stroke="#64748b" stroke-width="7" stroke-linecap="round"/>
  <!-- 双臂垂直贴腿下垂 -->
  <line x1="145" y1="120" x2="175" y2="165" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <!-- 杠铃杆贴小腿 -->
  <circle cx="175" cy="165" r="10" fill="#ef4444"/>
  <!-- 向后推臀箭头 -->
  <line x1="180" y1="125" x2="225" y2="125" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrowHip)"/>
  <text x="235" y="125" fill="#f59e0b" font-size="11" font-weight="bold">臀部主动向后推</text>
  <text x="210" y="160" fill="#00f59b" font-size="11" font-weight="bold">腘绳肌紧绷拉伸</text>
  <text x="210" y="178" fill="#cbd5e1" font-size="10">微屈膝锁定 · 杠铃贴腿下放</text>
</svg>"""
    },

    # 15. 保加利亚分腿蹲
    "bulgarian_split_squat": {
        "title": "保加利亚分腿蹲 (Bulgarian Split Squat)",
        "equipment": "哑铃 / 平板卧推凳",
        "target": "前腿股四头肌、臀大肌、臀中肌 (单侧力量与平衡)",
        "volleyballFocus": "消除排球单双侧起跳失衡，强化落地单腿制动稳定性，防止膝盖晃动",
        "breathing": "垂直下沉时吸气收腹，前脚掌蹬伸回正时呼气发力。",
        "steps": [
            "背对卧推凳约两步距离，将后脚脚背自然搭在凳面边缘。",
            "前脚踩实地面，躯干保持微前倾（约15度更有利于臀部发力），双手各持哑铃。",
            "重心落在前脚脚后跟，控制身体垂直下蹲，直到前腿大腿平行地面。",
            "前腿脚后跟主动踩地发力推起身体，后腿仅作辅助平衡不可过度借力。"
        ],
        "mistakes": [
            "前脚站距过短，导致下蹲时膝盖严重过度超前且脚跟离地。",
            "前腿膝盖在发力时向内扣摆动。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad15" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowVolt15"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowUp15" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,6 L3,0 L6,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad15)"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <!-- 后脚卧推凳 -->
  <rect x="270" y="150" width="55" height="15" rx="3" fill="#334155"/>
  <rect x="290" y="165" width="10" height="40" fill="#1e293b"/>
  <!-- 人物下沉单腿深蹲 -->
  <circle cx="160" cy="85" r="12" fill="#cbd5e1"/>
  <line x1="160" y1="97" x2="160" y2="150" stroke="#94a3b8" stroke-width="15" stroke-linecap="round"/>
  <!-- 前腿臀腿高亮 -->
  <polyline points="160,150 135,160 135,205" fill="none" stroke="#00f59b" stroke-width="12" stroke-linecap="round" filter="url(#glowVolt15)"/>
  <!-- 后腿搭凳 -->
  <polyline points="160,150 220,175 275,150" fill="none" stroke="#64748b" stroke-width="7" stroke-linecap="round"/>
  <!-- 手持哑铃 -->
  <line x1="155" y1="105" x2="155" y2="155" stroke="#e2e8f0" stroke-width="4"/>
  <rect x="148" y="150" width="14" height="12" rx="2" fill="#f59e0b"/>
  <!-- 垂直蹬伸箭头 -->
  <line x1="110" y1="175" x2="110" y2="135" stroke="#00f59b" stroke-width="3" marker-end="url(#arrowUp15)"/>
  <text x="75" y="125" fill="#00f59b" font-size="11" font-weight="bold">前脚掌踩地蹬伸</text>
  <text x="210" y="120" fill="#cbd5e1" font-size="10">后腿自然搭凳平衡</text>
  <text x="210" y="138" fill="#f59e0b" font-size="10">消除双腿起跳力量失衡</text>
</svg>"""
    },

    # 16. 提踵力量训练
    "standing_calf_raise": {
        "title": "站姿提踵 (Standing Calf Raise)",
        "equipment": "稳固台阶 / 哑铃 / 史密斯机",
        "target": "腓肠肌、比目鱼肌、跟腱复合体",
        "volleyballFocus": "起跳脱离地面的终末一蹬，输出最后 15-20% 的垂直加速度",
        "breathing": "前脚掌全力蹬起提踵时呼气，脚跟下沉拉伸时吸气。",
        "steps": [
            "前脚掌踩在台阶边缘，脚跟悬空露在外面，手扶支架保持平衡。",
            "缓慢完全下沉脚跟，降到最低点感受跟腱与小腿后侧的极限拉伸 1 秒。",
            "小腿三头肌全力爆发收缩，以前脚掌为轴将脚后跟高高提起至最高点。",
            "在顶点顶峰收缩 1-2 秒，充分让跟腱处于高张力状态。"
        ],
        "mistakes": [
            "快速上下“弹簧抖动”，靠阿基里斯腱的被动回弹而非肌肉主动向心发力。",
            "膝盖大幅前后晃动借力。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad16" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowVolt16"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowUp16" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,6 L3,0 L6,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad16)"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <!-- 台阶踏板 -->
  <rect x="80" y="175" width="80" height="30" fill="#334155" stroke="#475569" stroke-width="2"/>
  <!-- 站立提踵人物 -->
  <circle cx="150" cy="55" r="12" fill="#cbd5e1"/>
  <line x1="150" y1="67" x2="150" y2="125" stroke="#94a3b8" stroke-width="14" stroke-linecap="round"/>
  <line x1="150" y1="125" x2="148" y2="150" stroke="#64748b" stroke-width="8"/>
  <!-- 小腿腓肠肌与跟腱高亮 -->
  <ellipse cx="145" cy="155" rx="8" ry="14" fill="#00f59b" opacity="0.9" filter="url(#glowVolt16)"/>
  <!-- 极度提起的脚跟 -->
  <line x1="145" y1="165" x2="135" y2="175" stroke="#00f59b" stroke-width="6"/>
  <polyline points="135,175 120,175" stroke="#ffffff" stroke-width="6" stroke-linecap="round"/>
  <!-- 抬起箭头 -->
  <line x1="110" y1="185" x2="110" y2="150" stroke="#00f59b" stroke-width="3" marker-end="url(#arrowUp16)"/>
  <text x="180" y="85" fill="#00f59b" font-size="12" font-weight="bold">前脚掌全力踮起</text>
  <text x="180" y="105" fill="#cbd5e1" font-size="10">脚跟悬空 · 顶峰停顿 1 秒</text>
  <text x="180" y="125" fill="#f59e0b" font-size="10">起跳离地终末加速</text>
</svg>"""
    },

    # 17. 胫骨前肌抬脚尖 (Tibialis Raise)
    "tibialis_raise": {
        "title": "胫骨前肌抬脚尖 (Tibialis Raise)",
        "equipment": "靠墙自重 / 平整地面",
        "target": "胫骨前肌 (小腿骨前侧刹车肌)",
        "volleyballFocus": "【防跳跃膝秘密武器】排球落地第一道刹车吸震器，强化它可有效缓解髌腱炎痛感",
        "breathing": "勾脚尖时呼气收紧，下落脚掌着地时吸气平缓。",
        "steps": [
            "背靠墙站立，双脚向前跨出约半米至大半米（距离越远难度越高）。",
            "双腿伸直微锁，以脚后跟为轴心支撑地面。",
            "全力收缩小腿前侧肌肉，将脚尖向上拉起，尽量靠近小腿骨。",
            "在最高点维持 1-2 秒，感到小腿前侧明显酸胀，然后缓慢放下。"
        ],
        "mistakes": [
            "依靠臀部翘起晃动借力，降低对胫骨前肌的孤立刺激。",
            "脚掌下落时直接拍地松懈，没有保持离心控制。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad17" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowVolt17"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowToe" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,6 L3,0 L6,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad17)"/>
  <!-- 靠墙立面与地面 -->
  <line x1="120" y1="30" x2="120" y2="205" stroke="#475569" stroke-width="8"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <!-- 靠墙站立人物 (斜向前跨步) -->
  <circle cx="140" cy="75" r="12" fill="#cbd5e1"/>
  <line x1="130" y1="87" x2="155" y2="145" stroke="#94a3b8" stroke-width="15" stroke-linecap="round"/>
  <!-- 胫骨前肌高亮 (小腿前侧) -->
  <line x1="155" y1="145" x2="190" y2="202" stroke="#64748b" stroke-width="8" stroke-linecap="round"/>
  <line x1="155" y1="150" x2="182" y2="195" stroke="#00f59b" stroke-width="6" filter="url(#glowVolt17)"/>
  <!-- 强力勾起的脚尖 -->
  <polyline points="190,202 185,178 170,172" fill="none" stroke="#ffffff" stroke-width="6" stroke-linecap="round"/>
  <!-- 勾脚尖箭头 -->
  <path d="M 215,200 Q 215,180 195,172" fill="none" stroke="#00f59b" stroke-width="3" marker-end="url(#arrowToe)"/>
  <text x="220" y="85" fill="#00f59b" font-size="12" font-weight="bold">脚跟着地 · 全力勾起脚尖</text>
  <text x="220" y="105" fill="#cbd5e1" font-size="10">小腿前侧极度酸胀</text>
  <text x="220" y="125" fill="#ef4444" font-size="10">【排球吸震护膝第一肌】</text>
</svg>"""
    },

    # 18. 龙门架高位斜向伐木 (Cable Woodchopper)
    "cable_woodchopper_high_low": {
        "title": "龙门架高位斜向伐木 (High-to-Low Woodchopper)",
        "equipment": "龙门架高位单滑轮 / D型手柄",
        "target": "腹内外斜肌、转髋动力链、前侧核心爆发力",
        "volleyballFocus": "【扣球发力动作孪生版】空中拉弓到收腹暴击的斜向转体鞭打动能重现",
        "breathing": "起势高位吸气蓄势，斜向下砍转体瞬间爆发有力呼气。",
        "steps": [
            "将滑轮调至最高位，侧对龙门架站立，双脚宽于肩宽，双手握紧手柄置于斜上方上方。",
            "后脚脚掌蹬地，转动后侧髋关节带动躯干旋转，如同排球空中转体挥臂。",
            "核心强力斜向下绞转，将手柄沿斜对角线砍向对侧膝盖外侧。",
            "在最低点腹斜肌全力紧闭收缩，随后有控制地抵抗阻力回放至高位。"
        ],
        "mistakes": [
            "纯用手臂去拉绳索，髋部和核心几乎没旋转动能。",
            "弯曲腰椎去弓背，导致旋转剪切力施加在腰椎上而非髋胸段。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad18" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowOrange18"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowSlash" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#f97316"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad18)"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <!-- 龙门架高位滑轮 -->
  <rect x="40" y="30" width="10" height="175" fill="#334155"/>
  <circle cx="45" cy="45" r="8" fill="#64748b"/>
  <!-- 侧身斜砍人物 -->
  <circle cx="210" cy="70" r="12" fill="#cbd5e1"/>
  <line x1="208" y1="82" x2="200" y2="140" stroke="#94a3b8" stroke-width="16" stroke-linecap="round"/>
  <!-- 腹内外斜肌旋转核心高亮 (排球专属橙) -->
  <ellipse cx="202" cy="115" rx="14" ry="12" fill="#f97316" opacity="0.9" filter="url(#glowOrange18)"/>
  <!-- 双腿转髋步态 -->
  <polyline points="200,140 180,175 170,205" fill="none" stroke="#64748b" stroke-width="6"/>
  <polyline points="200,140 230,175 240,205" fill="none" stroke="#64748b" stroke-width="6"/>
  <!-- 绳索从高处斜切到对侧膝 -->
  <line x1="53" y1="45" x2="160" y2="145" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="4,2"/>
  <polyline points="205,95 180,125 160,145" fill="none" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <!-- 暴扣斜砍轨迹箭头 -->
  <path d="M 120,70 Q 150,110 170,160" fill="none" stroke="#f97316" stroke-width="3" marker-end="url(#arrowSlash)"/>
  <text x="235" y="65" fill="#f97316" font-size="12" font-weight="black">高位斜向斩杀</text>
  <text x="235" y="85" fill="#cbd5e1" font-size="10">后脚转髋蹬地 · 扣球动能孪生</text>
  <text x="235" y="105" fill="#00f59b" font-size="10">打造空中转体抽鞭发力感</text>
</svg>"""
    },

    # 19. 帕洛夫抗旋转推举 (Pallof Press)
    "pallof_press": {
        "title": "帕洛夫抗旋转推举 (Pallof Press)",
        "equipment": "龙门架中位绳索 / 弹力带",
        "target": "腹横肌、深层横突肌、抗旋转稳定链",
        "volleyballFocus": "空中受到对抗阻力时维持躯干绝对刚度，防止身体被撞变形击球丢失准星",
        "breathing": "双手推向前方停顿抗旋转时呼气闭气固化躯干，收回胸前时吸气。",
        "steps": [
            "将滑轮调至胸部中位，侧向龙门架两米处站稳，双脚与肩同宽站立，微屈髋膝下沉重心。",
            "双手合握把手置于胸骨正前方，抵抗绳索横向要将你身体扭向龙门架的旋转力。",
            "保持躯干、骨盆和肩膀绝对朝向正前方，双手缓慢将把手推至手臂完全伸直。",
            "在最远端（力矩最大处）静止对抗锁定 2-3 秒，平稳收回胸前。"
        ],
        "mistakes": [
            "身体被拉力带跑发生扭转或倾斜。",
            "肩膀过度前耸耸肩代偿。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad20" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowVolt20"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowPress" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad20)"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <!-- 龙门架中位滑轮 -->
  <rect x="40" y="40" width="10" height="165" fill="#334155"/>
  <circle cx="45" cy="115" r="7" fill="#64748b"/>
  <!-- 侧向站立人物 -->
  <circle cx="210" cy="70" r="12" fill="#cbd5e1"/>
  <line x1="210" y1="82" x2="210" y2="145" stroke="#94a3b8" stroke-width="16" stroke-linecap="round"/>
  <!-- 核心抗旋转圆筒高亮 -->
  <rect x="198" y="105" width="24" height="32" rx="6" fill="#00f59b" opacity="0.9" filter="url(#glowVolt20)"/>
  <!-- 侧向拉力横向绳索 -->
  <line x1="52" y1="115" x2="245" y2="115" stroke="#f59e0b" stroke-width="2.5"/>
  <!-- 双手前推手臂 -->
  <polyline points="208,98 225,115 255,115" fill="none" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <!-- 下肢微屈扎马步 -->
  <line x1="204" y1="145" x2="195" y2="205" stroke="#64748b" stroke-width="6"/>
  <line x1="216" y1="145" x2="225" y2="205" stroke="#64748b" stroke-width="6"/>
  <!-- 推出锁定箭头 -->
  <line x1="220" y1="102" x2="260" y2="102" stroke="#00f59b" stroke-width="3" marker-end="url(#arrowPress)"/>
  <text x="240" y="65" fill="#00f59b" font-size="12" font-weight="black">平推静止停顿 2 秒</text>
  <text x="240" y="85" fill="#cbd5e1" font-size="10">抵抗横向旋转拉力</text>
  <text x="240" y="145" fill="#f59e0b" font-size="10">打造空中绝对躯干刚度</text>
</svg>"""
    },

    # 20. 踝关节弹性小跳 (Pogo Hops)
    "pogo_hops": {
        "title": "踝关节弹性小跳 (Pogo Hops)",
        "equipment": "自重 / 平整硬地",
        "target": "跟腱刚度 (Achilles Tendon Stiffness)、腓肠肌、足底筋膜",
        "volleyballFocus": "【跟腱弹簧化】缩短起跳触地时间（GCT），将跟腱变成高弹性弹簧，提升排球二次起跳反应",
        "breathing": "保持短促平稳的有节奏呼吸，核心微收紧不憋气。",
        "steps": [
            "双脚与髋同宽站立，双手叉腰或自然放在身侧。",
            "【锁膝法则】：膝盖微屈但锁死该角度，坚决不进行深蹲蓄力！",
            "仅依靠脚踝屈伸和前脚掌快速蹬地弹跳，像跳跳杆一样快速上下弹动。",
            "触地瞬间脚跟保持悬空不完全砸地，触地时间越短越好（如火烧脚底），连续弹性起跳。"
        ],
        "mistakes": [
            "每一跳都弯曲膝盖蹲下去（变成了小深蹲跳，失去了训练跟腱刚度的目的）。",
            "全脚掌平拍甚至脚后跟重重砸地，震伤腰部和膝盖。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad23" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowVolt23"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowUp23" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,6 L3,0 L6,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad23)"/>
  <line x1="20" y1="200" x2="380" y2="200" stroke="#1e293b" stroke-width="2"/>
  <!-- 悬空弹性起跳人物 -->
  <circle cx="170" cy="55" r="12" fill="#cbd5e1"/>
  <line x1="170" y1="67" x2="170" y2="125" stroke="#94a3b8" stroke-width="15" stroke-linecap="round"/>
  <!-- 膝盖微屈锁定直腿 -->
  <line x1="166" y1="125" x2="164" y2="165" stroke="#64748b" stroke-width="7"/>
  <line x1="174" y1="125" x2="176" y2="165" stroke="#64748b" stroke-width="7"/>
  <!-- 跟腱高弹性光环 -->
  <ellipse cx="170" cy="175" rx="10" ry="14" fill="#00f59b" opacity="0.9" filter="url(#glowVolt23)"/>
  <!-- 绷直下压的前脚掌 (离地) -->
  <polyline points="164,165 160,185" stroke="#ffffff" stroke-width="6" stroke-linecap="round"/>
  <polyline points="176,165 180,185" stroke="#ffffff" stroke-width="6" stroke-linecap="round"/>
  <!-- 弹簧图腾与反弹波纹 -->
  <path d="M 170,187 L 165,191 L 175,195 L 165,199 L 170,203" fill="none" stroke="#f59e0b" stroke-width="2.5"/>
  <!-- 快速反弹箭头 -->
  <line x1="130" y1="180" x2="130" y2="120" stroke="#00f59b" stroke-width="3" marker-end="url(#arrowUp23)"/>
  <text x="210" y="75" fill="#00f59b" font-size="12" font-weight="black">跟腱弹簧化 (Stiffness)</text>
  <text x="210" y="95" fill="#cbd5e1" font-size="10">微屈膝锁定 · 触地时间越短越好</text>
  <text x="210" y="115" fill="#38bdf8" font-size="10">前脚掌弹性小跳 (火烧脚底感)</text>
</svg>"""
    },

    # 21. 哑铃轻负重深蹲跳
    "db_jump_squat": {
        "title": "哑铃轻负重深蹲跳 (DB Jump Squat)",
        "equipment": "轻哑铃一对 (3-8kg)",
        "target": "下肢三关节快速伸展爆发力 (RFD 力量转化)",
        "volleyballFocus": "在 20% 1RM 黄金功率输出区间释放峰值爆发力，全面提升摸高极限",
        "breathing": "下蹲吸气蓄力，起跳瞬间爆发强力呼气。",
        "steps": [
            "双手各持轻哑铃置于体侧，站姿双脚略宽于肩，脚尖微外展。",
            "快速半蹲下沉蓄力（不可蹲太深，约 1/4 到 1/2 浅蹲即可模拟排球起跳准备姿态）。",
            "脚跟与前掌瞬间蹬地，三关节（髋、膝、踝）同时爆发性快速完全伸展！",
            "全力跃至最高空，落地时屈髋屈膝缓冲吸收冲击力，保持轻柔落地。"
        ],
        "mistakes": [
            "拿过重的哑铃导致起跳速度变慢（重量过大变成抗阻耐力，丧失爆发力特性）。",
            "落地直腿砸地，冲击膝盖半月板。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad24" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowVolt24"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowUp24" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,6 L3,0 L6,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad24)"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <!-- 起跳凌空姿态人物 -->
  <circle cx="160" cy="45" r="12" fill="#cbd5e1"/>
  <line x1="160" y1="57" x2="160" y2="105" stroke="#94a3b8" stroke-width="15" stroke-linecap="round"/>
  <!-- 伸髋伸膝伸踝 三关节爆发高亮 -->
  <line x1="156" y1="105" x2="152" y2="150" stroke="#00f59b" stroke-width="12" stroke-linecap="round" filter="url(#glowVolt24)"/>
  <line x1="152" y1="150" x2="150" y2="175" stroke="#00f59b" stroke-width="7" stroke-linecap="round"/>
  <!-- 手持轻哑铃 -->
  <rect x="135" y="100" width="10" height="18" rx="2" fill="#f59e0b"/>
  <rect x="175" y="100" width="10" height="18" rx="2" fill="#f59e0b"/>
  <!-- 爆发腾空箭头 -->
  <line x1="100" y1="185" x2="100" y2="90" stroke="#00f59b" stroke-width="4" marker-end="url(#arrowUp24)"/>
  <text x="210" y="65" fill="#00f59b" font-size="12" font-weight="black">三关节快速暴发伸展</text>
  <text x="210" y="85" fill="#cbd5e1" font-size="10">20% 1RM 黄金最大功率输出</text>
  <text x="210" y="105" fill="#f59e0b" font-size="10">轻哑铃快速半蹲 · 瞬间全力跃起</text>
</svg>"""
    },

    # 22. 跳箱稳固跳跃 + 柔和落地
    "box_jump_soft_landing": {
        "title": "稳固跳箱跳跃 + 柔和落地 (Box Jump)",
        "equipment": "稳固跳箱 / 踏板 (40-60cm)",
        "target": "下肢垂直爆发力、离心吸震缓冲控制",
        "volleyballFocus": "跳上高处大幅消除落地的地面对膝盖关节的冲击力，是排球摸高安全训练首选",
        "breathing": "起跳前深吸气摆臂，落地稳固吸震后呼气站直。",
        "steps": [
            "站在跳箱前一步距离，双脚与肩同宽站稳，双臂后摆俯身蓄力。",
            "双臂强力向上摆臂引体，脚掌蹬地爆发跃向跳箱表面。",
            "【柔和落地法则】：双脚全脚掌稳固踩上箱面，顺势屈髋屈膝像猫一样无声吸收冲击力。",
            "站直完成一跳后，从跳箱侧面【走下来】，切不可从高箱上直接跳下！"
        ],
        "mistakes": [
            "双脚在箱面上重重拍响砸地（说明离心缓冲吸震能力不足）。",
            "跳下箱子造成膝盖巨大离心冲击。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad25" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <marker id="arrowArc25" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad25)"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <!-- 跳箱 -->
  <rect x="230" y="115" width="120" height="90" rx="5" fill="#1e293b" stroke="#475569" stroke-width="3"/>
  <text x="270" y="165" fill="#64748b" font-size="14" font-weight="bold">50 cm</text>
  <!-- 箱上轻柔深蹲缓冲落地人物 -->
  <circle cx="280" cy="55" r="12" fill="#cbd5e1"/>
  <line x1="280" y1="67" x2="275" y2="95" stroke="#94a3b8" stroke-width="14" stroke-linecap="round"/>
  <polyline points="275,95 295,105 285,115" fill="none" stroke="#00f59b" stroke-width="8" stroke-linecap="round"/>
  <!-- 起跳轨迹弧线 -->
  <path d="M 80,185 Q 160,20 270,110" fill="none" stroke="#00f59b" stroke-width="3" stroke-dasharray="5,3" marker-end="url(#arrowArc25)"/>
  <!-- 起跳位置脚印 -->
  <ellipse cx="80" cy="195" rx="14" ry="4" fill="#334155"/>
  <text x="45" y="145" fill="#f59e0b" font-size="11" font-weight="bold">摆臂蹬地跃起</text>
  <text x="200" y="35" fill="#00f59b" font-size="12" font-weight="black">像猫一样轻盈无声吸震</text>
</svg>"""
    },

    # 23. 健身房坡度爬坡跑步机
    "incline_treadmill": {
        "title": "跑步机坡度快走 (Incline Treadmill)",
        "equipment": "商用爬坡跑步机 (建议坡度 10%-15%)",
        "target": "后链肌群 (臀大肌、腘绳肌、小腿)、心肺有氧",
        "volleyballFocus": "【极佳低冲击有氧】完全避免了公路慢跑对跳跃膝盖的反复震荡，同时强化臀部后链发力",
        "breathing": "保持腹式深长呼吸，步伐节奏与呼吸节奏相配合（如两步一吸、两步一呼）。",
        "steps": [
            "将坡度调高至 10%-15%，时速设定为 3.8-4.5 km/h（以大步快走为主，严禁慢跑）。",
            "双手自然随步伐前后摆臂，尽量【不扶扶手】（扶手会使卡路里消耗虚标降低 25-30%）。",
            "挺胸收腹，身体与坡度自然垂直保持轻微前倾，严禁仰靠在跑步机上。",
            "每一步脚跟先着地后过渡到全脚掌，主动用臀部收紧向后方蹬伸。"
        ],
        "mistakes": [
            "双手死死抓住把手并身体后仰悬挂，完全抵消了坡度带来的重心抬升做功。",
            "在 12% 以上大坡度上强行慢跑，使脚踝和跟腱遭受过大拉扯压力。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad27" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowVolt27"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad27)"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <!-- 坡度 12% 跑步机面板与斜坡跑带 -->
  <line x1="60" y1="195" x2="260" y2="140" stroke="#f59e0b" stroke-width="10" stroke-linecap="round"/>
  <rect x="250" y="80" width="12" height="70" fill="#334155"/>
  <rect x="235" y="70" width="40" height="15" rx="3" fill="#64748b"/>
  <!-- 大步爬坡快走人物 -->
  <circle cx="160" cy="75" r="12" fill="#cbd5e1"/>
  <line x1="160" y1="87" x2="170" y2="135" stroke="#94a3b8" stroke-width="14" stroke-linecap="round"/>
  <!-- 臀大肌与后链大步蹬伸高亮 -->
  <polyline points="170,135 185,150 195,158" stroke="#00f59b" stroke-width="8" stroke-linecap="round" filter="url(#glowVolt27)"/>
  <polyline points="170,135 145,155 130,175" stroke="#64748b" stroke-width="7" stroke-linecap="round"/>
  <!-- 摆臂 -->
  <line x1="160" y1="95" x2="140" y2="115" stroke="#e2e8f0" stroke-width="4" stroke-linecap="round"/>
  <line x1="160" y1="95" x2="185" y2="105" stroke="#e2e8f0" stroke-width="4" stroke-linecap="round"/>
  <!-- 坡度角标注 -->
  <path d="M 120,195 A 30 30 0 0 1 140,175" fill="none" stroke="#f59e0b" stroke-width="2"/>
  <text x="145" y="195" fill="#f59e0b" font-size="11" font-weight="bold">坡度 12%</text>
  <text x="210" y="45" fill="#00f59b" font-size="12" font-weight="black">ACSM 专业级爬坡公式</text>
  <text x="210" y="65" fill="#cbd5e1" font-size="10">不扶把手 · 臀后链主导发力</text>
  <text x="210" y="85" fill="#38bdf8" font-size="10">零冲击护膝有氧</text>
</svg>"""
    },

    # 24. 排球高强度实战对抗
    "volleyball_competitive": {
        "title": "排球激烈对抗比赛 / 扣球实战",
        "equipment": "标准排球场 / 网口",
        "target": "网前扣杀、鱼跃救球、拦网争顶、全场折返",
        "volleyballFocus": "真刀真枪的实战体能消耗，高频起跳与爆发扣杀挥臂",
        "breathing": "起跳与挥击空中强力吐气，落地后迅速调整深呼吸。",
        "steps": [
            "助跑三步起跳（左右左或右左右），双臂充分后摆蓄能。",
            "网前双脚强力制动起跳，空中形成拉弓挺胸转体击球姿势。",
            "在最高点击球点快速前收腹转髋并挥打小臂击球后上方包球扣杀。",
            "双脚轻柔微屈落地吸震，立即回正重心进入防守准备。"
        ],
        "mistakes": [
            "扣球下网或冲网导致触网违例或踩线踩脚扭伤。",
            "单脚落地且膝盖内扣，承受巨大膝关节扭矩。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad29" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowVolt29"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <rect width="400" height="240" fill="url(#bgGrad29)"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <!-- 排球网 -->
  <line x1="270" y1="60" x2="270" y2="205" stroke="#ffffff" stroke-width="4"/>
  <rect x="268" y="70" width="4" height="60" fill="#f59e0b"/>
  <!-- 空中扣杀拉弓人物 -->
  <circle cx="180" cy="55" r="12" fill="#cbd5e1"/>
  <path d="M 175,67 Q 160,95 185,125" fill="none" stroke="#00f59b" stroke-width="14" stroke-linecap="round" filter="url(#glowVolt29)"/>
  <!-- 扣球挥臂击球 -->
  <polyline points="175,70 195,50 235,45" fill="none" stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>
  <!-- 辅助引臂 -->
  <line x1="175" y1="70" x2="210" y2="70" stroke="#94a3b8" stroke-width="4"/>
  <!-- 空中屈膝后折 -->
  <polyline points="185,125 170,150 155,145" fill="none" stroke="#64748b" stroke-width="6" stroke-linecap="round"/>
  <!-- 击中排球特效 -->
  <circle cx="245" cy="42" r="11" fill="#38bdf8" stroke="#f59e0b" stroke-width="2"/>
  <path d="M 245,35 Q 260,70 295,150" fill="none" stroke="#ef4444" stroke-width="3" stroke-dasharray="4,2"/>
  <text x="35" y="45" fill="#00f59b" font-size="12" font-weight="black">空中拉弓后弓扣杀</text>
  <text x="35" y="65" fill="#cbd5e1" font-size="10">背阔+转体核心鞭打</text>
  <text x="35" y="85" fill="#f59e0b" font-size="10">最高点击球包满球心</text>
</svg>"""
    },

    # 25. 靠墙静蹲 / 西班牙深蹲等长收缩
    "wall_sit_isometric": {
        "title": "靠墙静蹲/西班牙深蹲等长收缩 (Wall Sit Isometric)",
        "equipment": "垂直墙面 / 环状弹力带(西班牙深蹲)",
        "target": "股四头肌等长收缩、髌腱张力调控",
        "volleyballFocus": "【排球髌腱赛前镇痛金标准】45秒等长收缩触发中枢镇痛机制，赛前压制跳跃膝疼痛且零摩擦",
        "breathing": "保持匀速深沉的鼻吸口呼节奏，严禁憋气导致血压飙升。",
        "steps": [
            "背部、臀部与后脑勺紧贴垂直墙面站立，双脚向前迈出约一大步，与肩同宽。",
            "沿墙面缓缓滑下，直至大腿与地面接近平行（膝盖屈曲约 80°-90°），小腿尽量垂直地面。",
            "【护膝关键】：确保双膝正对第二脚趾方向，坚决不内扣，重心均匀压在全脚掌。",
            "保持该静态角度稳定 45 秒（感受股四头肌与髌腱微酸发暖但膝盖不尖锐刺痛）。"
        ],
        "mistakes": [
            "脚跟离地或膝盖大幅度前顶超过脚尖，增加髌股关节压力。",
            "膝盖向内夹紧（X型腿内扣）或双手撑在膝盖上借力偷懒。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgWall" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowWall"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <rect width="400" height="240" fill="url(#bgWall)"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <!-- 垂直墙面 -->
  <rect x="75" y="30" width="16" height="175" rx="2" fill="#334155"/>
  <line x1="91" y1="30" x2="91" y2="205" stroke="#475569" stroke-width="2"/>
  <!-- 靠墙静蹲人物：背部贴墙，大小腿呈90度 -->
  <circle cx="107" cy="65" r="12" fill="#cbd5e1"/>
  <line x1="103" y1="77" x2="103" y2="135" stroke="#94a3b8" stroke-width="15" stroke-linecap="round"/>
  <!-- 大腿水平高亮 (股四头肌等长发力) -->
  <line x1="103" y1="135" x2="168" y2="135" stroke="#00f59b" stroke-width="13" stroke-linecap="round" filter="url(#glowWall)"/>
  <!-- 小腿垂直地面 -->
  <line x1="168" y1="135" x2="168" y2="198" stroke="#64748b" stroke-width="9" stroke-linecap="round"/>
  <line x1="168" y1="198" x2="190" y2="202" stroke="#cbd5e1" stroke-width="7" stroke-linecap="round"/>
  <!-- 髌腱镇痛保护光环 -->
  <circle cx="171" cy="138" r="10" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="3,2"/>
  <!-- 90度直角标尺 -->
  <polyline points="154,135 154,149 168,149" fill="none" stroke="#f59e0b" stroke-width="2"/>
  <text x="132" y="162" fill="#f59e0b" font-size="10" font-weight="bold">80°-90°</text>
  <!-- 双臂前平举/贴体侧 -->
  <line x1="105" y1="92" x2="145" y2="115" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <!-- 标注 -->
  <text x="210" y="65" fill="#00f59b" font-size="12" font-weight="black">等长镇痛护膝 (45s)</text>
  <text x="210" y="85" fill="#cbd5e1" font-size="10">大小腿呈 90° · 零关节摩擦</text>
  <text x="210" y="105" fill="#38bdf8" font-size="10">背部紧贴墙面 · 重心踩实全掌</text>
  <text x="210" y="125" fill="#f59e0b" font-size="10">★ 排球赛前跳跃膝急救首选</text>
</svg>"""
    },

    # 26. 弹力带怪兽侧步走 (Monster Walk)
    "miniband_lateral_walk": {
        "title": "弹力带怪兽侧步走 (Miniband Lateral Walk)",
        "equipment": "环状迷你弹力带",
        "target": "臀中肌、臀小肌、髋外展稳定肌群",
        "volleyballFocus": "【锁死膝盖防内扣】强化髋外展刚度，防止助跑急停和单脚落地膝内扣扭伤韧带",
        "breathing": "保持均匀呼吸，每侧跨步时保持核心腹压稳定。",
        "steps": [
            "将迷你弹力带套在双膝上方约 5cm 处（或脚踝处加大难度），双脚与肩同宽。",
            "臀部微向后坐进入约 1/4 半蹲运动预备姿，抬头挺胸，核心收紧。",
            "向外侧主动迈出一脚（保持弹力带始终有拉紧张力），另一脚受控跟进半步而不完全并拢。",
            "向左侧横移 12 步后，再向右侧横移 12 步，全程保持双膝向外微顶撑开。"
        ],
        "mistakes": [
            "迈步时上身左右剧烈摇晃借力，失去了臀中肌的孤立抗阻刺激。",
            "跟随腿回收太快导致弹力带松弛失去张力，或膝盖随阻力向内塌陷。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgWalk" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowWalk"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowSide" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgWalk)"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <!-- 正面半蹲人物 -->
  <circle cx="160" cy="60" r="12" fill="#cbd5e1"/>
  <path d="M 145,74 L 175,74 L 178,125 L 142,125 Z" fill="#94a3b8"/>
  <!-- 双侧臀中肌高亮发光 -->
  <ellipse cx="138" cy="122" rx="10" ry="12" fill="#00f59b" opacity="0.9" filter="url(#glowWalk)"/>
  <ellipse cx="182" cy="122" rx="10" ry="12" fill="#00f59b" opacity="0.9" filter="url(#glowWalk)"/>
  <!-- 微屈大腿与向外跨步小腿 -->
  <polyline points="145,125 125,158 115,200" fill="none" stroke="#64748b" stroke-width="8" stroke-linecap="round"/>
  <polyline points="175,125 198,158 210,200" fill="none" stroke="#64748b" stroke-width="8" stroke-linecap="round"/>
  <!-- 膝盖上方橙色弹力带 -->
  <rect x="122" y="148" width="78" height="9" rx="4" fill="#f97316" stroke="#fed7aa" stroke-width="1"/>
  <!-- 侧向跨步动态箭头 -->
  <line x1="220" y1="185" x2="265" y2="185" stroke="#00f59b" stroke-width="3" marker-end="url(#arrowSide)"/>
  <line x1="100" y1="185" x2="65" y2="185" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="3,2"/>
  <!-- 手部叉腰稳定 -->
  <polyline points="145,82 130,105 142,118" fill="none" stroke="#e2e8f0" stroke-width="4" stroke-linecap="round"/>
  <polyline points="175,82 190,105 178,118" fill="none" stroke="#e2e8f0" stroke-width="4" stroke-linecap="round"/>
  <text x="235" y="75" fill="#00f59b" font-size="12" font-weight="black">臀中肌锁死膝盖对线</text>
  <text x="235" y="95" fill="#cbd5e1" font-size="10">半蹲微屈髋 · 侧向横移</text>
  <text x="235" y="115" fill="#f97316" font-size="10">弹力带全程绷紧撑开膝盖</text>
</svg>"""
    },

    # 27. 俯卧/俯身 Y-T-W 肩胛与肩袖激活
    "prone_ytw_raises": {
        "title": "俯卧/俯身 Y-T-W 肩袖激活 (Prone Y-T-W Raises)",
        "equipment": "瑜伽垫 / 1-2kg 极轻哑铃或徒手",
        "target": "下斜方肌、菱形肌、肩袖外旋肌群",
        "volleyballFocus": "【避开背阔肌，精雕肩袖微稳定】只动员深层护肩小肌群，赛前让扣球手臂润滑顺畅",
        "breathing": "手臂抬起夹紧肩胛骨时吐气，缓慢放下时吸气。",
        "steps": [
            "俯卧在垫面或俯身折髋约 45°，双手空握或持 1kg 极轻哑铃，大拇指全程朝上。",
            "【Y 字上举】：双臂向斜上方 135° 呈 Y 形抬起，下压肩胛骨，停顿 1 秒。",
            "【T 字平展】：双臂向正两侧 90° 呈 T 形抬起，挤压后背菱形肌，停顿 1 秒。",
            "【W 字夹臂】：屈肘呈 W 形向后上方外旋抬起，充分激活肩袖后束。"
        ],
        "mistakes": [
            "使用过重哑铃导致上斜方肌耸肩代偿、脖子僵硬。",
            "快速上下甩动，没有在最高点做出肩胛骨后缩停顿。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgYtw" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowYtw"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <rect width="400" height="240" fill="url(#bgYtw)"/>
  <!-- 俯视双肩肩胛骨示意 -->
  <circle cx="150" cy="70" r="12" fill="#cbd5e1"/>
  <path d="M 130,86 L 170,86 L 164,165 L 136,165 Z" fill="#94a3b8"/>
  <!-- 中下斜方肌与肩袖高亮 (倒三角微稳定区) -->
  <polygon points="136,88 164,88 150,128" fill="#00f59b" opacity="0.9" filter="url(#glowYtw)"/>
  <!-- Y 字方向虚线臂 -->
  <line x1="133" y1="90" x2="95" y2="45" stroke="#38bdf8" stroke-width="4" stroke-dasharray="4,2" stroke-linecap="round"/>
  <line x1="167" y1="90" x2="205" y2="45" stroke="#38bdf8" stroke-width="4" stroke-dasharray="4,2" stroke-linecap="round"/>
  <text x="82" y="38" fill="#38bdf8" font-size="13" font-weight="black">Y</text>
  <text x="208" y="38" fill="#38bdf8" font-size="13" font-weight="black">Y</text>
  <!-- T 字方向实线臂 -->
  <line x1="133" y1="92" x2="80" y2="92" stroke="#00f59b" stroke-width="5" stroke-linecap="round"/>
  <line x1="167" y1="92" x2="220" y2="92" stroke="#00f59b" stroke-width="5" stroke-linecap="round"/>
  <text x="64" y="96" fill="#00f59b" font-size="13" font-weight="black">T</text>
  <text x="225" y="96" fill="#00f59b" font-size="13" font-weight="black">T</text>
  <!-- W 字屈肘臂 -->
  <polyline points="133,96 105,120 90,102" fill="none" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
  <polyline points="167,96 195,120 210,102" fill="none" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
  <text x="74" y="106" fill="#f59e0b" font-size="13" font-weight="black">W</text>
  <text x="215" y="106" fill="#f59e0b" font-size="13" font-weight="black">W</text>
  <!-- 说明 -->
  <text x="248" y="65" fill="#00f59b" font-size="12" font-weight="black">肩袖微稳定激活</text>
  <text x="248" y="88" fill="#cbd5e1" font-size="10">大拇指朝上 · 沉肩夹背</text>
  <text x="248" y="108" fill="#38bdf8" font-size="10">极轻 1kg 或徒手(不力竭)</text>
  <text x="248" y="128" fill="#f59e0b" font-size="10">零背阔疲劳 · 赛前护肩必备</text>
</svg>"""
    },

    # 28. 轻量单腿罗马尼亚硬拉 (Single-Leg RDL)
    "single_leg_rdl": {
        "title": "轻量单腿罗马尼亚硬拉 (Single-Leg RDL)",
        "equipment": "自重 / 4-6kg 轻哑铃",
        "target": "单侧臀大肌、腘绳肌、足踝本体感觉平衡",
        "volleyballFocus": "【单脚落地吸震本能】唤醒单侧臀后链与脚踝微调神经，防止扣球落地重心失衡砸伤右膝",
        "breathing": "屈髋俯身下放时深吸气，臀大肌发力拉直回位时呼气。",
        "steps": [
            "单脚稳固站立，支撑腿膝关节保持微屈（约 15°）且全程锁定角度。",
            "收紧核心与骨盆保持水平（切忌骨盆向悬空侧翻转），后抬腿向后蹬伸。",
            "以髋关节为铰链，让上身与后摆腿如跷跷板般呈一条直线俯身至接近水平 T 字。",
            "感受支撑侧大腿后侧与臀部的强烈拉伸后，发力将髋部向前顶回直立姿。"
        ],
        "mistakes": [
            "骨盆旋转掀翻（像翻身一样把悬空侧髋部抬高），失去了稳定训练意义。",
            "弯腰驼背代替折叠髋关节，导致腰椎代偿受力。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgSlRdl" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowSlRdl"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <rect width="400" height="240" fill="url(#bgSlRdl)"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <!-- T 字平衡水平基准虚线 -->
  <line x1="70" y1="95" x2="290" y2="95" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,3"/>
  <!-- 躯干与后摆腿形成水平一条直线 -->
  <circle cx="255" cy="92" r="12" fill="#cbd5e1"/>
  <line x1="243" y1="95" x2="170" y2="95" stroke="#94a3b8" stroke-width="15" stroke-linecap="round"/>
  <line x1="170" y1="95" x2="90" y2="90" stroke="#64748b" stroke-width="9" stroke-linecap="round"/>
  <!-- 支撑腿臀大肌与腘绳肌高亮 -->
  <ellipse cx="170" cy="100" rx="14" ry="11" fill="#00f59b" opacity="0.9" filter="url(#glowSlRdl)"/>
  <polyline points="170,100 176,148 172,202" fill="none" stroke="#00f59b" stroke-width="8" stroke-linecap="round" filter="url(#glowSlRdl)"/>
  <!-- 手持轻哑铃垂直下垂 -->
  <line x1="225" y1="98" x2="225" y2="145" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <rect x="214" y="143" width="22" height="10" rx="3" fill="#f59e0b"/>
  <!-- 标注 -->
  <text x="45" y="50" fill="#00f59b" font-size="12" font-weight="black">水平 T 字单腿屈髋平衡</text>
  <text x="45" y="70" fill="#cbd5e1" font-size="10">骨盆水平不翻转 · 臀大肌后链吸震</text>
  <text x="235" y="185" fill="#f59e0b" font-size="10">轻负重(4-6kg)或徒手</text>
</svg>"""
    },

    # 29. 仰卧死虫子核心激活 (Deadbug)
    "deadbug_core": {
        "title": "仰卧死虫子核心激活 (Deadbug)",
        "equipment": "瑜伽垫 / 自重",
        "target": "腹横肌、深层核心稳定肌群",
        "volleyballFocus": "【空中抗折腰刚度】深度激活腹横肌，扣球空中拉弓发力时保护腰椎并锁紧躯干能量传递",
        "breathing": "对角手脚伸展下放时缓慢鼻吸气维持腹压，拉回时口呼气收紧肋骨。",
        "steps": [
            "仰卧平躺于瑜伽垫，双手臂垂直天花板伸直，双腿屈髋屈膝各呈 90° 抬起（桌腿姿）。",
            "【核心锁止铁律】：深呼一口气将肋骨下压，使下背部与地面之间的缝隙完全压死贴实。",
            "保持下背紧贴垫面绝对不起翘，缓慢将左手向头顶上方伸展，同时右腿向前下方缓慢伸直。",
            "在手脚接近地面（不触地）处停留 1 秒后受控拉回，换另一侧对角手脚交替进行。"
        ],
        "mistakes": [
            "腿下放时下腰部大幅度向上反弓腾空，会导致髂腰肌和腰椎直接代偿酸痛。",
            "手脚同时同侧伸展或动作过快甩动。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgBug" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowBug"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <rect width="400" height="240" fill="url(#bgBug)"/>
  <!-- 瑜伽垫地面 -->
  <rect x="40" y="185" width="320" height="8" rx="3" fill="#334155"/>
  <!-- 仰卧躯干 -->
  <circle cx="115" cy="168" r="12" fill="#cbd5e1"/>
  <line x1="128" y1="173" x2="215" y2="173" stroke="#94a3b8" stroke-width="15" stroke-linecap="round"/>
  <!-- 腹横肌深层高亮 + 下背贴地红/橙锁止区 -->
  <ellipse cx="172" cy="170" rx="22" ry="9" fill="#00f59b" opacity="0.9" filter="url(#glowBug)"/>
  <line x1="150" y1="184" x2="195" y2="184" stroke="#f97316" stroke-width="4"/>
  <!-- 固定垂直手臂与悬空90度腿 -->
  <line x1="140" y1="168" x2="140" y2="105" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <polyline points="215,170 215,125 255,125" fill="none" stroke="#64748b" stroke-width="7" stroke-linecap="round"/>
  <!-- 对角伸展手脚 (虚线延伸) -->
  <line x1="138" y1="168" x2="72" y2="162" stroke="#38bdf8" stroke-width="4" stroke-dasharray="4,2" stroke-linecap="round"/>
  <line x1="215" y1="172" x2="300" y2="174" stroke="#38bdf8" stroke-width="6" stroke-dasharray="4,2" stroke-linecap="round"/>
  <text x="140" y="205" fill="#f97316" font-size="11" font-weight="bold">▲ 下腰全程死贴垫面 (不可拱腰)</text>
  <text x="210" y="55" fill="#00f59b" font-size="12" font-weight="black">对角缓慢伸展抗过伸</text>
  <text x="210" y="75" fill="#cbd5e1" font-size="10">深度唤醒腹横肌核心刚度</text>
</svg>"""
    },

    # 30. 单杠悬垂收腹转体 (补全手绘精图)
    "hanging_knee_twist": {
        "title": "单杠悬垂收腹转体 (Hanging Knee Twist)",
        "equipment": "龙门架单杠 / 引体架",
        "target": "腹直肌下束、腹内外斜肌、转髋肌群",
        "volleyballFocus": "脱离地面支撑，训练滞空状态下转髋折叠并快速收腹扣球的复合力量",
        "breathing": "悬垂准备时吸气，向上收膝转体卷腹时强力吐气。",
        "steps": [
            "双手正握单杠（略宽于肩），沉肩拉长脊柱使身体垂直稳固悬垂不晃荡。",
            "骨盆后倾发力启动，将双膝并拢向上抬起并向左侧斜上方旋转挤压胸前。",
            "感受左侧腹斜肌与下腹充分拧紧收缩，顶峰停顿 0.5 秒。",
            "控制速度缓慢下放复原至悬垂，再转向右侧，全程不借助甩腿惯性。"
        ],
        "mistakes": [
            "像荡秋千一样利用惯性前后狂甩腿部，变成单纯的髂腰肌摆动。",
            "只抬膝盖而骨盆不向内向上卷曲，下腹肌几乎不怎么发力。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgHang" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowHang"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowHang" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,6 L3,0 L6,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgHang)"/>
  <line x1="60" y1="35" x2="340" y2="35" stroke="#cbd5e1" stroke-width="6" stroke-linecap="round"/>
  <!-- 双臂悬垂 -->
  <line x1="150" y1="38" x2="165" y2="85" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <line x1="210" y1="38" x2="195" y2="85" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <circle cx="180" cy="65" r="12" fill="#cbd5e1"/>
  <line x1="180" y1="82" x2="180" y2="135" stroke="#94a3b8" stroke-width="15" stroke-linecap="round"/>
  <!-- 腹斜肌与下腹高亮 -->
  <ellipse cx="176" cy="122" rx="13" ry="15" fill="#00f59b" opacity="0.9" filter="url(#glowHang)"/>
  <!-- 双膝斜向收腹抬起 -->
  <polyline points="180,135 142,115 135,148" fill="none" stroke="#64748b" stroke-width="8" stroke-linecap="round"/>
  <!-- 旋转向上箭头 -->
  <path d="M 180,180 Q 130,175 135,128" fill="none" stroke="#00f59b" stroke-width="3" stroke-dasharray="4,2" marker-end="url(#arrowHang)"/>
  <text x="230" y="85" fill="#00f59b" font-size="12" font-weight="black">骨盆后倾 + 斜向转髋</text>
  <text x="230" y="105" fill="#cbd5e1" font-size="10">悬垂脊柱减压 · 控速不摆荡</text>
  <text x="230" y="125" fill="#f59e0b" font-size="10">模拟滞空收腹扣杀折叠</text>
</svg>"""
    },

    # 31. 弹力带/绳索爆发转体冲拳 (补全手绘精图)
    "band_rotational_punch": {
        "title": "弹力带/绳索爆发转体冲拳 (Rotational Punch)",
        "equipment": "龙门架绳索 / 高弹力弹力带",
        "target": "腹斜肌、下肢转髋链、三角肌前束、胸大肌",
        "volleyballFocus": "打通脚掌蹬地->转髋->转躯干->手臂出拳的动力链，直接提升扣球挥臂出球初速度",
        "breathing": "蓄力拉弓时吸气，转髋暴发冲拳瞬间短促爆破吐气。",
        "steps": [
            "背对龙门架或弹力带锚点，呈前后弓步站立，单手握把手置于右肩前方蓄力。",
            "重心微压向后脚，微微向后旋髋蓄满弹性势能。",
            "【动能链传导】：后脚脚掌快速旋内蹬地 -> 髋部猛然转向正前方 -> 带动胸廓旋转。",
            "顺着躯干扭转的鞭打惯性，单臂暴发性向前上方直拳推出，控制速率匀速拉回。"
        ],
        "mistakes": [
            "单纯靠手臂往前推（没有后脚蹬地和转髋，完全丢失动力链发力精髓）。",
            "冲拳终点时上身前扑失去平衡。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgPunch" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowPunch"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowPunch" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgPunch)"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <rect x="45" y="45" width="12" height="160" fill="#334155"/>
  <circle cx="51" cy="115" r="7" fill="#64748b"/>
  <!-- 弓步旋转人物 -->
  <circle cx="170" cy="70" r="12" fill="#cbd5e1"/>
  <line x1="170" y1="82" x2="165" y2="140" stroke="#94a3b8" stroke-width="15" stroke-linecap="round"/>
  <!-- 腹斜肌发力旋转链高亮 -->
  <ellipse cx="168" cy="115" rx="14" ry="12" fill="#00f59b" opacity="0.9" filter="url(#glowPunch)"/>
  <polyline points="165,140 135,170 115,202" fill="none" stroke="#64748b" stroke-width="7" stroke-linecap="round"/>
  <polyline points="165,140 198,168 215,202" fill="none" stroke="#64748b" stroke-width="7" stroke-linecap="round"/>
  <!-- 绳索与爆发冲拳 -->
  <line x1="57" y1="115" x2="245" y2="95" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="4,2"/>
  <line x1="172" y1="95" x2="245" y2="95" stroke="#ffffff" stroke-width="6" stroke-linecap="round"/>
  <circle cx="248" cy="95" r="6" fill="#00f59b"/>
  <!-- 传导箭头 -->
  <line x1="200" y1="80" x2="265" y2="80" stroke="#00f59b" stroke-width="3" marker-end="url(#arrowPunch)"/>
  <text x="200" y="55" fill="#00f59b" font-size="12" font-weight="black">蹬地 → 转髋 → 鞭打冲拳</text>
  <text x="200" y="135" fill="#cbd5e1" font-size="10">模拟扣球瞬间全身动力链爆发</text>
</svg>"""
    },

    # 32. 杠铃推腹抗伸展 (补全手绘精图)
    "barbell_rollout": {
        "title": "杠铃推腹抗伸展 (Barbell Rollout)",
        "equipment": "杠铃杆 + 轻片 / 健腹轮",
        "target": "腹直肌全段、背阔肌、深层脊柱保护肌",
        "volleyballFocus": "强化扣球空中大幅度挺胸拉弓后防止腰椎过伸拉伤的绝对核心刹车力量",
        "breathing": "向前滚动展开时深吸气紧绷核心，拉回时大力呼气收腹。",
        "steps": [
            "双膝跪在瑜伽垫上，双手略宽于肩抓握装有圆片（可滚动）的杠铃杆，双臂垂直地面。",
            "臀部微夹紧、微微含胸拱背（骨盆后倾锁紧腰椎）。",
            "核心死死锁住腰部防下塌，双臂保持伸直顺势向前缓慢推滚杠铃至身体近似水平。",
            "在远端极限处保持 0.5 秒抗伸展张力，随后用腹直肌下拉感将杠铃拉回初始位。"
        ],
        "mistakes": [
            "向前推时屁股塌下去出现明显反弓（极易闪腰伤腰椎间盘）。",
            "拉回时先向后撅屁股坐回脚后跟偷懒，腹肌未完全吃力。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgRoll" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowRoll"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowRoll" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgRoll)"/>
  <line x1="20" y1="200" x2="380" y2="200" stroke="#1e293b" stroke-width="2"/>
  <rect x="60" y="192" width="110" height="8" rx="3" fill="#334155"/>
  <!-- 跪姿向前展开躯干 -->
  <polyline points="80,192 105,192 115,155" fill="none" stroke="#64748b" stroke-width="8" stroke-linecap="round"/>
  <line x1="115" y1="155" x2="210" y2="132" stroke="#94a3b8" stroke-width="15" stroke-linecap="round"/>
  <circle cx="222" cy="126" r="11" fill="#cbd5e1"/>
  <!-- 腹直肌防塌腰高亮 -->
  <ellipse cx="165" cy="148" rx="22" ry="9" transform="rotate(-14 165 148)" fill="#00f59b" opacity="0.9" filter="url(#glowRoll)"/>
  <!-- 手臂推滚杠铃 -->
  <line x1="205" y1="134" x2="275" y2="178" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <circle cx="275" cy="178" r="22" fill="#1e293b" stroke="#ef4444" stroke-width="4"/>
  <circle cx="275" cy="178" r="6" fill="#cbd5e1"/>
  <!-- 前后滚箭头 -->
  <line x1="230" y1="192" x2="315" y2="192" stroke="#00f59b" stroke-width="2.5" stroke-dasharray="4,2" marker-end="url(#arrowRoll)"/>
  <text x="65" y="65" fill="#00f59b" font-size="12" font-weight="black">锁紧骨盆后倾 · 坚决不塌腰</text>
  <text x="65" y="85" fill="#cbd5e1" font-size="10">打造扣球拉弓后的核心抗过伸护甲</text>
</svg>"""
    },

    # 33. 单腿着地制动缓冲 (Drop & Freeze 补全手绘精图)
    "single_leg_drop_freeze": {
        "title": "单腿着地制动缓冲 (Drop & Freeze)",
        "equipment": "低矮台阶 / 踏板 (20-35cm)",
        "target": "臀中肌、股四头肌离心制动、膝关节稳固对线",
        "volleyballFocus": "【防前交叉韧带撕裂神技】专治排球拦网或救球单脚落地晃动、膝内扣扭伤",
        "breathing": "迈下瞬间吸气核心绷紧，落地瞬间稳定呼气冻结姿势。",
        "steps": [
            "站在 20-30cm 低台阶上，单脚向前悬空准备迈下（严禁向上跳起）。",
            "身体自然受控下落，先用前脚掌轻柔触地后立刻过渡到全脚掌踩实。",
            "【落地冻结铁律】：落地瞬间立即屈髋向后坐、微屈膝缓冲，像雕塑一样静止凝固 2 秒！",
            "检查落地瞬间膝盖必须笔直对准第二脚趾，坚决不往内侧抖动歪斜。"
        ],
        "mistakes": [
            "像木头一样直腿砸向地面（无屈髋屈膝吸震缓冲）。",
            "落地瞬间膝盖明显往里扣入（Knee Valgus，十字韧带极其危险信号）。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgDrop" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowDrop"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowDrop" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,6 L3,0 L6,6 Z" fill="#38bdf8"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgDrop)"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <!-- 矮台阶 -->
  <rect x="45" y="145" width="75" height="60" rx="3" fill="#334155"/>
  <!-- 落地瞬间微屈缓冲单腿冻结人物 -->
  <circle cx="170" cy="68" r="12" fill="#cbd5e1"/>
  <line x1="170" y1="80" x2="155" y2="128" stroke="#94a3b8" stroke-width="15" stroke-linecap="round"/>
  <!-- 臀中肌与大腿吸震高亮 -->
  <ellipse cx="155" cy="128" rx="14" ry="11" fill="#00f59b" opacity="0.9" filter="url(#glowDrop)"/>
  <!-- 单腿屈膝落地踩实 -->
  <polyline points="155,128 175,160 168,202" fill="none" stroke="#00f59b" stroke-width="8" stroke-linecap="round" filter="url(#glowDrop)"/>
  <!-- 悬空未落地腿 -->
  <polyline points="155,128 140,158 135,175" fill="none" stroke="#64748b" stroke-width="6" stroke-linecap="round"/>
  <!-- 垂直对线激光线 -->
  <line x1="175" y1="115" x2="175" y2="205" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,2"/>
  <text x="195" y="75" fill="#00f59b" font-size="12" font-weight="black">单脚轻柔落地凝固 2s</text>
  <text x="195" y="95" fill="#cbd5e1" font-size="10">后坐屈髋吸震 · 膝盖不晃动</text>
  <text x="195" y="115" fill="#38bdf8" font-size="10">蓝色基准线：膝盖严禁内扣</text>
</svg>"""
    },

    # 34. 排球休闲对抗 / 基础传垫 (补全手绘精图)
    "volleyball_casual": {
        "title": "排球休闲对抗 / 基础传垫 (Casual Volleyball)",
        "equipment": "排球 / 排球场地",
        "target": "下肢低重心移动步伐、手臂传垫控制感、主动有氧恢复",
        "volleyballFocus": "维持球感与网前脚底移动节奏，兼具关节主动恢复与低冲击热身效果",
        "breathing": "随跑动和垫球节奏保持轻松连贯呼吸。",
        "steps": [
            "双脚略宽于肩，屈膝降低重心、脚跟微抬，保持随时可八方启动的准备姿。",
            "垫球时双手叠掌包紧，大拇指并拢向下压紧手腕，使两前臂组成平坦宽阔的垫球击球平面。",
            "迎球时用脚蹬地带动微伸膝向上迎送排球，而非单纯甩动双臂。",
            "传球时十指自然张开成半球形于额前上方迎击，保持步法到位率先于出手。"
        ],
        "mistakes": [
            "直立站着不动伸手捞球（垫球不稳易飞）。",
            "垫球时双臂弯曲发力甩肘，击球面不平整。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgPass" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowPass"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <rect width="400" height="240" fill="url(#bgPass)"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <!-- 低重心垫球人物 -->
  <circle cx="150" cy="85" r="12" fill="#cbd5e1"/>
  <line x1="150" y1="97" x2="138" y2="145" stroke="#94a3b8" stroke-width="15" stroke-linecap="round"/>
  <!-- 屈膝低重心下肢 -->
  <polyline points="138,145 162,165 152,202" fill="none" stroke="#64748b" stroke-width="8" stroke-linecap="round"/>
  <polyline points="138,145 118,175 112,202" fill="none" stroke="#64748b" stroke-width="8" stroke-linecap="round"/>
  <!-- 前臂伸直压腕垫球平面高亮 -->
  <line x1="148" y1="108" x2="195" y2="132" stroke="#00f59b" stroke-width="7" stroke-linecap="round" filter="url(#glowPass)"/>
  <!-- 排球与抛物线 -->
  <circle cx="215" cy="70" r="14" fill="#f59e0b" stroke="#38bdf8" stroke-width="2"/>
  <path d="M 192,126 Q 202,95 212,82" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="4,2"/>
  <text x="235" y="75" fill="#00f59b" font-size="12" font-weight="black">叠掌压腕平坦垫球面</text>
  <text x="235" y="95" fill="#cbd5e1" font-size="10">脚蹬地迎送 · 步法先到位</text>
  <text x="235" y="115" fill="#f59e0b" font-size="10">低重心弹性准备姿</text>
</svg>"""
    },

    # 35. 排球扣球弹跳专项打靶测试 (补全手绘精图)
    "volleyball_spike_session": {
        "title": "排球扣球弹跳专项打靶测试 (Spike Testing)",
        "equipment": "排球网 / 标志杆打靶区",
        "target": "极限助跑摸高、网口鞭打爆破速、落点控制",
        "volleyballFocus": "将体能房下肢与核心力量完美转化为网前直线/斜线暴力得分杀伤力",
        "breathing": "三步助跑末尾急停起跳深吸气，最高点下压扣球瞬间强力吐气。",
        "steps": [
            "站在 3 米线外做好三步（或四步）助跑准备，精准预判二传出球弧度与高度。",
            "最后一步制动并蹬地，双臂最大幅度向后摆臂后迅速上摆带飞身体极限高度。",
            "空中拉弓挺胸，左手指向来球测距，右手引肘在耳后最高点准备鞭打。",
            "全手掌包满球心后上方下压并甩腕，精准击打目标靶位，双脚轻盈屈髋缓冲落地。"
        ],
        "mistakes": [
            "人比球快冲到网底（球在脑后仰着腰硬扣，肩关节极大损伤）。",
            "起跳落差过大且疲劳时仍继续反复硬跳，应重质不重量及时止损。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgSpikeTest" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowSpikeTest"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <rect width="400" height="240" fill="url(#bgSpikeTest)"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <!-- 排球网 -->
  <line x1="220" y1="80" x2="220" y2="205" stroke="#ffffff" stroke-width="3"/>
  <rect x="218" y="85" width="4" height="50" fill="#f59e0b"/>
  <!-- 助跑三步轨迹箭头 -->
  <path d="M 45,198 Q 100,198 125,180 Q 145,115 160,65" fill="none" stroke="#00f59b" stroke-width="2.5" stroke-dasharray="4,2"/>
  <!-- 最高空扣杀人物 -->
  <circle cx="155" cy="52" r="11" fill="#cbd5e1"/>
  <path d="M 152,63 Q 142,88 158,110" fill="none" stroke="#00f59b" stroke-width="12" stroke-linecap="round" filter="url(#glowSpikeTest)"/>
  <polyline points="152,66 172,46 196,42" fill="none" stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>
  <polyline points="158,110 146,132 135,126" fill="none" stroke="#64748b" stroke-width="6" stroke-linecap="round"/>
  <!-- 排球与目标靶心 -->
  <circle cx="204" cy="40" r="10" fill="#38bdf8" stroke="#f59e0b" stroke-width="2"/>
  <line x1="208" y1="44" x2="335" y2="178" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="4,2"/>
  <!-- 地面靶心同心圆 -->
  <ellipse cx="340" cy="188" rx="22" ry="8" fill="none" stroke="#ef4444" stroke-width="2"/>
  <ellipse cx="340" cy="188" rx="10" ry="4" fill="#ef4444" opacity="0.8"/>
  <text x="240" y="55" fill="#00f59b" font-size="12" font-weight="black">极限摸高 · 精确钉地板打靶</text>
  <text x="240" y="75" fill="#cbd5e1" font-size="10">全掌包球 · 直线/大斜线控点</text>
</svg>"""
    },

    # 36. 哑铃交替弯举
    "db_bicep_curl": {
        "title": "哑铃交替弯举 (Dumbbell Bicep Curl)",
        "equipment": "一对轻中重量哑铃 (8-12kg)",
        "target": "肱二头肌长头与短头、肱肌",
        "volleyballFocus": "巩固肘关节前侧动态防超伸稳定性，打球日适度充血不影响扣球挥臂加速",
        "breathing": "上举弯举收缩时吐气，缓慢下放伸展时吸气。",
        "steps": [
            "双脚与肩同宽自然站立，核心收紧挺胸，双手持哑铃自然垂于体侧。",
            "大臂贴紧躯干两侧像焊死一样固定不动，掌心向前上方旋转并向上弯举。",
            "至二头肌最高点顶峰收缩 1 秒（避免哑铃撞肩放松张力）。",
            "用 2 秒匀速控制缓慢下放至接近完全伸直但肘关节微屈，交替进行。"
        ],
        "mistakes": [
            "利用前后晃腰或耸肩甩动借力，将大臂往前顶出。",
            "练到力竭前臂死僵（打球日每组留 2~3 次余力即可）。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgCurl" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowCurl"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowCurl" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,6 L3,0 L6,6 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgCurl)"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <circle cx="150" cy="60" r="12" fill="#cbd5e1"/>
  <line x1="150" y1="72" x2="150" y2="145" stroke="#94a3b8" stroke-width="15" stroke-linecap="round"/>
  <line x1="145" y1="145" x2="142" y2="202" stroke="#64748b" stroke-width="8" stroke-linecap="round"/>
  <line x1="155" y1="145" x2="158" y2="202" stroke="#64748b" stroke-width="8" stroke-linecap="round"/>
  <!-- 固定大臂与弯举小臂 -->
  <line x1="154" y1="84" x2="156" y2="122" stroke="#e2e8f0" stroke-width="6" stroke-linecap="round"/>
  <ellipse cx="156" cy="105" rx="7" ry="13" fill="#00f59b" opacity="0.9" filter="url(#glowCurl)"/>
  <line x1="156" y1="122" x2="188" y2="92" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <rect x="180" y="84" width="22" height="10" rx="3" fill="#f59e0b"/>
  <!-- 弧线弯举轨迹 -->
  <path d="M 190,145 Q 208,118 192,96" fill="none" stroke="#00f59b" stroke-width="2.5" stroke-dasharray="4,2" marker-end="url(#arrowCurl)"/>
  <text x="220" y="75" fill="#00f59b" font-size="12" font-weight="black">大臂夹紧 · 仅动肘关节</text>
  <text x="220" y="95" fill="#cbd5e1" font-size="10">顶峰停顿 1s · 控速不借力</text>
  <text x="220" y="115" fill="#f59e0b" font-size="10">打球日留2次余力不力竭</text>
</svg>"""
    },

    # 37. 龙门架绳索三头下压
    "cable_tricep_pushdown": {
        "title": "龙门架绳索三头下压 (Cable Tricep Pushdown)",
        "equipment": "龙门架高位滑轮 + 双头绳",
        "target": "肱三头肌外侧头、长头与内侧头",
        "volleyballFocus": "顺滑模拟扣球终末伸肘鞭打；打球日仅作轻重量泵感激活，严防三头肌过度酸胀导致扣球发沉",
        "breathing": "向下压直手臂时呼气，控制向上回放时吸气。",
        "steps": [
            "面对龙门架高位滑轮站立，身体微前倾 10°，双手对握双头绳，大臂紧贴肋部两侧。",
            "固定手肘位置作为轴心，发力将绳索垂直向下压至双臂完全伸直。",
            "在最低点顺势将双头绳向两侧微拉开，挤压肱三头肌顶峰 0.5 秒。",
            "控制重量缓慢屈肘回升至前臂与地面平行（或略高），保持全程张力。"
        ],
        "mistakes": [
            "重量过大导致手肘上下前后大幅度甩动或用身体向下压砸。",
            "在赛前将其练至完全力竭（会导致下午扣球挥臂发软）。"
        ],
        "svg": """<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgPushdown" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0b1120"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <filter id="glowPushdown"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arrowDownTri" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L3,6 L6,0 Z" fill="#00f59b"/></marker>
  </defs>
  <rect width="400" height="240" fill="url(#bgPushdown)"/>
  <line x1="20" y1="205" x2="380" y2="205" stroke="#1e293b" stroke-width="2"/>
  <rect x="60" y="30" width="12" height="175" fill="#334155"/>
  <circle cx="66" cy="40" r="7" fill="#64748b"/>
  <!-- 站立微前倾人物 -->
  <circle cx="170" cy="65" r="12" fill="#cbd5e1"/>
  <line x1="170" y1="77" x2="178" y2="145" stroke="#94a3b8" stroke-width="15" stroke-linecap="round"/>
  <line x1="175" y1="145" x2="165" y2="202" stroke="#64748b" stroke-width="8" stroke-linecap="round"/>
  <line x1="181" y1="145" x2="195" y2="202" stroke="#64748b" stroke-width="8" stroke-linecap="round"/>
  <!-- 大臂贴体侧，后侧三头肌高亮，小臂下压伸直 -->
  <line x1="168" y1="88" x2="160" y2="122" stroke="#e2e8f0" stroke-width="6" stroke-linecap="round"/>
  <ellipse cx="169" cy="108" rx="6" ry="12" fill="#00f59b" opacity="0.9" filter="url(#glowPushdown)"/>
  <line x1="160" y1="122" x2="140" y2="155" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <!-- 绳索连接 -->
  <line x1="72" y1="44" x2="140" y2="155" stroke="#f59e0b" stroke-width="2.5"/>
  <circle cx="140" cy="155" r="5" fill="#f59e0b"/>
  <line x1="122" y1="110" x2="122" y2="148" stroke="#00f59b" stroke-width="3" marker-end="url(#arrowDownTri)"/>
  <text x="215" y="75" fill="#00f59b" font-size="12" font-weight="black">固定双肘 · 垂直下压分绳</text>
  <text x="215" y="95" fill="#cbd5e1" font-size="10">轻中重量激活(15kg×15次)</text>
  <text x="215" y="115" fill="#f59e0b" font-size="10">严禁力竭以防下午扣球发沉</text>
</svg>"""
    }
}

# 读取 exercises.js 里的全部动作并生成完整的 js/exercise_illustrations.js
with open(r'F:\AntigravityWorkspace\projects\spikefit\js\exercises.js', 'r', encoding='utf-8') as f:
    content = f.read()

import re
pattern = r"\{\s*id:\s*'([^']+)',\s*name:\s*'([^']+)',\s*category:\s*'([^']+)',\s*categoryName:\s*'([^']+)',\s*equipment:\s*'([^']+)',\s*targetMuscle:\s*'([^']+)',\s*whyForVolleyball:\s*'([^']+)'"
matches = re.findall(pattern, content)

all_illustrations = {}
for m in matches:
    ex_id, name, cat, cat_name, eq, muscle, why = m
    if ex_id in ILLUSTRATIONS:
        all_illustrations[ex_id] = ILLUSTRATIONS[ex_id]
    else:
        raise ValueError(f"动作 [{ex_id}] ({name}) 缺少专属精细 SVG 教学图解定义！")

# 输出为 JS 文件（包含别名映射兼容，确保所有历史或变体ID都能秒级调出正确图解）
js_code = "/**\n * SpikeFit - 全套动作教学示意图与生物力学要领库\n * 涵盖全部 " + str(len(all_illustrations)) + " 个专项动作的纯矢量无损 SVG 示意图、动作标准拆解与避坑指南\n */\n"
js_code += "const EXERCISE_ILLUSTRATIONS = " + json.dumps(all_illustrations, ensure_ascii=False, indent=2) + ";\n\n"
js_code += """const ILLUSTRATION_ALIASES = {
  'hanging_knee_raise_twist': 'hanging_knee_twist',
  'seated_cable_row': 'cable_seated_row'
};

function getExerciseIllustration(exerciseId) {
  if (!exerciseId) return null;
  const resolvedId = ILLUSTRATION_ALIASES[exerciseId] || exerciseId;
  return EXERCISE_ILLUSTRATIONS[resolvedId] || null;
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { EXERCISE_ILLUSTRATIONS, getExerciseIllustration };
}
"""

with open(r'F:\AntigravityWorkspace\projects\spikefit\js\exercise_illustrations.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

print(f"成功为全部 {len(all_illustrations)} 个动作生成专属精细教学示意图与要领库！（0兜底、全覆盖）")
