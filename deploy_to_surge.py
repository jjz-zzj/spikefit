import io
import os
import tarfile
import random
import requests

PROJECT_DIR = r"F:\AntigravityWorkspace\projects\spikefit"
DOMAIN = "spikefit-volleyball.surge.sh"

def deploy():
    # 1. 注册/获取 Token
    rand_id = random.randint(100000, 999999)
    email = f"spikefit_vball_{rand_id}@surge-deploy.io"
    password = f"SpikeFit_{rand_id}_Pass"

    print("正在向公网静态服务申请授权...")
    res = requests.post("https://surge.surge.sh/token", auth=(email, password))
    if res.status_code not in (200, 201):
        print("获取 Token 失败:", res.status_code, res.text)
        return False
    
    token_info = res.json()
    token = token_info.get("token")
    print("已成功获取公网部署授权 Token！")

    # 2. 打包项目目录为 tar.gz
    print("正在打包前端工程文件...")
    tar_stream = io.BytesIO()
    with tarfile.open(fileobj=tar_stream, mode="w:gz") as tar:
        for root, dirs, files in os.walk(PROJECT_DIR):
            for file in files:
                # 排除 pycache 和 python 脚本及临时文件
                if file.endswith(('.py', '.pyc', '.bat', '.jsonl', '.db', '.log')) or '__pycache__' in root:
                    continue
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, PROJECT_DIR).replace('\\', '/')
                tar.add(full_path, arcname=rel_path)
    
    tar_stream.seek(0)
    print(f"打包完成，压缩体积: {len(tar_stream.getvalue())} 字节")

    # 3. 部署到 Surge
    target_domains = [DOMAIN, f"spikefit-pro-{rand_id}.surge.sh"]
    
    for dom in target_domains:
        print(f"正在发布至公网域名: https://{dom} ...")
        tar_stream.seek(0)
        url = f"https://surge.surge.sh/{dom}"
        headers = {
            "Content-Type": "application/gzip",
            "Accept": "application/x-ndjson"
        }
        resp = requests.put(url, auth=("token", token), headers=headers, data=tar_stream, stream=True)
        print("响应状态码:", resp.status_code)
        
        success = False
        for line in resp.iter_lines():
            if line:
                line_str = line.decode('utf-8')
                print("Deploy log:", line_str)
                if '"success":true' in line_str or 'Success!' in line_str:
                    success = True

        if resp.status_code == 200:
            print("\n" + "="*50)
            print(f"🎉 部署成功！公网 HTTPS 访问地址：https://{dom}")
            print("="*50)
            return f"https://{dom}"
    
    return False

if __name__ == '__main__':
    deploy()
