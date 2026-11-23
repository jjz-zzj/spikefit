#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SpikeFit 本地局域网服务与多端数据同步中继
- 自动识别电脑局域网 IP
- 提供手机极速扫码访问
- 支持局域网离线数据同步与云端中继双保险
- 自动在浏览器中打开主界面
"""

import os
import sys
import json
import socket
import webbrowser
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import urllib.parse

PORT = 8080
STORAGE_FILE = os.path.join(os.path.dirname(__file__), 'local_sync_store.json')

def get_local_ip():
    """获取本机局域网 IPv4 地址"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

class SpikeFitRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        directory = os.path.dirname(os.path.abspath(__file__))
        super().__init__(*args, directory=directory, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == '/api/local_sync':
            params = urllib.parse.parse_qs(parsed.query)
            code = params.get('code', [''])[0].upper()
            self.handle_get_sync(code)
            return
        elif parsed.path == '/api/server_info':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            info = {
                'localIp': get_local_ip(),
                'port': PORT,
                'mobileUrl': f"http://{get_local_ip()}:{PORT}"
            }
            self.wfile.write(json.dumps(info).encode('utf-8'))
            return
        
        # 静态文件服务
        return super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == '/api/local_sync':
            content_length = int(self.headers.get('Content-Length', 0))
            post_body = self.rfile.read(content_length)
            try:
                payload = json.loads(post_body.decode('utf-8'))
                self.handle_post_sync(payload)
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(f'{{"error": "{str(e)}"}}'.encode('utf-8'))
            return
        return super().do_POST()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def handle_get_sync(self, code):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        store = {}
        if os.path.exists(STORAGE_FILE):
            try:
                with open(STORAGE_FILE, 'r', encoding='utf-8') as f:
                    store = json.load(f)
            except Exception:
                pass

        matched = store.get(code)
        if matched:
            self.wfile.write(json.dumps({'success': True, 'data': matched}).encode('utf-8'))
        else:
            self.wfile.write(json.dumps({'success': False, 'message': '未找到匹配数据'}).encode('utf-8'))

    def handle_post_sync(self, payload):
        code = str(payload.get('syncCode', '')).upper()
        data = payload.get('data')

        store = {}
        if os.path.exists(STORAGE_FILE):
            try:
                with open(STORAGE_FILE, 'r', encoding='utf-8') as f:
                    store = json.load(f)
            except Exception:
                pass

        if code and data:
            store[code] = data
            with open(STORAGE_FILE, 'w', encoding='utf-8') as f:
                json.dump(store, f, ensure_ascii=False, indent=2)

        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps({'success': True, 'message': '局域网中继同步成功'}).encode('utf-8'))


def run_server():
    local_ip = get_local_ip()
    server_address = ('0.0.0.0', PORT)
    
    try:
        httpd = ThreadingHTTPServer(server_address, SpikeFitRequestHandler)
    except OSError:
        # 端口若被占用，使用备用端口
        httpd = ThreadingHTTPServer(('0.0.0.0', PORT + 1), SpikeFitRequestHandler)

    actual_port = httpd.server_port
    local_url = f"http://localhost:{actual_port}"
    mobile_url = f"http://{local_ip}:{actual_port}"

    print("=" * 64)
    print("🏐 SpikeFit - 排球专项体能与健身计划服务已启动！")
    print("=" * 64)
    print(f"💻 电脑浏览器访问:  {local_url}")
    print(f"📱 手机同 Wi-Fi 访问: {mobile_url}")
    print("=" * 64)
    print("💡 手机扫码与使用提示:")
    print("  1. 手机连接与电脑相同的 Wi-Fi；")
    print(f"  2. 打开手机浏览器输入: {mobile_url} (或在电脑网页中点击'手机扫码')；")
    print("  3. 也可以在任意网络（包括 5G）下，使用网页顶部的 6 位同步口令进行免登录云同步！")
    print("=" * 64)
    print("按 Ctrl + C 可停止服务。\n")

    # 自动在默认浏览器中打开
    try:
        webbrowser.open(local_url)
    except Exception:
        pass

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务已平稳关闭。")
        sys.exit(0)

if __name__ == '__main__':
    run_server()
