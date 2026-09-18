from app.ai.agent.multi_agent.scheam.intent_scheam import RouterSchema
from app.ai.model.my_model import MyModel
from app.ai.prompt.bulider_prompt import BuilderPromptYaml
from langchain.agents import create_agent
from langchain.agents.middleware import ModelCallLimitMiddleware

# 路由分类节点

# 读取外部提示词配置文件
prompt = BuilderPromptYaml.get_prompt("router_agent.yaml")

# 创建意图识别智能体
def router_agent(question):
    print('\n【测试】这里是 -- router_node.py')
    try:
        # 获取本地模型
        model = MyModel.get_local_model()
        print("【测试】正在调用本地模型进行路由分类...")
        # 创建智能体
        agent = create_agent(
            model=model,
            system_prompt=prompt,
            response_format=RouterSchema,
            debug=True,
            middleware=[
                ModelCallLimitMiddleware(
                    thread_limit=3,
                    exit_behavior="end",
                )
            ],
        )
        # 提问
        user_msg = {"messages":{"role":"user","content":question}}
        rs = agent.invoke(user_msg)
        print(f"【测试】路由分类结果：{rs}")

        # 将输入结果转换为字典，json
        router_value = "chat"
        if "structured_response" in rs:
            data = rs["structured_response"].model_dump()
            router_value = data.get('router','chat')
        else:
            # 如果 structured_response 不存在，尝试从 AIMessage 的 content 中解析 (模型直接返回文本的情况)
            # 注意：这里需要确保 rs["messages"] 中最后一条是 AIMessage
            last_message = rs.get("messages", [])[1]
            if hasattr(last_message, 'content') and last_message.content:
                try:
                    # 尝试将 content 解析为 JSON
                    import json
                    content_json = json.loads(last_message.content)
                    router_value = content_json.get('router', 'chat')
                except json.JSONDecodeError:
                    # 如果 content 不是有效的 JSON，则保持默认值或进行其他处理
                    print("【测试】警告：模型返回的文本内容不是有效的JSON格式")
        return router_value

    except Exception as e:
        print(f"【测试】大模型路由分类兜底")
        print(f"【测试】报错信息：{e}")
        try:
            # 获取本地模型
            model = MyModel.get_model()
            print("【测试】正在调用在线模型进行路由分类...")
            # 创建智能体
            agent = create_agent(
                model=model,
                system_prompt=prompt,
                response_format=RouterSchema,
                debug=True,
                middleware=[
                    ModelCallLimitMiddleware(
                        thread_limit=3,
                        exit_behavior="end",
                    )
                ],
            )
            # 提问
            user_msg = {"messages": {"role": "user", "content": question}}
            rs = agent.invoke(user_msg)
            print(f"【测试】路由分类结果：{rs}")

            # 将输入结果转换为字典，json
            router_value = "chat"
            if "structured_response" in rs:
                data = rs["structured_response"].model_dump()
                router_value = data.get('router', 'chat')
            else:
                # 如果 structured_response 不存在，尝试从 AIMessage 的 content 中解析 (模型直接返回文本的情况)
                # 注意：这里需要确保 rs["messages"] 中最后一条是 AIMessage
                last_message = rs.get("messages", [])[1]
                if hasattr(last_message, 'content') and last_message.content:
                    try:
                        # 尝试将 content 解析为 JSON
                        import json
                        content_json = json.loads(last_message.content)
                        router_value = content_json.get('router', 'chat')
                    except json.JSONDecodeError:
                        # 如果 content 不是有效的 JSON，则保持默认值或进行其他处理
                        print("【测试】警告：模型返回的文本内容不是有效的JSON格式")
            return router_value

        except Exception as e:
            print("【测试】返回自定义路由分类结果")
            print(f"【测试】报错信息：{e}")
            return "chat"





