from openai import AsyncOpenAI
from ragas.llms import llm_factory
from ragas.metrics.collections import NoiseSensitivity
import os

# 设置 LLM (大语言模型)
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

# 创建评估指标
scorer = NoiseSensitivity(llm=llm)

# 进行评估
result = scorer.ascore(
    # 用户输入的问题
    user_input="印度人寿保险公司 (LIC) 以什么闻名？",
    # 生成的答案
    response="印度人寿保险公司 (LIC) 是印度最大的保险公司，以其庞大的投资组合而闻名。LIC 为国家的金融稳定做出了贡献。",
    # 参考答案
    reference="印度人寿保险公司 (LIC) 是印度最大的保险公司，于 1956 年通过保险业国有化而成立。它以管理大型投资组合而闻名。",
    # 检索到的上下文
    retrieved_contexts=[
        "印度人寿保险公司 (LIC) 成立于 1956 年，此前印度保险业进行了国有化。",
        "LIC 是印度最大的保险公司，拥有庞大的保单持有人网络和巨额投资。",
        "作为印度最大的机构投资者，LIC 管理着大量资金，为国家的金融稳定做出了贡献。",
        "印度经济是世界上增长最快的主要经济体之一，这得益于金融、科技、制造等行业。"
    ]
)

print(f"噪声敏感度得分: {result.value}")