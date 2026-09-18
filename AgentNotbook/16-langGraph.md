# 一、LangGraph

## （一）认识LangGraph

**LangGraph** 是 LangChain 生态中专门用于**构建有状态、多角色、复杂工作流的智能体框架**。它的核心特点是基于**图结构（Graph）**来编排 AI 应用，而不是传统的链式结构。

可以这样理解：

- **LangChain**：线性流程，像流水线一样顺序执行
- **LangGraph**：图状流程，可以有顺序，循环、分支、状态回溯，更像程序流程图

**LangGraph 是专为构建多智能体（Multi-Agent）系统而设计的架构框架**。它将复杂的协作流程定义为一张**有向状态图（StateGraph）**，每个智能体或功能模块都是图中的一个节点，通过“边”来定义它们之间的流转和交互逻辑

## （二）LangGraph vs LangChain 核心差异

| 维度           | LangChain                 | LangGraph                |
| -------------- | ------------------------- | ------------------------ |
| **工作流结构** | 线性链（Chain）           | 图结构（Graph）          |
| **循环支持**   | 不支持                    | 原生支持循环             |
| **状态管理**   | 依赖外部                  | 内置状态图（StateGraph） |
| **控制粒度**   | 高层抽象，较简单          | 精细控制每个节点和边     |
| **适用场景**   | 问答、RAG、摘要，单智能体 | 复杂 Agent、多智能体协作 |

- **LangChain 是"基础"**：它为 LangGraph 提供了所有基础组件。比如，你在 LangGraph 的节点（Node）里调用的 `ChatModel`、`Tool`，以及记忆模块，几乎都来自 LangChain。可以理解为，LangGraph 运行在 LangChain 提供的"物料"之上。
- **LangGraph 是"进阶"**：当你的应用逻辑超出简单的链式调用，需要一个更强大、更可控的"骨架"来承载复杂流程时，LangGraph 就是最佳选择。
- **相比直接使用 LangChain Agent，LangGraph 确实更容易控制 Token 消耗**，但并不是 LangGraph 本身能减少 Token，而是因为它提供了更精细的流程控制能力。

## （三）设计原理

它的核心模型可以概括为三个要素：

- **State（共享状态）**：这是多智能体协作的“共享白板”，存储了任务信息、中间结果和对话历史等。所有智能体（节点）都能读取和修改这个状态，实现了信息的透明传递。
- **Node（节点）**：每个节点代表一个独立的功能单元。它既可以是一个拥有特定工具的专业智能体（如“研究员”或“程序员”），也可以是一个简单的函数或一次大模型调用
- **Edge（边）**：定义了节点之间的流转路径。LangGraph 支持**条件边（Conditional Edge）**，这意味着系统可以根据当前状态（State）的结果，动态决定“下一步该执行哪个智能体”，这是实现复杂决策和路由的关键

## （四）环境安装

```
pip install -U langgraph
```

## （五）核心组件

### 1. 总体介绍

```python
用户输入
   ↓
State（数据）
   ↓
Node（处理）
   ↓
Edge（决策）
   ↓
下一Node or 结束
```

LangGraph = **数据在节点之间流动 + 流程被你控制**

### 2. State（状态）

State 是一个在整个流程中流动的**数据结构**（通常是一个 Python 字典或 TypedDict）

作用：它就像团队项目中的共享文档或背包。

- 用户输入的内容会放进去。
- 每一个节点（Node）处理完后，都会把结果（比如提取出的姓名、查到的邮箱、发送结果）**更新**进这个 State 里。
- 下一个节点读取时，拿到的就是包含了之前所有处理结果的 State。

### 3. Node（节点）

Node 是执行具体任务的**函数**

作用：它是实际干活的地方

- 它可以调用大模型（LLM）进行意图识别。
- 它可以调用工具（Tool）去查询数据库。
- 它可以执行具体的业务逻辑（比如发送邮件）。

输入与输出：

- **输入**：接收当前的 State。
- **输出**：返回一个字典，用来**更新** State。

### 4. Edge（边）

Edge 定义了节点之间的**流转路径**。它决定了程序下一步该去哪里

分类：

- **普通边 (Normal Edge)**：也就是“单行道”。比如 A 做完必须做 B。
- **条件边 (Conditional Edge)**：也就是“分岔路口”。这是 LangGraph 最强大的地方。它根据 State 里的数据（比如 `next_step` 的值）来决定是去“发送邮件”，还是直接“结束流程”。

# 二、顺序图

## （一）状态

`EmailState` 类就像一个“数据模型”或“蓝图”，它规定了整个智能体（Agent）可以拥有哪些数据字段（如 `messages`, `name`, `subject` 等）

```python
from typing_extensions import TypedDict, Annotated
from langchain.messages import AnyMessage
import operator

"""
邮件状态节点
"""
# 类的属性要求定义为字典类型
class EmailState(TypedDict):
    print("\n这里是email_state01.py")
    # 消息
    messages:Annotated[list[AnyMessage],operator.add]
    # 用户名
    name:str
    # 邮件
    email:str
    # 主题
    subject:str
    # 内容
    content:str
    # 结果回复，可选
    result:str
```

## （二）主程序

```python
from langchain_core.messages import HumanMessage
from langGraph_demo.demo01.graph.email_agent01 import email_agent

import asyncio
async def test01():
    print(f"\n【测试】这里是01-测试顺序图.py")
    graph = email_agent()
    print(f"\n【测试】这里是01-测试顺序图.py")
    print(f"【测试】获取邮件智能体结果：{graph}")
    input = {"messages":[HumanMessage(content="给year发送一封邮件，通知开学了")]}
    async for chunk,metadate in graph.astream(input, stream_mode="messages"):
        yield chunk.content

# 画流程图
def draw_graph():
    agent = email_agent()
    # 画图
    data = agent.get_graph().draw_mermaid_png()
    # 展示流程图
    with open("顺序图.png","wb") as f:
        f.write(data)

if __name__ == '__main__':
    # draw_graph()
    async def test():
        print("*-*-"*40)
        async for rs in test01():
            print(rs,end="")
    asyncio.run(test())
```

## （三）大脑或智能体

```python
from langgraph.graph import StateGraph, START, END
from langGraph_demo.demo01.state.email_state01 import EmailState
from langGraph_demo.demo01.node.email_node01 import email_node
from langGraph_demo.demo01.node.query_node01 import query_node
from langGraph_demo.demo01.node.internet_node01 import internet_node

"""
创建一个大脑或智能体
"""

def email_agent():
    print("\n【测试】这里是email_agent01.py")
    # 获取图形结果
    graph = StateGraph(EmailState)
    print(f"【测试】获取图形结果：{graph}")
    # 顺序图添加
    print("【测试】意图识别节点")
    graph.add_node("internet",internet_node)
    print("【测试】查询节点")
    graph.add_node("query",query_node)
    print("【测试】邮件节点")
    graph.add_node("email",email_node)
    # 画边
    # 新版入口
    print("【测试】开始 --》意图识别")
    graph.add_edge(START,"internet")
    # 旧版入口
    # graph.set_entry_("internet")
    print("【测试】意图识别 --》查询")
    graph.add_edge("internet", "query")
    print("【测试】查询 --》邮件")
    graph.add_edge("query", "email")
    print("【测试】邮件 --》结束")
    graph.add_edge("email", END)
    # 编译
    agent = graph.compile(debug=True)
    print(f"【测试】编译结果：{agent}")
    return agent
```

## （四）意图识别节点

`internet_node` 函数返回的字典，其作用就是**更新**由 `EmailState` 定义的全局状态

当 `internet_node` 返回 `{"messages": [...], "name": "...", ...}` 时，Lang Graph 框架会自动将这个字典里的内容**合并（merge）**到当前的全局状态中。

- `messages` 列表会追加新的 `AIMessage`。
- `name`, `subject`, `content` 等字段会被创建或更新。

```python
from langGraph_demo.demo01.state.email_state01 import EmailState
from pydantic import BaseModel,Field
from langchain.agents import create_agent
from model.my_model import MyModel
from langchain_core.messages import AIMessage

# 响应参数
class InternetResponse(BaseModel):
    name:str = Field(...,description="姓名")
    subject:str = Field(...,description="邮件主题")
    content:str = Field(...,description="邮件内容")

"""
意图识别节点，返回值必须为字典
"""

def internet_node(state:EmailState):
    print("\n【测试】这里是internet_node01.py")
    print(f"【测试】接收到的state：{state}")
    model = MyModel.get_local_model()
    prompt = """
        -- 角色：你是一个意图识别助手
        -- 任务：
            - 理解用户需求
            - 根据用户问题，提取姓名，邮件主题，邮件内容
        -- 规则：
            - 姓名、邮件主题、邮件内容不能为空
        -- 输出：
            - 输出以下内容：{"name":"xx","subject":"xx","content":"xx"}
        -- 示例：
            - 用户问题：发送邮件给张三，主题是测试，内容是测试邮件内容
            - 输出：{"name":"张三","subject":"测试","content":"测试邮件内容"}
    """
    agent = create_agent(
        model = model,
        tools=[],
        system_prompt=prompt,
        middleware=[],
        response_format=InternetResponse,
    )
    msg = {"messages":[{"role":"user","content":state["messages"][0].content}]}
    # 获取结果
    rs = agent.invoke(msg)
    print(f"【测试】大模型回复结果：{rs}")
    # 把结果转换成字典
    json = rs["structured_response"].model_dump()
    print(f"【测试】将回结果转为字典类型：{json}")
    # 定义AI返回的内容
    ai_msg = f"\n意图节点识别成功：\n 姓名：{json['name']}\n 邮件主题：{json['subject']}\n 邮件内容：{json['content']}"
    # 只返回当前节点修改的状态信息
    return {
        "messages":[AIMessage(content=ai_msg)],
        "name":json["name"],
        "subject":json["subject"],
        "content":json["content"],
        "result":"意图识别成功"
    }
```

打印信息

```
意图节点识别成功：
 姓名：year
 邮件主题：开学通知
 邮件内容：通知开学了
```

触发时机：

主程序中设置了 `stream_mode="messages"`。这个模式的含义是：“**每当状态中的 `messages` 字段有新消息加入时，就立刻把这个消息 yield（产出）出来**”

当 `internet_node` 执行完毕，返回的 `AIMessage` 被添加到 `messages` 状态后，`graph.astream` 就立即捕获到了这个新消息，并将其传递给 `async for` 循环，最终由 `print(rs, end="")` 打印到控制台

## （五）查询邮箱节点

```python
from langGraph_demo.demo01.state.email_state01 import EmailState
from tool.query_employee_tool import QueryEmployeeTool
from langchain_core.messages import ToolMessage
import ast

def query_node(state:EmailState):
    print("\n【测试】这里是query_node01.py")
    # 获取用户姓名
    name = state["name"]
    # 调用工具
    rs = QueryEmployeeTool.invoke({
        "sql":f"select email from employee where user_name = '{name}'"
    })
    print(f"【测试】查询数据结果：{rs}")    # [{'email': '2920242909@qq.com'}]
    print("【测试】查询数据结果数据类型：",type(rs))
    if rs=="()":
        return {
            "messages":[ToolMessage(content="用户邮箱不存在",tool_call_id="query_node")],
            "result":"用户邮箱不存在"
        }
    # 获取邮箱
    email = rs[0]['email']
    print(f"【测试】获取到的邮箱结果：{email}")
    # 定义结果
    tool_msg = f"\n查询节点成功\n邮箱为：{email}"
    return {
        "messages": [ToolMessage(content=tool_msg, tool_call_id="query_node")],
        "result": "\n用户邮箱查询成功\n",
        "email":email
    }
```

## （六）发送邮件节点

```python
from langGraph_demo.demo01.state.email_state01 import EmailState
from tool.send_email_tool import SendEmailTool
from langchain_core.messages import AIMessage

def email_node(state:EmailState):
    print("\n【测试】这里是email_node01.py")
    # 邮箱
    email = state["email"]
    # 标题
    subject = state["subject"]
    # 内容
    content = state["content"]
    # 调用邮件工具
    rs = SendEmailTool.invoke(
        {"to":email,"subject":subject,"content":content}
    )
    print(f"【测试】获得调用邮件工具结果：{rs}")
    if str(rs).strip() == "发送邮件成功":
        # 自定义最终答案，结果
        ai_msg = f"\n邮件发送成功\n"
        return {
            "messages":[AIMessage(content=ai_msg)],
            "return":"邮件发送成功"
        }
    else:
        # 自定义最终答案，结果
        ai_msg = f"\n邮件发送失败\n"
        return {
            "messages": [AIMessage(content=ai_msg)],
            "return": "邮件发送失败"
        }
```

## （七）主程序打印信息

```
D:\anaconda3\envs\agent_env\python.exe G:\GitHub\Stu_AI\StuAgent\langGraph_demo\demo01\01-测试顺序图.py 

这里是email_state01.py
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

【测试】这里是01-测试顺序图.py

【测试】这里是email_agent01.py
【测试】获取图形结果：<langgraph.graph.state.StateGraph object at 0x000002844CF83830>
【测试】意图识别节点
【测试】查询节点
【测试】邮件节点
【测试】开始 --》意图识别
【测试】意图识别 --》查询
【测试】查询 --》邮件
【测试】邮件 --》结束
【测试】编译结果：<langgraph.graph.state.CompiledStateGraph object at 0x000002844D61B470>

【测试】这里是01-测试顺序图.py
【测试】获取邮件智能体结果：<langgraph.graph.state.CompiledStateGraph object at 0x000002844D61B470>
[values] {'messages': [HumanMessage(content='给year发送一封邮件，通知开学了', additional_kwargs={}, response_metadata={})]}

【测试】这里是internet_node01.py
【测试】接收到的state：{'messages': [HumanMessage(content='给year发送一封邮件，通知开学了', additional_kwargs={}, response_metadata={})]}
【测试】大模型回复结果：{'messages': [HumanMessage(content='给year发送一封邮件，通知开学了', additional_kwargs={}, response_metadata={}, id='7745f07e-8457-43e1-a5f2-0fdbfaaef266'), AIMessage(content='', additional_kwargs={}, response_metadata={'finish_reason': 'stop', 'model_name': 'qwen2.5:7b', 'system_fingerprint': 'fp_ollama', 'model_provider': 'openai'}, id='lc_run--01a08a40-525a-7e51-9195-fe45d31529c9', tool_calls=[], invalid_tool_calls=[]), AIMessage(content='', additional_kwargs={}, response_metadata={'finish_reason': 'stop', 'model_name': 'qwen2.5:7b', 'system_fingerprint': 'fp_ollama', 'model_provider': 'openai'}, id='lc_run--01a08a40-8b78-7852-9572-95eec9a01687', tool_calls=[], invalid_tool_calls=[]), AIMessage(content='', additional_kwargs={}, response_metadata={'finish_reason': 'tool_calls', 'model_name': 'qwen2.5:7b', 'system_fingerprint': 'fp_ollama', 'model_provider': 'openai'}, id='lc_run--01a08a40-9c34-72d3-958e-c1d8fb836d11', tool_calls=[{'name': 'InternetResponse', 'args': {'name': 'year', 'subject': '开学通知', 'content': '新的学期已经开始了，请大家注意查收相关通知和准备新学期的学习工作。'}, 'id': 'call_nyu7sgui', 'type': 'tool_call'}], invalid_tool_calls=[]), ToolMessage(content="Returning structured response: name='year' subject='开学通知' content='新的学期已经开始了，请大家注意查收相关通知和准备新学期的学习工作。'", name='InternetResponse', id='15884b5c-196e-4f83-8ea9-f59d7427a3a9', tool_call_id='call_nyu7sgui')], 'structured_response': InternetResponse(name='year', subject='开学通知', content='新的学期已经开始了，请大家注意查收相关通知和准备新学期的学习工作。')}
【测试】将回结果转为字典类型：{'name': 'year', 'subject': '开学通知', 'content': '新的学期已经开始了，请大家注意查收相关通知和准备新学期的学习工作。'}

意图节点识别成功：
 姓名：year
 邮件主题：开学通知
 邮件内容：新的学期已经开始了，请大家注意查收相关通知和准备新学期的学习工作。
[updates] {'internet': {'messages': [AIMessage(content='\n意图节点识别成功：\n 姓名：year\n 邮件主题：开学通知\n 邮件内容：新的学期已经开始了，请大家注意查收相关通知和准备新学期的学习工作。', additional_kwargs={}, response_metadata={}, id='db1b325c-790a-47ad-a319-e6f9f8090405', tool_calls=[], invalid_tool_calls=[])], 'name': 'year', 'subject': '开学通知', 'content': '新的学期已经开始了，请大家注意查收相关通知和准备新学期的学习工作。', 'result': '意图识别成功'}}
[values] {'messages': [HumanMessage(content='给year发送一封邮件，通知开学了', additional_kwargs={}, response_metadata={}), AIMessage(content='\n意图节点识别成功：\n 姓名：year\n 邮件主题：开学通知\n 邮件内容：新的学期已经开始了，请大家注意查收相关通知和准备新学期的学习工作。', additional_kwargs={}, response_metadata={}, id='db1b325c-790a-47ad-a319-e6f9f8090405', tool_calls=[], invalid_tool_calls=[])], 'name': 'year', 'subject': '开学通知', 'content': '新的学期已经开始了，请大家注意查收相关通知和准备新学期的学习工作。', 'result': '意图识别成功'}

【测试】这里是query_node01.py
生成的sql语句：select email from employee where user_name = 'year'
【测试】查询数据结果：[{'email': '2920242909@qq.com'}]
【测试】查询数据结果数据类型： <class 'list'>
【测试】获取到的邮箱结果：2920242909@qq.com

查询节点成功
邮箱为：2920242909@qq.com
[updates] {'query': {'messages': [ToolMessage(content='\n查询节点成功\n邮箱为：2920242909@qq.com', id='fe511b89-78b0-4772-acfc-9e332db2b1a8', tool_call_id='query_node')], 'result': '\n用户邮箱查询成功\n', 'email': '2920242909@qq.com'}}
[values] {'messages': [HumanMessage(content='给year发送一封邮件，通知开学了', additional_kwargs={}, response_metadata={}), AIMessage(content='\n意图节点识别成功：\n 姓名：year\n 邮件主题：开学通知\n 邮件内容：新的学期已经开始了，请大家注意查收相关通知和准备新学期的学习工作。', additional_kwargs={}, response_metadata={}, id='db1b325c-790a-47ad-a319-e6f9f8090405', tool_calls=[], invalid_tool_calls=[]), ToolMessage(content='\n查询节点成功\n邮箱为：2920242909@qq.com', id='fe511b89-78b0-4772-acfc-9e332db2b1a8', tool_call_id='query_node')], 'name': 'year', 'email': '2920242909@qq.com', 'subject': '开学通知', 'content': '新的学期已经开始了，请大家注意查收相关通知和准备新学期的学习工作。', 'result': '\n用户邮箱查询成功\n'}

【测试】这里是email_node01.py
【测试】获得调用邮件工具结果：发送邮件成功


邮件发送成功
[updates] {'email': {'messages': [AIMessage(content='\n邮件发送成功\n', additional_kwargs={}, response_metadata={}, id='1be5f4ae-3cac-4337-93c8-1ff5026c6dbf', tool_calls=[], invalid_tool_calls=[])]}}
[values] {'messages': [HumanMessage(content='给year发送一封邮件，通知开学了', additional_kwargs={}, response_metadata={}), AIMessage(content='\n意图节点识别成功：\n 姓名：year\n 邮件主题：开学通知\n 邮件内容：新的学期已经开始了，请大家注意查收相关通知和准备新学期的学习工作。', additional_kwargs={}, response_metadata={}, id='db1b325c-790a-47ad-a319-e6f9f8090405', tool_calls=[], invalid_tool_calls=[]), ToolMessage(content='\n查询节点成功\n邮箱为：2920242909@qq.com', id='fe511b89-78b0-4772-acfc-9e332db2b1a8', tool_call_id='query_node'), AIMessage(content='\n邮件发送成功\n', additional_kwargs={}, response_metadata={}, id='1be5f4ae-3cac-4337-93c8-1ff5026c6dbf', tool_calls=[], invalid_tool_calls=[])], 'name': 'year', 'email': '2920242909@qq.com', 'subject': '开学通知', 'content': '新的学期已经开始了，请大家注意查收相关通知和准备新学期的学习工作。', 'result': '\n用户邮箱查询成功\n'}

Process finished with exit code 0
```

# 三、条件图

## （一）状态

```python
from typing_extensions import TypedDict, Annotated
from langchain.messages import AnyMessage
import operator

# 类的属性要求定义为字典类型
class EmailState(TypedDict):
    print("\n【测试】这里是email_state02.py")
    # 消息
    messages:Annotated[list[AnyMessage],operator.add]
    # 用户名
    name:str
    # 邮件
    email:str
    # 主题
    subject:str
    # 内容
    content:str
    # 结果回复，可选
    result:str

    # 下一步操作：条件判断
    next_step:str
```

## （二）主程序

```python
from langchain_core.messages import HumanMessage
from langGraph_demo.demo02.graph.email_agent02 import email_agent

import asyncio
async def test02():
    print(f"\n【测试】这里是02-测试顺序图.py")
    graph = email_agent()
    print(f"\n【测试】这里是02-测试顺序图.py")
    print(f"【测试】获取邮件智能体结果：{graph}")
    input = {"messages":[HumanMessage(content="给year发送一封邮件，通知开学了")]}
    async for chunk,metadate in graph.astream(input, stream_mode="messages"):
        yield chunk.content

# 画流程图
def draw_graph():
    agent = email_agent()
    # 画图
    data = agent.get_graph().draw_mermaid_png()
    # 展示流程图
    with open("条件图.png","wb") as f:
        f.write(data)

if __name__ == '__main__':
    # draw_graph()
    async def test():
        print("*-*-"*40)
        async for rs in test02():
            print(rs,end="")
    asyncio.run(test())
```

## （三）大脑或智能体

```python
from langgraph.graph import StateGraph, START, END
from langGraph_demo.demo02.state.email_state02 import EmailState
from langGraph_demo.demo02.node.email_node02 import email_node
from langGraph_demo.demo02.node.query_node02 import query_node
from langGraph_demo.demo02.node.internet_node02 import internet_node
from langGraph_demo.demo02.node.condiyion_node02 import query_router

def email_agent():
    print("\n【测试】这里是email_agent02.py")
    # 获取图形结果
    graph = StateGraph(EmailState)
    print(f"【测试】获取图形结果：{graph}")
    # 顺序图添加
    print("【测试】意图识别节点")
    graph.add_node("internet",internet_node)
    print("【测试】查询节点")
    graph.add_node("query",query_node)
    print("【测试】邮件节点")
    graph.add_node("email",email_node)
    # 画边
    # 新版入口
    print("【测试】开始 --》意图识别")
    graph.add_edge(START,"internet")
    # 旧版入口
    # graph.set_entry_point("internet")
    print("【测试】意图识别 --》查询")
    graph.add_edge("internet", "query")

    # 添加条件边
    print("【测试】查询 --》结束")
    graph.add_conditional_edges("query",query_router,{"a":"email","b":END})

    # 编译
    agent = graph.compile(debug=True)
    print(f"【测试】编译结果：{agent}")
    return agent
```

## （四）意图识别节点

返回值必须为字典

```python
from langGraph_demo.demo02.state.email_state02 import EmailState
from pydantic import BaseModel,Field
from langchain.agents import create_agent
from model.my_model import MyModel
from langchain_core.messages import AIMessage

# 响应参数
class InternetResponse(BaseModel):
    name:str = Field(...,description="姓名")
    subject:str = Field(...,description="邮件主题")
    content:str = Field(...,description="邮件内容")

def internet_node(state:EmailState):
    print("\n【测试】这里是internet_node02.py")
    print(f"【测试】接收到的state：{state}")
    model = MyModel.get_local_model()
    prompt = """
        -- 角色：你是一个意图识别助手
        -- 任务：
            - 理解用户需求
            - 根据用户问题，提取姓名，邮件主题，邮件内容
        -- 规则：
            - 姓名、邮件主题、邮件内容不能为空
        -- 输出：
            - 输出以下内容：{"name":"xx","subject":"xx","content":"xx"}
        -- 示例：
            - 用户问题：发送邮件给张三，主题是测试，内容是测试邮件内容
            - 输出：{"name":"张三","subject":"测试","content":"测试邮件内容"}
    """
    agent = create_agent(
        model = model,
        tools=[],
        system_prompt=prompt,
        middleware=[],
        response_format=InternetResponse,
    )
    msg = {"messages":[{"role":"user","content":state["messages"][0].content}]}
    # 获取结果
    rs = agent.invoke(msg)
    print(f"【测试】大模型回复结果：{rs}")
    # 把结果转换成字典
    json = rs["structured_response"].model_dump()
    print(f"【测试】将回结果转为字典类型：{json}")
    # 定义AI返回的内容
    ai_msg = f"\n意图节点识别成功：\n 姓名：{json['name']}\n 邮件主题：{json['subject']}\n 邮件内容：{json['content']}"
    # 只返回当前节点修改的状态信息
    return {
        "messages":[AIMessage(content=ai_msg)],
        "name":json["name"],
        "subject":json["subject"],
        "content":json["content"],
        "result":"意图识别成功"
    }
```

## （五）查询邮箱节点

```python
from langGraph_demo.demo02.state.email_state02 import EmailState
from tool.query_employee_tool import QueryEmployeeTool
from langchain_core.messages import ToolMessage

def query_node(state:EmailState):
    print("\n【测试】这里是query_node02.py")
    # 获取用户姓名
    name = state["name"]
    # 调用工具
    rs = QueryEmployeeTool.invoke({
        "sql":f"select email from employee where user_name = '{name}'"
    })
    print(f"【测试】查询数据结果：{rs}")    # [{'email': '2920242909@qq.com'}]
    print("【测试】查询数据结果数据类型：",type(rs))
    if rs==():
        return {
            "messages":[ToolMessage(content="用户邮箱不存在",tool_call_id="query_node")],
            "result":"用户邮箱不存在",
            "next_step":"end"   # 标识结束了
        }
    # 获取邮箱
    email = rs[0]['email']
    print(f"【测试】获取到的邮箱结果：{email}")
    # 定义结果
    tool_msg = f"\n查询节点成功\n邮箱为：{email}"
    return {
        "messages": [ToolMessage(content=tool_msg, tool_call_id="query_node")],
        "result": "\n用户邮箱查询成功\n",
        "email":email,
        "next_step":"email"     # 标识下一步走邮箱节点
    }
```

## （六）条件分支节点

```python
from langGraph_demo.demo02.state.email_state02 import EmailState

# 定义query节点条件路由函数
def query_router(state:EmailState):
    print("\n【测试】这里是condiyion_node02.py")
    data = state['next_step']
    if data == "email":
        return "a"
    else:
        return "b"
```

## （七）发送邮件节点

```python
from langGraph_demo.demo02.state.email_state02 import EmailState
from tool.send_email_tool import SendEmailTool
from langchain_core.messages import AIMessage

def email_node(state:EmailState):
    print("\n【测试】这里是email_node02.py")
    # 邮箱
    email = state["email"]
    # 标题
    subject = state["subject"]
    # 内容
    content = state["content"]
    # 调用邮件工具
    rs = SendEmailTool.invoke(
        {"to":email,"subject":subject,"content":content}
    )
    print(f"【测试】获得调用邮件工具结果：{rs}")
    if str(rs).strip() == "发送邮件成功":
        # 自定义最终答案，结果
        ai_msg = f"\n邮件发送成功\n"
        return {
            "messages":[AIMessage(content=ai_msg)],
            "return":"邮件发送成功"
        }
    else:
        # 自定义最终答案，结果
        ai_msg = f"\n邮件发送失败\n"
        return {
            "messages": [AIMessage(content=ai_msg)],
            "return": "邮件发送失败"
        }
```

## （八）主程序打印信息

```
D:\anaconda3\envs\agent_env\python.exe G:\GitHub\Stu_AI\StuAgent\langGraph_demo\demo02\02-测试顺序图.py 

【测试】这里是email_state02.py
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

【测试】这里是02-测试顺序图.py

【测试】这里是email_agent02.py
【测试】获取图形结果：<langgraph.graph.state.StateGraph object at 0x00000226511C3680>
【测试】意图识别节点
【测试】查询节点
【测试】邮件节点
【测试】开始 --》意图识别
【测试】意图识别 --》查询
【测试】查询 --》结束
【测试】编译结果：<langgraph.graph.state.CompiledStateGraph object at 0x0000022650AC9670>

【测试】这里是02-测试顺序图.py
【测试】获取邮件智能体结果：<langgraph.graph.state.CompiledStateGraph object at 0x0000022650AC9670>
[values] {'messages': [HumanMessage(content='给yea发送一封邮件，通知开学了', additional_kwargs={}, response_metadata={})]}

【测试】这里是internet_node02.py
【测试】接收到的state：{'messages': [HumanMessage(content='给yea发送一封邮件，通知开学了', additional_kwargs={}, response_metadata={})]}
【测试】大模型回复结果：{'messages': [HumanMessage(content='给yea发送一封邮件，通知开学了', additional_kwargs={}, response_metadata={}, id='cecb9087-9c5c-4cd3-a946-152298e911e4'), AIMessage(content='', additional_kwargs={}, response_metadata={'finish_reason': 'stop', 'model_name': 'qwen2.5:7b', 'system_fingerprint': 'fp_ollama', 'model_provider': 'openai'}, id='lc_run--01a08a54-a06f-79e1-af21-89b9e364dc46', tool_calls=[], invalid_tool_calls=[]), AIMessage(content='', additional_kwargs={}, response_metadata={'finish_reason': 'stop', 'model_name': 'qwen2.5:7b', 'system_fingerprint': 'fp_ollama', 'model_provider': 'openai'}, id='lc_run--01a08a54-afea-7ec0-96fd-8edf36cd450c', tool_calls=[], invalid_tool_calls=[]), AIMessage(content='', additional_kwargs={}, response_metadata={'finish_reason': 'tool_calls', 'model_name': 'qwen2.5:7b', 'system_fingerprint': 'fp_ollama', 'model_provider': 'openai'}, id='lc_run--01a08a54-bf23-7e32-92c9-ff8d1616cce9', tool_calls=[{'name': 'InternetResponse', 'args': {'name': 'yea', 'subject': '开学通知', 'content': '各位同学，新学期已经开始，请大家做好准备'}, 'id': 'call_1549943v', 'type': 'tool_call'}], invalid_tool_calls=[]), ToolMessage(content="Returning structured response: name='yea' subject='开学通知' content='各位同学，新学期已经开始，请大家做好准备'", name='InternetResponse', id='584120f7-a2b6-4f91-8083-c934ef9d8490', tool_call_id='call_1549943v')], 'structured_response': InternetResponse(name='yea', subject='开学通知', content='各位同学，新学期已经开始，请大家做好准备')}
【测试】将回结果转为字典类型：{'name': 'yea', 'subject': '开学通知', 'content': '各位同学，新学期已经开始，请大家做好准备'}

意图节点识别成功：
 姓名：yea
 邮件主题：开学通知
 邮件内容：各位同学，新学期已经开始，请大家做好准备
 [updates] {'internet': {'messages': [AIMessage(content='\n意图节点识别成功：\n 姓名：yea\n 邮件主题：开学通知\n 邮件内容：各位同学，新学期已经开始，请大家做好准备', additional_kwargs={}, response_metadata={}, id='0c859f3b-0952-4f54-9794-506e92c32422', tool_calls=[], invalid_tool_calls=[])], 'name': 'yea', 'subject': '开学通知', 'content': '各位同学，新学期已经开始，请大家做好准备', 'result': '意图识别成功'}}
[values] {'messages': [HumanMessage(content='给yea发送一封邮件，通知开学了', additional_kwargs={}, response_metadata={}), AIMessage(content='\n意图节点识别成功：\n 姓名：yea\n 邮件主题：开学通知\n 邮件内容：各位同学，新学期已经开始，请大家做好准备', additional_kwargs={}, response_metadata={}, id='0c859f3b-0952-4f54-9794-506e92c32422', tool_calls=[], invalid_tool_calls=[])], 'name': 'yea', 'subject': '开学通知', 'content': '各位同学，新学期已经开始，请大家做好准备', 'result': '意图识别成功'}

【测试】这里是query_node02.py
生成的sql语句：select email from employee where user_name = 'yea'
【测试】查询数据结果：()
【测试】查询数据结果数据类型： <class 'tuple'>

【测试】这里是condiyion_node02.py
用户邮箱不存在
[updates] {'query': {'messages': [ToolMessage(content='用户邮箱不存在', id='d9149116-2de4-4346-94ea-0d98f4f24900', tool_call_id='query_node')], 'result': '用户邮箱不存在', 'next_step': 'end'}}
[values] {'messages': [HumanMessage(content='给yea发送一封邮件，通知开学了', additional_kwargs={}, response_metadata={}), AIMessage(content='\n意图节点识别成功：\n 姓名：yea\n 邮件主题：开学通知\n 邮件内容：各位同学，新学期已经开始，请大家做好准备', additional_kwargs={}, response_metadata={}, id='0c859f3b-0952-4f54-9794-506e92c32422', tool_calls=[], invalid_tool_calls=[]), ToolMessage(content='用户邮箱不存在', id='d9149116-2de4-4346-94ea-0d98f4f24900', tool_call_id='query_node')], 'name': 'yea', 'subject': '开学通知', 'content': '各位同学，新学期已经开始，请大家做好准备', 'result': '用户邮箱不存在', 'next_step': 'end'}

Process finished with exit code 0
```

# 四、循环图

## （一）状态

```python
from typing_extensions import TypedDict, Annotated
from langchain.messages import AnyMessage
import operator

# 类的属性要求定义为字典类型
class EmailState(TypedDict):
    print("\n【测试】这里是email_state03.py")
    # 消息
    messages:Annotated[list[AnyMessage],operator.add]
    # 用户名
    name:str
    # 邮件
    email:str
    # 主题
    subject:str
    # 内容
    content:str
    # 结果回复，可选
    result:str

    # 下一步操作：条件判断
    next_step:str

    # 智能体名称
    agent_name:str
    # 置信度
    confidence:float

    # 设置重试次数
    count:int
```

## （二）主程序

```python
from langchain_core.messages import HumanMessage
from langGraph_demo.demo03.graph.langGraph_agent03 import langGraph_agent

import asyncio
async def test():
    print(f"\n【测试】这里是 -- 03-测试循环图.py")
    graph = langGraph_agent()
    print(f"\n【测试】这里是 -- 03-测试循环图.py")
    # print(f"【测试】获取路由智能体结果：{graph}")
    # input = {"messages":[HumanMessage(content="你好，什么是python")]}
    input = {"messages": [HumanMessage(content="给year发送邮件，通知她放学了")],"count":0}
    async for chunk,metadate in graph.astream(input, stream_mode="messages"):
        yield chunk.content


# 画流程图
def draw_graph():
    agent = langGraph_agent()
    # 画图
    data = agent.get_graph().draw_mermaid_png()
    # 展示流程图
    with open("循环图.png","wb") as f:
        f.write(data)

if __name__ == '__main__':
    # draw_graph()
    async def t():
        print("*-*-"*40)
        async for rs in test():
            print(rs,end="")
    asyncio.run(t())
```

## （三）大脑或智能体

```python
from langgraph.graph import StateGraph, START, END
from langGraph_demo.demo03.state.email_state03 import EmailState
from langGraph_demo.demo03.node.email_node03 import email_node
from langGraph_demo.demo03.node.query_node03 import query_node
from langGraph_demo.demo03.node.routeAgent_node03 import routeAgent_node
from langGraph_demo.demo03.node.condiyion_node03 import query_router,agent_router,query_for_router
from langGraph_demo.demo03.node.chat_node03 import chat_node
from langGraph_demo.demo03.node.internet_node03 import internet_node

def langGraph_agent():
    print("\n【测试】这里是langGraph_agent03.py")

    # 获取图形结果 -- 创建一个空的“流程图”骨架，并规定了这个流程图中所有节点必须遵守的“数据规范”
    graph = StateGraph(EmailState)
    # print(f"【测试】获取图形结果：{graph}")

    # 顺序图添加
    # print("【测试】路由智能体节点")
    graph.add_node("routeAgent",routeAgent_node)
    # print("【测试】聊天节点")
    graph.add_node("chat", chat_node)
    # print("【测试】意图识别节点")
    graph.add_node("internet", internet_node)
    # print("【测试】查询节点")
    graph.add_node("query",query_node)
    # print("【测试】邮件节点")
    graph.add_node("email",email_node)

    # 画边
    # print("【测试】开始 --》路由智能体")
    graph.add_edge(START,"routeAgent")

    # 智能体判断普通聊天还是发邮件
    # print("【测试】routeAgent --》聊天/意图识别")
    graph.add_conditional_edges("routeAgent", agent_router, {"chat":"chat","internet":"internet"})

    # 普通聊天
    # print("【测试】聊天 --》结束")
    graph.add_edge("chat", END)

    # 发邮件 -- 查询邮箱
    # print("【测试】意图识别 --》查询")
    graph.add_edge("internet", "query")
    # # print("【测试】查询 --》结束/邮件")
    # graph.add_conditional_edges("query",query_router,{"email":"email","end":END})

    # 添加循环边
    graph.add_conditional_edges("query",query_for_router,{"email":"email","i":"internet","end":END})

    # print("【测试】邮件 --》结束")
    graph.add_edge("email", END)

    # 编译
    agent = graph.compile()
    # print(f"【测试】编译结果：{agent}")
    return agent
```

## （四）路由节点

```python
from langchain.agents import create_agent
from langchain_core.messages import AIMessage,HumanMessage
from model import my_model
from langGraph_demo.demo03.state.email_state03 import EmailState
import json

# 创建大模型
model = my_model.MyModel.get_local_model()

# 创建提示词
prompt = """
-- 角色：
    你是一个专业的路由智能体，根据用户的输入，选择调用合适的节点，并且返回节点的名称和置信度
-- 任务：
    根据用户的输入，选择调用合适的节点，并且返回节点的名称和置信度
    只要用户提到‘发邮件’、‘通知’、‘写信’等和邮件相关的关键词，哪怕收件人写得不规范（比如只写了名字或数字），也必须强制分类为 internet 节点（或你的邮件查询节点），不要当成闲聊
-- 规则：
    节点名称必须是: chat_node, internet_node 其中一个
    执行度根据问题和智能体的匹配程度来判断，置信度必须是0.00-1.00（开区间）之间，保留2位小数
-- 输出格式:
    输出必须是 {"node":"节点名称","confidence":置信度}，不能输出其他任何解释或说明性文字
"""

# 创建工具
tools = []

# 创建智能体
agent = create_agent(
    model, tools,
    system_prompt=prompt,
    middleware=[]
)

def routeAgent_node(state:EmailState):
    print("\n【测试】这里是routeAgent_node03.py")
    # print(f"【测试】接收到的state：{state}")
    que_msg = {"messages":[{"role":"user","content":state["messages"][0].content}]}
    result = agent.invoke(que_msg)
    # print(f"【测试】大模型回复结果：{result}")
    data = result["messages"][-1].content
    # print(f"【测试】大模型回复结果data：{data}")
    json_data = json.loads(data)
    print(f"【测试】将大模型回复结果转为字典类型：{json_data}")
    # 定义AI返回的内容
    ai_msg = f"\n路由智能体意图识别成功：\n - 选择节点：{json_data['node']}\n - 置信度：{json_data['confidence']}"
    if json_data["node"] == "chat_node":
        return {
            "messages": [AIMessage(content=ai_msg)],
            "result": "路由智能体意图识别成功",
            "next_step": "chat",
            "confidence": json_data["confidence"],
            "agent_name": json_data["node"]
        }
    else:
        return {
            "messages": [AIMessage(content=ai_msg)],
            "result": "路由智能体意图识别成功",
            "next_step": "internet",
            "confidence": json_data["confidence"],
            "agent_name": json_data["node"]
        }
```

## （五）循环分支节点

```python
from langGraph_demo.demo03.state.email_state03 import EmailState

# 定义query节点条件路由函数 -- 是否能查询到邮箱
def query_router(state:EmailState):
    print("\n【测试】这里是condiyion_node03.py -- query_router")
    data = state['next_step']
    if data == "email":
        return "email"
    else:
        return "end"

# 是否发送邮件
def agent_router(state:EmailState):
    print("\n【测试】这里是condiyion_node03.py -- agent_router")
    data = state['next_step']
    if data == "chat":
        return "chat"
    else:
        return "internet"

# 查不到就重新查
def query_for_router(state:EmailState):
    print("\n【测试】这里是condiyion_node03.py -- query_for_router")
    # 获取查询结果
    query = query_router(state)
    count = state['count']
    if query == "email":
        return "email"
    else:
        if count < 3:
            return "i"
        else:
            return "end"
```

## （六）聊天节点

```python
from langGraph_demo.demo03.state.email_state03 import EmailState
from langchain_core.messages import AIMessage,HumanMessage
from langchain.agents import create_agent
from model import my_model


def chat_node(state:EmailState):
    print("\n\n【测试】这里是chat_node03.py\n")
    # print(f"【测试】接收到的state：{state}\n")
    prompt = """
        -- 角色：你是一个专业的聊天助手
    """
    model = my_model.MyModel.get_local_model()
    agent = create_agent(
        model = model,
        tools=[],
        system_prompt=prompt,
        middleware=[],
    )
    que_msg = {"messages": [{"role": "user", "content": state["messages"][0].content}]}
    result = agent.invoke(que_msg)
    result = result['messages'][1].content
    # print(f"【测试】大模型回复结果：{result}\n")
    return {
        "messages": [AIMessage(content=result)],
        "result": "聊天节点成功",
    }
```

## （七）意图识别节点

```python
from langGraph_demo.demo03.state.email_state03 import EmailState
from pydantic import BaseModel,Field
from langchain.agents import create_agent
from model.my_model import MyModel
from langchain_core.messages import AIMessage

# 响应参数
class InternetResponse(BaseModel):
    name:str = Field(...,description="姓名")
    subject:str = Field(...,description="邮件主题")
    content:str = Field(...,description="邮件内容")

"""
意图识别节点，返回值必须为字典
"""

def internet_node(state:EmailState):
    print("\n\n【测试】这里是internet_node03.py")
    # print(f"【测试】接收到的state：{state}")
    model = MyModel.get_local_model()
    prompt = """
        -- 角色：你是一个意图识别助手
        -- 任务：
            - 理解用户需求
            - 根据用户问题，提取姓名，邮件主题，邮件内容
        -- 规则：
            - 姓名、邮件主题、邮件内容不能为空
        -- 输出：
            - 输出以下内容：{"name":"xx","subject":"xx","content":"xx"}
        -- 示例：
            - 用户问题：发送邮件给张三，主题是测试，内容是测试邮件内容
            - 输出：{"name":"张三","subject":"测试","content":"测试邮件内容"}
    """
    agent = create_agent(
        model = model,
        tools=[],
        system_prompt=prompt,
        middleware=[],
        response_format=InternetResponse,
    )
    msg = {"messages":[{"role":"user","content":state["messages"][0].content}]}
    # 获取结果
    rs = agent.invoke(msg)
    print(f"【测试】大模型回复结果：{rs}")
    # 把结果转换成字典
    json = rs["structured_response"].model_dump()
    print(f"【测试】将回结果转为字典类型：{json}")
    # 定义AI返回的内容
    ai_msg = f"\n意图节点识别成功：\n 姓名：{json['name']}\n 邮件主题：{json['subject']}\n 邮件内容：{json['content']}"
    # 只返回当前节点修改的状态信息
    return {
        "messages":[AIMessage(content=ai_msg)],
        "name":json["name"],
        "subject":json["subject"],
        "content":json["content"],
        "result":"意图识别成功"
    }
```

## （八）查询邮箱节点

```python
from langGraph_demo.demo03.state.email_state03 import EmailState
from tool.query_employee_tool import QueryEmployeeTool
from langchain_core.messages import ToolMessage
"""
查询节点
"""

def query_node(state:EmailState):
    print("\n\n【测试】这里是query_node03.py")
    # 获取查询次数
    count = state['count']+1
    # 获取用户姓名
    name = state["name"]
    # 调用工具
    rs = QueryEmployeeTool.invoke({
        "sql":f"select email from employee where user_name = '{name}'"
    })
    print("\n【测试】这里是query_node03.py")
    # print(f"【测试】查询数据结果：{rs}")    # [{'email': '2920242909@qq.com'}]
    # print("【测试】查询数据结果数据类型：",type(rs))
    if rs == ():
        return {
            "messages":[ToolMessage(content="用户邮箱不存在",tool_call_id="query_node")],
            "result":"用户邮箱不存在",
            "next_step":"end",   # 标识结束了
            "count":count
        }
    # 获取邮箱
    email = rs[0]['email']
    print(f"【测试】获取到的邮箱结果：{email}")
    # 定义结果
    tool_msg = f"\n查询节点成功\n邮箱为：{email}"
    return {
        "messages": [ToolMessage(content=tool_msg, tool_call_id="query_node")],
        "result": "\n用户邮箱查询成功\n",
        "email":email,
        "next_step":"email",     # 标识下一步走邮箱节点
        "count":count
    }
```

## （九）发送邮件节点

```python
from langGraph_demo.demo03.state.email_state03 import EmailState
from tool.send_email_tool import SendEmailTool
from langchain_core.messages import AIMessage

def email_node(state:EmailState):
    print("\n\n【测试】这里是email_node03.py")
    # 邮箱
    email = state["email"]
    # 标题
    subject = state["subject"]
    # 内容
    content = state["content"]
    # 调用邮件工具
    rs = SendEmailTool.invoke(
        {"to":email,"subject":subject,"content":content}
    )
    print(f"【测试】获得调用邮件工具结果：{rs}")
    if str(rs).strip() == "发送邮件成功":
        # 自定义最终答案，结果
        ai_msg = f"邮件发送成功\n"
        return {
            "messages":[AIMessage(content=ai_msg)],
            "return":"邮件发送成功"
        }
    else:
        # 自定义最终答案，结果
        ai_msg = f"邮件发送失败\n"
        return {
            "messages": [AIMessage(content=ai_msg)],
            "return": "邮件发送失败"
        }
```

# 五、动态路由

## （一）状态

```python
from typing_extensions import TypedDict, Annotated
from langchain.messages import AnyMessage
import operator

# 类的属性要求定义为字典类型
class EmailState(TypedDict):
    print("\n【测试】这里是email_state04.py")
    # 消息
    messages:Annotated[list[AnyMessage],operator.add]
    # 用户名
    name:str
    # 邮件
    email:str
    # 主题
    subject:str
    # 内容
    content:str
    # 结果回复，可选
    result:str

    # 结果，可选
    result:str

    # 步骤（当前节点这步）
    step:str
```

## （二）主程序

### 1. messages 流式

```python
from langchain_core.messages import HumanMessage
from langGraph_demo.demo04.graph.langGraph_agent04 import langGraph_agent

import asyncio
async def test():
    print(f"\n【测试】这里是 -- 04-测试动态路由.py")
    graph = langGraph_agent()
    print(f"\n【测试】这里是 -- 04-测试动态路由.py")
    # print(f"【测试】获取路由智能体结果：{graph}")
    # input = {"messages":[HumanMessage(content="你好，什么是python")]}
    input = {"messages": [HumanMessage(content="给小明发送邮件，通知她放学了")]}
    async for chunk,metadate in graph.astream(input, stream_mode="messages"):
        yield chunk.content


# 画流程图
def draw_graph():
    agent = langGraph_agent()
    # 画图
    data = agent.get_graph().draw_mermaid_png()
    # 展示流程图
    with open("动态路由图.png","wb") as f:
        f.write(data)



if __name__ == '__main__':
    # draw_graph()
    async def t():
        print("*-*-"*40)
        async for rs in test():
            print(rs,end="")
    asyncio.run(t())
```

### 2. updates 流式

```python
from langchain_core.messages import HumanMessage
# from langGraph_demo.demo04.graph.langGraph_agent04 import langGraph_agent
from langGraph_demo.demo01.graph.email_agent01 import email_agent

import asyncio
async def test():
    print(f"\n【测试】这里是 -- 04-update流式.py")
    # graph = langGraph_agent()
    graph = email_agent()
    print(f"\n【测试】这里是 -- 04-update流式.py")
    # print(f"【测试】获取路由智能体结果：{graph}")
    # input = {"messages":[HumanMessage(content="你好，什么是python")]}
    input = {"messages": [HumanMessage(content="给year发送邮件，通知她放学了")]}
    async for chunk in graph.astream(input, stream_mode="updates"):
        print(f"【测试】获取流式输出结果：")
        # yield chunk
        if "internet" in chunk:
            yield f"{chunk['internet']['result']}"


# 画流程图
def draw_graph():
    # agent = langGraph_agent()
    agent = email_agent()
    # 画图
    data = agent.get_graph().draw_mermaid_png()
    # 展示流程图
    with open("动态路由图.png","wb") as f:
        f.write(data)



if __name__ == '__main__':
    # draw_graph()
    async def t():
        print("*-*-"*40)
        async for rs in test():
            print(rs,end="")
    asyncio.run(t())
```

## （三）大脑或智能体

```python
from langgraph.graph import StateGraph, START, END
from langGraph_demo.demo04.state.email_state04 import EmailState
from langGraph_demo.demo04.node.email_node04 import email_node
from langGraph_demo.demo04.node.query_node04 import query_node
from langGraph_demo.demo04.node.internet_node04 import internet_node
from langGraph_demo.demo04.node.manager_node04 import manager_node


def langGraph_agent():
    print("\n【测试】这里是langGraph_agent04.py")

    # 获取图形结果 -- 创建一个空的“流程图”骨架，并规定了这个流程图中所有节点必须遵守的“数据规范”
    graph = StateGraph(EmailState)
    # print(f"【测试】获取图形结果：{graph}")

    # 顺序图添加
    # print("【测试】意图识别节点")
    graph.add_node("internet", internet_node)
    # print("【测试】查询节点")
    graph.add_node("query",query_node)
    # print("【测试】邮件节点")
    graph.add_node("email",email_node)
    # print("【测试】主管节点")
    graph.add_node("manager", manager_node)

    # 画边
    # print("【测试】开始 --》主管")
    graph.add_edge(START, "manager")

    graph.add_edge("internet","manager")
    graph.add_edge("query", "manager")
    graph.add_edge("email", "manager")


    # 编译
    agent = graph.compile()
    # print(f"【测试】编译结果：{agent}")
    return agent
```

## （四）主管节点

```python
from langGraph_demo.demo04.state.email_state04 import EmailState
from langgraph.graph import END
from langgraph.types import Command

def manager_node(state:EmailState):
    print("\n\n【测试】这里是manager_node04.py.py")

    # 主管觉得下一步做什么 -- 获取当前步骤信息
    step = state.get("step","start")

    if step == "start":
        next_node = "internet"
    elif step == "internet_node":
        next_node = "query"
    elif step == "query_node":
        next_node = "email"
    elif step == "email_node":
        next_node = END
    else:
        next_node = END
    # 动态跳转节点
    return Command(goto=next_node)

if __name__ == '__main__':
    data = {"name":"","age":23}
    # print(f"name={data["address"]}")
    print(f"name={data.get("address", "a")}")

```

## （五）意图识别节点

```python
from langGraph_demo.demo04.state.email_state04 import EmailState
from pydantic import BaseModel,Field
from langchain.agents import create_agent
from model.my_model import MyModel
from langchain_core.messages import AIMessage

# 响应参数
class InternetResponse(BaseModel):
    name:str = Field(...,description="姓名")
    subject:str = Field(...,description="邮件主题")
    content:str = Field(...,description="邮件内容")

def internet_node(state:EmailState):
    print("\n\n【测试】这里是internet_node04.py")
    # print(f"【测试】接收到的state：{state}")
    model = MyModel.get_local_model()
    prompt = """
        -- 角色：你是一个意图识别助手
        -- 任务：
            - 理解用户需求
            - 根据用户问题，提取姓名，邮件主题，邮件内容
        -- 规则：
            - 姓名、邮件主题、邮件内容不能为空
        -- 输出：
            - 输出以下内容：{"name":"xx","subject":"xx","content":"xx"}
        -- 示例：
            - 用户问题：发送邮件给张三，主题是测试，内容是测试邮件内容
            - 输出：{"name":"张三","subject":"测试","content":"测试邮件内容"}
    """
    agent = create_agent(
        model = model,
        tools=[],
        system_prompt=prompt,
        middleware=[],
        response_format=InternetResponse,
    )
    msg = {"messages":[{"role":"user","content":state["messages"][0].content}]}
    # 获取结果
    rs = agent.invoke(msg)
    print(f"【测试】大模型回复结果：{rs}")
    # 把结果转换成字典
    json = rs["structured_response"].model_dump()
    print(f"【测试】将回结果转为字典类型：{json}")
    # 定义AI返回的内容
    ai_msg = f"\n意图节点识别成功：\n 姓名：{json['name']}\n 邮件主题：{json['subject']}\n 邮件内容：{json['content']}"
    # 只返回当前节点修改的状态信息
    return {
        "messages":[AIMessage(content=ai_msg)],
        "name":json["name"],
        "subject":json["subject"],
        "content":json["content"],
        "result":"意图识别成功",
        "step":"internet_node"
    }
```

## （六）查询邮箱节点

```python
from langGraph_demo.demo04.state.email_state04 import EmailState
from tool.query_employee_tool import QueryEmployeeTool
from langchain_core.messages import ToolMessage
"""
查询节点
"""

def query_node(state:EmailState):
    print("\n\n【测试】这里是query_node04.py")
    # 获取用户姓名
    name = state["name"]
    # 调用工具
    rs = QueryEmployeeTool.invoke({
        "sql":f"select email from employee where user_name = '{name}'"
    })
    print("\n【测试】这里是query_node04.py")
    # print(f"【测试】查询数据结果：{rs}")    # [{'email': '2920242909@qq.com'}]
    # print("【测试】查询数据结果数据类型：",type(rs))
    if rs == ():
        return {
            "messages":[ToolMessage(content="用户邮箱不存在",tool_call_id="query_node")],
            "result":"\n用户邮箱不存在\n",
            "step":"error_node"
        }
    # 获取邮箱
    email = rs[0]['email']
    print(f"【测试】获取到的邮箱结果：{email}")
    # 定义结果
    tool_msg = f"\n查询节点成功\n邮箱为：{email}"
    return {
        "messages": [ToolMessage(content=tool_msg, tool_call_id="query_node")],
        "result": "\n用户邮箱查询成功\n",
        "email":email,
        "step": "query_node"
    }
```

## （七）发送邮件节点

```python
from langGraph_demo.demo04.state.email_state04 import EmailState
from tool.send_email_tool import SendEmailTool
from langchain_core.messages import AIMessage

def email_node(state:EmailState):
    print("\n\n【测试】这里是email_node04.py")
    # 邮箱
    email = state["email"]
    # 标题
    subject = state["subject"]
    # 内容
    content = state["content"]
    # 调用邮件工具
    rs = SendEmailTool.invoke(
        {"to":email,"subject":subject,"content":content}
    )
    print(f"【测试】获得调用邮件工具结果：{rs}")
    if str(rs).strip() == "发送邮件成功":
        # 自定义最终答案，结果
        ai_msg = f"邮件发送成功\n"
        return {
            "messages":[AIMessage(content=ai_msg)],
            "return":"邮件发送成功",
            "step":"email_node"
        }
    else:
        # 自定义最终答案，结果
        ai_msg = f"邮件发送失败\n"
        return {
            "messages": [AIMessage(content=ai_msg)],
            "return": "邮件发送失败",
            "step":"error_node"
        }
```

# 六、人工审核

## （一）状态

```python
from typing_extensions import TypedDict, Annotated
from langchain.messages import AnyMessage
import operator

# 类的属性要求定义为字典类型
class EmailState(TypedDict):
    print("\n这里是email_state01.py")
    # 消息
    messages:Annotated[list[AnyMessage],operator.add]
    # 用户名
    name:str
    # 邮件
    email:str
    # 主题
    subject:str
    # 内容
    content:str
    # 结果回复，可选
    result:str
```

## （二）主程序

### 1. 人工审核

```python
from langchain_core.messages import HumanMessage
from langGraph_demo.demo01.graph.email_agent01 import email_agent
from langgraph.checkpoint.memory import InMemorySaver
import asyncio
from langgraph.types import Command

print(f"\n【测试】这里是01-测试顺序图.py")
memory = InMemorySaver()
graph = email_agent(memory)
# print(f"【测试】获取邮件智能体结果：{graph}")

# 添加记忆配置
config = {"configurable": {"thread_id": 1}}

async def test01():
    print(f"\n【测试】这里是01-测试顺序图.py")
    # print(f"【测试】获取邮件智能体结果：{graph}")
    input = {"messages":[HumanMessage(content="给year发送一封邮件，通知开学了")]}
    async for chunk,metadate in graph.astream(input, config, stream_mode="messages"):
        yield chunk.content

# 人工审核 -- 修改
def test_edit():
    async def test():
        print("修改：","*-*-" * 40)
        async for rs in test01():
            print(rs,end="")
    asyncio.run(test())
    #获取拦截的节点信息
    state = graph.get_state(config)
    print(state)
    info = input("请输入修改的邮件内容：\n")
    graph.update_state(config,{"content": info})
    #继续执行
    rs = graph.invoke(None, config)
    print(rs['messages'][-1].content)

# 人工审核-批准
def test_approve():
    async def test():
        print("批准：","*-*-" * 40)
        async for rs in test01():
            print(rs,end="")
    asyncio.run(test())
    #获取拦截的节点信息
    state = graph.get_state(config)
    print(state)
    info = input("请输入批准或者拒绝（y/n）：")
    if info =="y":
        # 继续执行
        rs = graph.invoke(None, config)
        print(rs['messages'][-1].content)
    else:
        #拒绝
        graph.invoke(Command(goto="cancel"),config)
        print("邮件发送取消")


if __name__ == '__main__':
    # test_edit()
    test_approve()
```

## （三）大脑或智能体

```python
from langgraph.graph import StateGraph, START, END
from langGraph_demo.demo01.state.email_state01 import EmailState
from langGraph_demo.demo01.node.email_node01 import email_node
from langGraph_demo.demo01.node.query_node01 import query_node
from langGraph_demo.demo01.node.internet_node01 import internet_node
from langGraph_demo.demo01.node.cancel_node import cancel_node

def email_agent(m):
    print("\n【测试】这里是email_agent01.py")
    # 获取图形结果
    graph = StateGraph(EmailState)
    # print(f"【测试】获取图形结果：{graph}")
    # 顺序图添加
    # print("【测试】意图识别节点")
    graph.add_node("internet",internet_node)
    # print("【测试】查询节点")
    graph.add_node("query",query_node)
    # print("【测试】邮件节点")
    graph.add_node("email",email_node)
    # print("【测试】取消节点")
    graph.add_node("cancel", cancel_node)
    # 画边
    # 新版入口
    # print("【测试】开始 --》意图识别")
    graph.add_edge(START,"internet")
    # 旧版入口
    # graph.set_entry_("internet")
    # print("【测试】意图识别 --》查询")
    graph.add_edge("internet", "query")
    # print("【测试】查询 --》邮件")
    graph.add_edge("query", "email")
    # print("【测试】邮件 --》结束")
    graph.add_edge("email", END)
    # print("【测试】取消 --》结束")
    graph.add_edge("cancel", END)
    # 编译 -- 在邮件节点前中断
    agent = graph.compile(
        interrupt_before=["email"],
        checkpointer=m  # 人工审核必须加入检查点
    )
    # print(f"【测试】编译结果：{agent}")
    return agent
```

## （四）意图识别节点

```python


from langGraph_demo.demo01.state.email_state01 import EmailState
from pydantic import BaseModel,Field
from langchain.agents import create_agent
from model.my_model import MyModel
from langchain_core.messages import AIMessage

# 响应参数
class InternetResponse(BaseModel):
    name:str = Field(...,description="姓名")
    subject:str = Field(...,description="邮件主题")
    content:str = Field(...,description="邮件内容")

"""
意图识别节点，返回值必须为字典
"""

def internet_node(state:EmailState):
    print("\n【测试】这里是internet_node01.py")
    # print(f"【测试】接收到的state：{state}")
    model = MyModel.get_local_model()
    prompt = """
        -- 角色：你是一个意图识别助手
        -- 任务：
            - 理解用户需求
            - 根据用户问题，提取姓名，邮件主题，邮件内容
        -- 规则：
            - 姓名、邮件主题、邮件内容不能为空
        -- 输出：
            - 输出以下内容：{"name":"xx","subject":"xx","content":"xx"}
        -- 示例：
            - 用户问题：发送邮件给张三，主题是测试，内容是测试邮件内容
            - 输出：{"name":"张三","subject":"测试","content":"测试邮件内容"}
    """
    agent = create_agent(
        model = model,
        tools=[],
        system_prompt=prompt,
        middleware=[],
        response_format=InternetResponse,
    )
    msg = {"messages":[{"role":"user","content":state["messages"][0].content}]}
    # 获取结果
    rs = agent.invoke(msg)
    # print(f"【测试】大模型回复结果：{rs}")
    # 把结果转换成字典
    json = rs["structured_response"].model_dump()
    print(f"【测试】将回结果转为字典类型：{json}")
    # 定义AI返回的内容
    ai_msg = f"\n意图节点识别成功：\n 姓名：{json['name']}\n 邮件主题：{json['subject']}\n 邮件内容：{json['content']}"
    # 只返回当前节点修改的状态信息
    return {
        "messages":[AIMessage(content=ai_msg)],
        "name":json["name"],
        "subject":json["subject"],
        "content":json["content"],
        "result":"意图识别成功"
    }
```

## （五）查询邮箱节点

```python


from langGraph_demo.demo01.state.email_state01 import EmailState
from tool.query_employee_tool import QueryEmployeeTool
from langchain_core.messages import ToolMessage
import ast
"""
查询节点
"""

def query_node(state:EmailState):
    print("\n\n【测试】这里是query_node01.py")
    # 获取用户姓名
    name = state["name"]
    # 调用工具
    rs = QueryEmployeeTool.invoke({
        "sql":f"select email from employee where user_name = '{name}'"
    })
    # print(f"【测试】查询数据结果：{rs}")    # [{'email': '2920242909@qq.com'}]
    # print("【测试】查询数据结果数据类型：",type(rs))
    if rs=="()":
        return {
            "messages":[ToolMessage(content="用户邮箱不存在",tool_call_id="query_node")],
            "result":"用户邮箱不存在"
        }
    # 获取邮箱
    email = rs[0]['email']
    print(f"【测试】获取到的邮箱结果：{email}")
    # 定义结果
    tool_msg = f"\n查询节点成功\n邮箱为：{email}"
    return {
        "messages": [ToolMessage(content=tool_msg, tool_call_id="query_node")],
        "result": "\n用户邮箱查询成功\n",
        "email":email
    }
```

## （六）发送邮件节点

```python
from langGraph_demo.demo01.state.email_state01 import EmailState
from tool.send_email_tool import SendEmailTool
from langchain_core.messages import AIMessage

def email_node(state:EmailState):
    print("\n【测试】这里是email_node01.py")
    # 邮箱
    email = state["email"]
    # 标题
    subject = state["subject"]
    # 内容
    content = state["content"]
    # 调用邮件工具
    rs = SendEmailTool.invoke(
        {"to":email,"subject":subject,"content":content}
    )
    print(f"【测试】获得调用邮件工具结果：{rs}")
    if str(rs).strip() == "发送邮件成功":
        # 自定义最终答案，结果
        ai_msg = f"\n邮件发送成功\n"
        return {
            "messages":[AIMessage(content=ai_msg)],
            "return":"邮件发送成功"
        }
    else:
        # 自定义最终答案，结果
        ai_msg = f"\n邮件发送失败\n"
        return {
            "messages": [AIMessage(content=ai_msg)],
            "return": "邮件发送失败"
        }
```

## （七）取消发送节点

```python
from langGraph_demo.demo01.state.email_state01 import EmailState

def cancel_node(state: EmailState):
    print("邮件发送已取消")
    return {}
```

