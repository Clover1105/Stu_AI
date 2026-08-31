from openai import AsyncOpenAI
from ragas.llms import llm_factory
from ragas.metrics import ContextPrecision, ContextUtilization

import os

# 有参考答案的上下文精度
def llm_context_precision_with_reference():
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
    scorer = ContextPrecision(llm=llm)

    # Evaluate
    # 评估
    result = scorer.score(
        # 用户输入的问题
        user_input="埃菲尔铁塔位于哪里?",
        # 参考答案
        reference="埃菲尔铁塔位于巴黎。",
        # 检索上下文
        retrieved_contexts=[
            "埃菲尔铁塔位于巴黎。",
            "勃兰登堡门位于柏林。"
        ]
    )

    # 输出结果
    print(f"上下文精确度得分: {result.value}")

# 无参考答案的上下文精度
def llm_context_precision_without_reference():
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
    scorer = ContextUtilization(llm=llm)

    # Evaluate
    # 评估
    result = scorer.score(
        # 用户输入的问题
        user_input="埃菲尔铁塔位于哪里?",
        # 生成结果
        response="埃菲尔铁塔位于巴黎。",
        # 检索上下文
        retrieved_contexts=[
            "埃菲尔铁塔位于巴黎。",
            "勃兰登堡门位于柏林。"
        ]
    )

    # 输出结果
    print(f"上下文精确度得分: {result.value}")



if __name__ == '__main__':
    llm_context_precision_with_reference()
    llm_context_precision_without_reference()