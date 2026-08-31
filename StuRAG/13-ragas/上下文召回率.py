"""
    声明：
        通俗易懂的解释就是把生成的结果解析成多个声明【比如词】
        然后去参考答案中找到这些声明，有就有，没有就没有，然后计算结果，得到一个分数
"""
from openai import AsyncOpenAI
from ragas.llms import llm_factory
from ragas.metrics.collections import ContextRecall
import os

# Setup LLM
# 配置调用模型
client = AsyncOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
# 基于配置加载模型
llm = llm_factory(
    model="qwen3.7-max-preview",
    client=client
)

# Create metric
# 创建指标对象
scorer = ContextRecall(llm=llm)

# Evaluate
# 评估
result = scorer.score(
    # 用户输入的问题
    user_input="小明喜欢吃苹果吗？",
    # 参考答案
    reference="小明喜欢吃香蕉，小明也很喜欢吃橘子",
    # 检索到的上下文
    retrieved_contexts=[
        "小明喜欢吃苹果和香蕉。",
        "小红喜欢吃香蕉。",
    ]
)

# 输出结果
print(f"上下文召回率得分: {result.value}")