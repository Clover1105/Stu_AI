from openai import AsyncOpenAI
from ragas.llms import llm_factory
from ragas.metrics.collections import Faithfulness
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

# 创建指标对象
scorer = Faithfulness(llm=llm)

# 评估
result = scorer.score(
    # 用户输入的问题
    user_input="爱因斯坦在何时何地出生？",
    # 生成的回复
    response="爱因斯坦于 1879 年 3 月 10 日出生在中国。",
    # 检索到的上下文
    retrieved_contexts=[
        "阿尔伯特·爱因斯坦（生于 1879 年 3 月 14 日）是一位德国出生的理论物理学家，被广泛认为是有史以来最伟大和最有影响力的科学家之一。",
    ]
)
# 输出结果
print(f"忠诚度得分: {result.value}")
