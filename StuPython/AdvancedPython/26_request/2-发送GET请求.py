"""
    requests.get(url, params=字典) 发送GET请求，params自动拼接URL参数
    response.text 获取文本内容
    response.content 获取二进制内容
    response.status_code 获取状态码
    response.json() 解析JSON响应

    下载文件要用 'wb' 模式写入，避免编码问题
    params中的参数值会自动URL编码
"""

import requests

# GET请求
url = 'https://httpbin.org/get'
response = requests.get(url)
print(f"状态码: {response.status_code}")
print(f"响应内容前200字符: {response.text[:200]}\n")

# 带查询参数的GET请求
params = {'name': '张三', 'age': 25, 'city': '北京'}
response = requests.get(url, params=params)
print(f"最终请求URL: {response.url}")
print(f"服务器返回的参数: {response.json().get('args')}\n")

# 下载图片文件
image_url = 'https://www.python.org/static/img/python-logo.png'
response = requests.get(image_url)
if response.status_code == 200:
    with open('python_logo.png', 'wb') as f:
        f.write(response.content)
    print("图片已成功下载并保存为 python_logo.png")
else:
    print(f"下载失败，状态码：{response.status_code}")