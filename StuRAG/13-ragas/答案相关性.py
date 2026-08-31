"""
    计算答案相关性：
        基于结果逆向生成问题
        然后基于生成的问题和用户输入的问题之间计算余弦相似度
        最后取平均值作为结果
"""
from openai import AsyncOpenAI
from ragas.embeddings import embedding_factory
from ragas.llms import llm_factory
from ragas.metrics.collections import AnswerRelevancy
import os

# Setup LLM
# 配置调用的模型
client = AsyncOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
# 基于配置加载模型
llm = llm_factory(
    model="qwen3.7-plus-2026-05-26",
    client=client
)

embeddings = embedding_factory(
    "openai",
    model="qwen3.7-text-embedding",
    client=client
)


# 创建指标对象
scorer = AnswerRelevancy(llm=llm, embeddings=embeddings)

# 评估
result = scorer.score(
    # 用户输入的问题
    user_input="法国在哪里，它的首都是什么？",
    # 生成的回复
    response="法国在西欧，首都是巴黎。",
)
# 输出结果
print(f"答案相关性得分: {result.value}")
