# 向量化模型
from langchain_huggingface import HuggingFaceEmbeddings
# 向量数据库
from langchain_chroma import Chroma
# 模型
from langchain_openai import ChatOpenAI
# 路径
import os
# 并行执行器
from langchain_core.runnables import RunnableParallel
# 提示词
from langchain_core.prompts import PromptTemplate
# 透明传递
from langchain_core.runnables import RunnablePassthrough
# 转为字符串输出
from langchain_core.output_parsers import StrOutputParser
# 将普通函数转为转换为chain的对象
from langchain_core.runnables import  RunnableLambda
# 时间
import time

""" 项目配置 """
# ChromaDB 数据库持久化存储路径
vector_path = r"G:\GitHub\Stu_AI\StuRAG\chromadb_data"
# ChromaDB 集合名称
collection_name = "an_li01"
# Embedding 模型名称
model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
# Embedding 模型本地存储路径
model_path = r"G:\models\paraphrase-multilingual-MiniLM-L12-v2"

""" 初始化大语言模型 """
chatLLM = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen3.7-max",
)

""" 问答：使用RAG """    # 先用langchain封装的QA链实现
def yes_rag_qa(question):
    # 初始化 Embedding 模型（与创建向量数据库时保持一致）
    embedding_model = HuggingFaceEmbeddings(
        model_name=model_path,
        # 使用本地模型
        model_kwargs={
            "device": "cuda",
            "local_files_only": True,
        },
    )

    # 创建（连接）Chroma 向量数据库对象
    vector_db = Chroma(
        collection_name = collection_name,  # 集合名称
        persist_directory = vector_path,    # 数据库持久化存储路径
        embedding_function=embedding_model  # 指定模型
    )

    """02*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-02-*-*-*-*-*-*-*-*-*--*--*-*-*-*-*-*-*-*-*-*-*-*-*-02"""
    # 获取检索器
    retriever = vector_db.as_retriever(search_kwargs={"k": 2})

    # 设置大模型回复的提示词 -- 属于系统提示词
    # 比如下面的template就是提示词内容，其中{xxxx}表示一个变量，在提示词使用的过程中会被替换为实际的值
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

    #创建提示词对象
    prompt = PromptTemplate(
        template=template,
        input_variables=["context", "question"],
    )

    # 打印召回的结果
    def print_doc(docs):
        print("\n检索到的文档内容：")
        # 遍历docs获取每一条检索到的文档信息
        for doc in docs:
            print(doc.page_content)
            print("-" * 20)
        # 返回检索结果给后续使用
        return docs

    """
    自己构建langchain中的链（chain）来实现RAG问答，步骤：
        1、加载向量化模型
        2、加载向量数据库对象
        3、明确自己的链的执行过程：
            3.1 获取向量数据库的检索结果 -- 把检索的结果和问题一同打包 -- 替换大模型提示词中的变量占位符
            3.2 在使用llm生成回复
            3.3 输出结果的处理，比如可以把llm输出的结果转为字符串输出等等...
    想要构建langchian中的链，其实就是搭积木，要求每一个积木实现runnable接口，如果说在搭建chain的过程中，需要把一个函数
    转为可以放入到chain中使用的积木，那么可以直接把函数放在RunnableLambda中直接转换
    """
    qa_chain = (
        RunnableParallel(    # 并行执行器
            {
                # RunnableLambda的作用就是把普通函数print_docs转换为chain的对象【实现了runnable接口，就可以放入到chain中】
                # retriever的输出就是print_docs函数中的型参输入 --- 等价于doces=检索的文档
                "context": retriever | RunnableLambda(print_doc),   # 上下文，内容就是检索器的结果，直接创建一个检索器即可
                "question": RunnablePassthrough(),  # 透明传递，直接使用question变量的值【不做任何更改】
            }
        )
        # “ | ”表示管道运算符
        | prompt  # 提示词
        | chatLLM  # 大模型对象
        | StrOutputParser()  # 把chatllm输出的结果转为字符串输出
    )

    # 调用 QA 链
    rs = qa_chain.invoke(question)

    # 伪造流式输出
    s = ""
    print("输出结果：")
    for item in rs:
        s += item
        print("\r" + s, end="", flush=True)
        time.sleep(0.1)
    print()


"""02*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-02-*-*-*-*-*-*-*-*-*--*--*-*-*-*-*-*-*-*-*-*-*-*-*-02"""

"""七、执行"""
if __name__ == "__main__":
    # 问答：使用RAG
    question = input("请输入问题：\n")
    yes_rag_qa(question)