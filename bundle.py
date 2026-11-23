import os

base_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_dir, 'index.html'), 'r', encoding='utf-8') as f:
    html = f.read()

with open(os.path.join(base_dir, 'css', 'custom.css'), 'r', encoding='utf-8') as f:
    css = f.read()

with open(os.path.join(base_dir, 'js', 'exercises.js'), 'r', encoding='utf-8') as f:
    exercises = f.read()

with open(os.path.join(base_dir, 'js', 'calculator.js'), 'r', encoding='utf-8') as f:
    calculator = f.read()

with open(os.path.join(base_dir, 'js', 'recommender.js'), 'r', encoding='utf-8') as f:
    recommender = f.read()

with open(os.path.join(base_dir, 'js', 'nutrition.js'), 'r', encoding='utf-8') as f:
    nutrition = f.read()

with open(os.path.join(base_dir, 'js', 'sync.js'), 'r', encoding='utf-8') as f:
    sync = f.read()

with open(os.path.join(base_dir, 'js', 'app.js'), 'r', encoding='utf-8') as f:
    app = f.read()

# 内联 CSS
html = html.replace('<link rel="stylesheet" href="./css/custom.css">', f'<style>\n{css}\n</style>')

# 内联 JS
js_block = f"""  <script>
{exercises}

{calculator}

{recommender}

{nutrition}

{sync}

{app}
  </script>"""

find_scripts = """  <!-- 引入业务核心模块 -->
  <script src="./js/exercises.js"></script>
  <script src="./js/calculator.js"></script>
  <script src="./js/recommender.js"></script>
  <script src="./js/nutrition.js"></script>
  <script src="./js/sync.js"></script>
  <script src="./js/app.js"></script>"""

if find_scripts in html:
    html = html.replace(find_scripts, js_block)
else:
    # 查找 </body> 前插入
    html = html.replace('</body>', f'{js_block}\n</body>')

output_path = os.path.join(base_dir, 'SpikeFit_手机便携离线版.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"打包成功！已生成单文件版：{output_path}，大小：{len(html)} 字节")
