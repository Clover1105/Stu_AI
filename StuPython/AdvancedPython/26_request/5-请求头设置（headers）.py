"""
    headers参数接收字典，用于设置User-Agent、Authorization等
    常见用途：模拟浏览器、传递认证令牌、指定内容类型

    注意事项：
    某些服务器会检查User-Agent，不设置可能被拒绝访问
    Authorization头的常见格式：'Bearer token值' 或 'Basic base64字符串'
"""

import requests

url = 'https://httpbin.org/headers'

# 基础请求头设置
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}
response = requests.get(url, headers=headers)
print("服务器收到的请求头:")
print(f"  User-Agent: {response.json().get('headers').get('User-Agent')}")
print(f"  Accept: {response.json().get('headers').get('Accept')}")

# 带认证的请求头
headers_with_auth = {
    'User-Agent': 'Mozilla/5.0',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xyz',
    'X-API-Key': 'abc123456'
}
response = requests.get(url, headers=headers_with_auth)
print(f"Authorization头: {response.json().get('headers').get('Authorization')}")
print(f"X-API-Key头: {response.json().get('headers').get('X-Api-Key')}")