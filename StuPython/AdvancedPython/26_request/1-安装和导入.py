"""
- 使用pip install requests安装
- import requests导入模块
- 这是一个常用的HTTP请求库
"""

"""
Python requests 是一个常用的 HTTP 请求库，可以方便地向网站发送 HTTP 请求，并获取响应结果。
使用 requests 发送 HTTP 请求需要先下载并导入 requests 模块
"""

# url 就是网址
# 有固定的格式 协议://ip(或者域名):端口/路径?参数=值&参数=值
# http://

import requests

print(f"requests模块版本：{requests.__version__}")
print("requests模块已成功导入")