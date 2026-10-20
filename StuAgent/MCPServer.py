from fastmcp import FastMCP
import os
import requests

from dotenv import load_dotenv
load_dotenv()

mcp = FastMCP("clover")

# 操作数据库
@mcp.tool(
    name="get_weather",
    description=("查询某个城市天气")
)
async def get_weather(city):
    api_key = os.getenv("XINZHI_API_KEY")
    url = f"https://api.seniverse.com/v3/weather/now.json?key={api_key}&location={city}&language=zh-Hans&unit=c"
    rs = requests.get(url)
    json_data = rs.json()
    r = json_data['results'][0]
    return (f"{r['location']['name']} | "
            f"{r['now']['text']} | "
            f"{r['now']['temperature']}°C | "
            f"更新: {r['last_update']}")

# cloudflared.exe tunnel --url http://127.0.0.1:8000/mcp
if __name__ == '__main__':
    mcp.run(
        transport="http",
        host="127.0.0.1",
        port=8000,
        show_banner=True,
        path='/mcp'
    )