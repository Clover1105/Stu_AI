import requests
from langchain.tools import tool
from pydantic import BaseModel,Field
from util.geocode import get_geocode
from dotenv import load_dotenv
import os
load_dotenv()

# 参数校验
class AmapDriverToolScheam(BaseModel):
    start_location:str = Field(...,description="起始地址")
    end_location:str = Field(...,description="终点地址，目的地")


@tool(args_schema=AmapDriverToolScheam)
def AmapDriverTool(start_location:str,end_location:str) -> str:
    """
    查询汽车从起始地址到目的地的路线
    """
    try:
        # 计算地理编码
        start = get_geocode(start_location)
        end = get_geocode(end_location)
        url = os.getenv("GAODE_DRP_URL")
        params = {
            "key": os.getenv("GAODE_AMAP_KEY"),
            "origin": start,
            "destination": end,
        }
        rs = requests.get(url=url, params=params)
        rs = rs.json()
        print(rs)
        data = rs["route"]["paths"]
        return data
    except Exception as e:
        return f"查询汽车从起始地址到目的地的路线失败:{e}"

if __name__ == '__main__':
    AmapDriverTool.invoke({
        "start_location":"重庆北站",
        "end_location":"成都东站"
    })