import redis
from langchain.agents.middleware import before_model, AgentState, after_model
from langgraph.runtime import Runtime


# 连接redis
client = redis.StrictRedis(host="localhost",port=6379,password="123456",db=0)

@before_model
def ModelCallLimitBeforeMiddleware(state:AgentState,time:Runtime):
    print(time)
    # 用户id
    user_id = time.execution_info.thread_id
    print(f"用户id:{user_id}")
    # 查询到用户的模型使用次数
    num = 3
    # 自定义键名
    key = f"limit:{user_id}"
    # 获取值
    value = client.get(key)
    print(f"value:{value}")
    if value is None:
        return {}
    else:
        data = int(value.decode("utf-8"))
        if data >= num:
            raise ValueError(f"用户{user_id}模型使用次数超过限制{num}次，不允许生成")



@after_model
def ModelCallLimitAfterMiddleware(state:AgentState,time:Runtime):
    user_id = time.execution_info.thread_id
    print(f"用户id:{user_id}")
    # 自定义键名
    key = f"limit:{user_id}"
    # 设置自增
    client.incr(key,1)
    # 设置失效事件
    client.expire(key,300)
    print(f"用户{user_id}模型使用次数增加1")
    return {}