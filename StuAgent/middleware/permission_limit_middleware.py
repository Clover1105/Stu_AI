import ast

import redis
from langchain.agents.middleware import AgentState, after_agent, before_agent
from langgraph.runtime import Runtime
from langchain_core.messages import AIMessage

from tool.query_employee_tool import QueryEmployeeTool


#链接redis服务
client = redis.StrictRedis(host='localhost', port=6379, password=123456, db=0)

# 权限校验
@before_agent
def PermissionCheckMiddleware(state:AgentState,time:Runtime):
    # 用户id
    user_id = time.execution_info.thread_id
    # 演示案例，在数据库中查询
    result = QueryEmployeeTool.invoke({
        "sql":f"select department from employee where user_id = '{user_id}'"
    })
    print(result)
    print(type(result))
    # 类型转换 -- 将包含 Python 字面量（如列表、字典、字符串等）的字符串安全地解析并转换为真实的 Python 对象
    # data = ast.literal_eval(result)
    # 获取部门
    department = result[0]['department']
    # 只有管理员，可以访问
    if department != "管理员":
        raise Exception(f"用户{user_id}没有权限访问")
    return {}


# 统计消耗token -- 单次对话
@after_agent()
def CountTokenMiddleware(state:AgentState,time:Runtime):
    # 用户id
    user_id = time.execution_info.thread_id
    # 计算token
    token = 0
    usage_metadata = state['messages'][-1].usage_metadata
    if usage_metadata:
        print(usage_metadata)
        input_tokens = usage_metadata['input_tokens']
        output_tokens = usage_metadata['output_tokens']
        total_tokens = usage_metadata['total_tokens']
        token += input_tokens + output_tokens + total_tokens
        print(f"用户消耗token:{token}")
        return {
            "messages": [AIMessage(content=f"输入token:{input_tokens}，输出token:{output_tokens}，总token:{total_tokens}")]
        }
    return {}

# 统计消耗token -- 多轮对话
@after_agent()
def CountTokenMemoryMiddleware(state:AgentState,time:Runtime):
    # 用户id
    user_id = time.execution_info.thread_id
    # 自定义键名
    key = f"countToken:{user_id}"
    # 获取键的值 -- 存的token，为什么不能用get
    value = client.hgetall(key)
    print(f"获取redis中的值:{value}")
    # 计算token
    token = 0
    # 从redis中获取token，不存在设置为0，存在直接取出
    if not value:
        input_tokens = 0
        output_tokens = 0
        total_tokens = 0
        client.hset(key, "input_tokens", input_tokens)
        client.hset(key, "output_tokens", output_tokens)
        client.hset(key, "total_tokens", total_tokens)
        print(f"初始token：{input_tokens}、{output_tokens}、{total_tokens}")
    else:
        print("开始从redis中取值")
        input_tokens = client.hget(key, "input_tokens")
        print(f"获取redis的输入token类型(decode前):{type(input_tokens)}")
        print(f"获取redis的输入token(decode前):{input_tokens}")
        input_tokens = input_tokens.decode()
        print(f"获取redis的输入token类型(decode后):{type(input_tokens)}")
        print(f"获取redis的输入token(decode后):{input_tokens}")
        input_tokens = int(input_tokens)
        print(f"获取redis的输入token类型(类型转换后后):{type(input_tokens)}")
        output_tokens = int(client.hget(key, "output_tokens").decode())
        total_tokens = int(client.hget(key, "total_tokens").decode())
        print(f"获取redis的输出token:{output_tokens}")
        print(f"获取redis的总token:{total_tokens}")
    # 或取本轮对话所消耗的token值，加上以前的值后再存入redis
    usage_metadata = state['messages'][-1].usage_metadata
    if usage_metadata:
        print(usage_metadata)
        input_tokens += usage_metadata['input_tokens']
        output_tokens += usage_metadata['output_tokens']
        total_tokens += usage_metadata['total_tokens']
        token += input_tokens + output_tokens + total_tokens
        print(f"用户累计消耗token:{total_tokens}")
        # 将新值存入redis中
        client.hset(key, "input_tokens", input_tokens)
        client.hset(key, "output_tokens", output_tokens)
        client.hset(key, "total_tokens", total_tokens)
        return {
            "messages": [AIMessage(content=f"输入token:{input_tokens}，输出token:{output_tokens}，总token:{total_tokens}")]
        }
    return {}