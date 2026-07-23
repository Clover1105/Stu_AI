"""
    requests.request(method, url, **kwargs) 可以发送任意HTTP方法，向指定的 url 发送指定的请求方法
    method参数：'GET'、'POST'、'PUT'、'DELETE'等字符串
    其他参数与具体方法一致（params、data、json、headers等）

    注意事项：
    method必须是大写字符串
    适合需要动态切换请求方法的场景
"""

import requests

url = 'https://httpbin.org'

# 使用request方法发送GET请求
response = requests.request('GET', f'{url}/get', params={'q': 'python'})
print(f"状态码: {response.status_code}")
print(f"请求URL: {response.url}\n")

# 使用request方法发送POST请求（JSON）
response = requests.request(
    method='POST',
    url=f'{url}/post',
    json={'name': '张三', 'age': 25},
    headers={'User-Agent': 'MyApp/1.0'}
)
print(f"状态码: {response.status_code}")
print(f"服务器接收的JSON: {response.json().get('json')}\n")

# 动态切换请求方法（实际应用场景）
def send_request(method, endpoint, data=None):
    """通用的请求发送函数"""
    full_url = f'{url}/{endpoint}'
    response = requests.request(method, full_url, json=data)
    return response

# 调用示例
get_resp = send_request('GET', 'get')
print(f"GET请求状态码: {get_resp.status_code}")

post_resp = send_request('POST', 'post', {'key': 'value'})
print(f"POST请求状态码: {post_resp.status_code}")
print(f"POST响应数据: {post_resp.json().get('json')}")