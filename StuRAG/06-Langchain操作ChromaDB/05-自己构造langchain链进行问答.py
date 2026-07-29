from langchain_chroma import  Chroma
from langchain_core.prompts import PromptTemplate

from Load import LoadLLM
from Load import LoadEmbeddingModel

# 查询问题
question = "珠穆朗玛峰在哪？"

"""
    问题【用户输入，客户端】 --->  目的【基于用户的问题生成回答】
    RAG 流程：
        1、让LLM如何来生成回复【提示词】
        2、提示词：需要告诉模型上下文内容是什么，问题是什么，以及生成回复时的规则
        3、为了得到上下文信息，这里需要得到向量数据库的检索器对象
        4、构造langchain链 --- 管道运算符
"""

# 创建提示词
template = """
    你是一名知识库问答助手，请结合提供的知识内容回答用户问题。
    回答要求：
        - 仅依据提供的知识内容进行回答，不补充未出现的信息。
        - 若知识内容无法回答问题，请明确说明当前知识不足，避免推测或编造。
        - 对多个知识片段进行综合分析后再作答，避免简单复制原文。
        - 回答应准确、自然、条理清晰，优先直接回答问题，再补充必要说明。
        - 相同信息无需重复描述。
        - 不要提及"根据参考资料"、"根据检索结果"、"根据上下文"等描述。
        - 若未提供任何知识内容或知识为空，请友好告知暂时无法回答，并建议用户补充信息或换个问题。
    知识内容：
        {context}
    用户问题：
        {question}
    回答：
"""

# 创建提示词对象
prompt = PromptTemplate(
    template=template,
    input_variables=["context", "question"],
)

# 创建检索器对象
vector = Chroma(
    collection_name="cs02",
    persist_directory=r"G:\GitHub\Stu_AI\StuRAG\chromadb_data",
    embedding_function=LoadEmbeddingModel.load_embedding_model()
)
retriever = vector.as_retriever(search_kwargs={"k": 3})

