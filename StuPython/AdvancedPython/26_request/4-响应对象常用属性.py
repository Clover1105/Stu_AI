"""
    status_code：HTTP状态码（200成功，404未找到，500服务器错误）
    headers：响应头（字典格式）
    content：字节格式的响应内容
    text：字符串格式的响应内容
    encoding：响应内容的编码格式
    url：最终请求的URL（自动处理重定向）

    注意事项：
    访问不存在的属性会报错
    json()方法解析失败会抛出异常，建议用try包裹
"""

import requests

url = 'https://httpbin.org/get'
response = requests.get(url)

print(f"1. 状态码 (status_code): {response.status_code}")
print(f"2. 响应头 (headers): {dict(response.headers)}")
print(f"3. 响应内容长度 content: {len(response.content)} 字节")
print(f"4. 响应文本前100字符 text: {response.text[:100]}")
print(f"5. 编码格式 (encoding): {response.encoding}")
print(f"6. 最终URL (url): {response.url}")

# 额外：JSON解析示例
print(f"\n7. JSON解析 (json()): {response.json().get('url')}")