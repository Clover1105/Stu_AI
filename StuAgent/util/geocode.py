import requests
from dotenv import load_dotenv
import os
load_dotenv()

# 根据地点获取地理编码
def get_geocode(address):
    # 定义地址
    url = os.getenv("GAODE_GEO_URL")
    # 定义参数（字典）
    params = {
        "key": os.getenv("GAODE_AMAP_KEY"),
        "address": address
    }
    r = requests.get(url=url, params=params)
    # print(r)    # <Response [200]>
    # print(r.json())   # {'status': '1', 'info': 'OK', 'infocode': '10000', 'count': '2', 'geocodes': [{'formatted_address': '北京市海淀区中关村大街1号', 'country': '中国', 'province': '北京市', 'citycode': '010', 'city': '北京市', 'district': '海淀区', 'township': [], 'neighborhood': {'name': [], 'type': []}, 'building': {'name': [], 'type': []}, 'adcode': '110108', 'street': '中关村大街', 'number': '1号', 'location': '116.315419,39.983342', 'level': '门址'}, {'formatted_address': '北京市海淀区中关村大街4号', 'country': '中国', 'province': '北京市', 'citycode': '010', 'city': '北京市', 'district': '海淀区', 'township': [], 'neighborhood': {'name': [], 'type': []}, 'building': {'name': [], 'type': []}, 'adcode': '110108', 'street': '中关村大街', 'number': [], 'location': '116.317147,39.983495', 'level': '门牌号'}]}
    # 格式转换
    r = r.json() # 需要的字段：location
    # 提取需要的内容
    location = r["geocodes"][0]["location"]
    return location

if __name__ == '__main__':
    get_geocode("北京市海淀区中关村大街1号")