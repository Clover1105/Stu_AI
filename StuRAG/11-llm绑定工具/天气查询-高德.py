# 初始化大模型
from langchain_ollama import ChatOllama
ollama = ChatOllama(
    model="qwen2.5:7b",
    base_url="http://127.0.0.1:11434"
)

# 参数校验
from pydantic import BaseModel, Field
class getWeather(BaseModel):
    city:str = Field(..., description="城市名称")

# 定义工具函数 -- 查询天气
from langchain_core.tools import tool
import requests
@tool(
    name_or_callable="get_weather",
    description="""
        当用户需要查询某个城市的天气时，调用此工具
        参数：
            city：字符串类型，表示城市名称
    """
)
def get_weather(city:str):
    print(f"查询天气的城市：{city}")
    # 引入天气查询接口 --- 第三方api【高德、心知】
    url = "https://restapi.amap.com/v3/weather/weatherInfo"
    params = {
        "key": "be2c23df0824437362ed4948ecfb50d9",
        "city": city,
    }
    # 通过requests发送get请求
    result = requests.get(url=url, params=params)
    result = result.json()
    # 拼接天气数据
    live = result["lives"][0]
    return {
        "result": (
            f"{live['province']}{live['city']}当前天气{live['weather']}，"
            f"气温{live['temperature_float']}℃，湿度{live['humidity_float']}%，"
            f"{live['winddirection']}风{live['windpower']}级，"
            f"数据更新时间为{live['reporttime']}。"
        )
    }

# 模型绑定工具
ollama = ollama.bind_tools(tools=[get_weather])

# 问题
que = "你好，今天重庆的天气怎么样？"

# 模型意图识别与工具调用决策
# 让大模型进行意图识别和参数提取，生成工具调用指令，而不是直接执行工具函数。
"""
语义理解：分析用户输入 "你好，今天重庆的天气怎么样？"，判断是否需要使用已绑定的工具。
决策输出：如果判定需要调用工具，模型不会返回天气结果，而是返回一个包含 tool_calls 的响应对象，其中指明了要调用的工具名（如 get_weather）及提取出的参数（如 {"city": "重庆"}）。
不执行逻辑：此时 get_weather 函数并未被实际运行，print 语句不会触发，也不会返回“晴天”等真实数据。
"""
response = ollama.invoke(que)   # 里面包含了：工具调用指令
print("意图识别结果：\n", response)

# 保存信息
messages = []
messages.append(response)

# 解析response结果，获取工具的具体信息，然后调用工具获取结果
for tool_call in messages[0].tool_calls:
    tool_name = tool_call['name']
    city = tool_call['args']['city']
    print(f"工具名称：{tool_name}, 城市：{city}")
    tool_result = eval(tool_name).invoke(tool_call)
    print(f"工具调用结果：{tool_result}")
    # 保存工具调用结果
    messages.append(tool_result)

# 最后的回复
fin = ollama.invoke(messages)
print("最终的回复：\n", fin)