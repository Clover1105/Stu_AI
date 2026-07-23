"""
    data参数：发送application/x-www-form-urlencoded格式（表单）
    json参数：发送application/json格式，自动序列化字典
    files参数：发送multipart/form-data格式，用于文件上传

    注意事项：
    data和json不要混用，根据API要求选择
    上传文件需要以'rb'模式打开
"""

import requests

url = 'https://httpbin.org/post'

# 表单数据（application/x-www-form-urlencoded）
form_data = {'username': 'jack', 'password': '123456'}
response = requests.post(url, data=form_data)
print(f"状态码: {response.status_code}")
print(f"服务器接收的表单数据: {response.json().get('form')}\n")

# JSON数据（application/json）
json_data = {'username': 'jack', 'password': '123456', 'role': 'admin'}
response = requests.post(url, json=json_data)
print(f"服务器接收的JSON数据: {response.json().get('json')}\n")

# 文件上传
# 创建测试文件
with open('test.txt', 'w') as f:
    f.write('这是测试上传的内容')
# 上传文件
with open('test.txt', 'rb') as f:
    files = {'file': ('test.txt', f, 'text/plain')}
    response = requests.post(url, files=files)
print(f"服务器响应的文件信息: {response.json().get('files')}")