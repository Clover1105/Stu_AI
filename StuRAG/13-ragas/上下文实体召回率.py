"""
    ContextEntityRecall 指标基于 reference（参考答案）和 retrieved_contexts（检索到的上下文）中共同存在的实体数量，与仅存在于 reference 中的实体数量进行比较，从而衡量检索到的上下文的召回率。简而言之，它衡量的是从 reference 中召回了多少比例的实体。
"""
from openai import AsyncOpenAI
from ragas.llms import llm_factory
from ragas.metrics.collections import ContextEntityRecall
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
scorer = ContextEntityRecall(llm=llm)

# 评估
result = scorer.score(
    # 参考答案
    reference="泰姬陵是一座象牙白色的大理石陵墓，位于印度城市阿格拉的亚穆纳河右岸。它由莫卧儿王朝皇帝沙贾汗于1631年下令建造，用于安放其爱妻蒙塔兹·玛哈的陵墓。",
    # 检索到的上下文
    retrieved_contexts=[
        "泰姬陵是位于印度阿格拉的爱情象征和建筑奇迹。它由莫卧儿王朝皇帝沙贾汗为纪念其爱妻蒙塔兹·玛哈而建造。该建筑以其复杂的大理石工艺和周围美丽的花园而闻名。",
    ]
)
# 输出结果
print(f"上下文实体召回率得分: {result.value}")