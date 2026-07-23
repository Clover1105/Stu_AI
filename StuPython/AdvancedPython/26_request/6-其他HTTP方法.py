"""
    DELETE：删除资源
    PUT：完整更新资源（替换）
    PATCH：部分更新资源
    HEAD：只获取响应头，不获取响应体

    注意事项：
    HEAD请求没有响应体，response.text为空
    PUT和PATCH通常需要配合data或json参数
"""

import requests

base_url = 'https://httpbin.org'

# DELETE请求
response = requests.delete(f'{base_url}/delete')
print(f"状态码: {response.status_code}")
print(f"响应内容: {response.json()}\n")

# PUT请求（完整更新）
put_data = {'id': 1, 'name': '更新后的名称', 'status': 'active'}
response = requests.put(f'{base_url}/put', json=put_data)
print(f"状态码: {response.status_code}")
print(f"服务器接收的数据: {response.json().get('json')}\n")

# PATCH请求（部分更新）
patch_data = {'status': 'inactive'}  # 只更新状态字段
response = requests.patch(f'{base_url}/patch', json=patch_data)
print(f"状态码: {response.status_code}")
print(f"服务器接收的数据: {response.json().get('json')}\n")

# HEAD请求（只获取响应头）
response = requests.head(f'{base_url}/get')
print(f"状态码: {response.status_code}")
print(f"响应头: {dict(response.headers)}")
print(f"响应体内容长度: {len(response.text)} (HEAD请求无响应体)")