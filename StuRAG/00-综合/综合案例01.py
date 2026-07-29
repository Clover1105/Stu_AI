# 使用langchain封装的问答链PetrievalQA实现
# 注意：langchain封装的API和chroma库中的API不一样，不要混淆
# 安装库：pip install langchain-chroma==1.1.0

# 拓展知识（先了解即可）：若使用 langchain 中的技术将各各模块搭建起来，那么每一个模块的类型都要是 runable 结构

"""
步骤：
1. 项目配置：
    原始文档路径、ChromaDB 数据库持久化存储路径、ChromaDB 集合名称、LLM 模型名称（用于生成回答）
2. 创建向量数据库并且添加数据 -- 处理文档
    导包：TextLoader、RecursiveCharacterTextSplitter
    加载器读取文本、加载数据、创建分割对象、分割文本
3. 创建向量数据库并且添加数据 -- 加载向量化模型（本地）
    导包：HuggingFaceEmbeddings
    在项目配置中添加向量模型本地存储路径
    实现本地要添加参数：model_kwargs={"device": "cuda","local_files_only": True,}
4. 创建向量数据库并且添加数据 -- 创建向量数据库
    导包：Chroma
    参数：数据内容、向量化模型、存储位置、集合名称、相似度匹配方式
    防止出问题报错，可以使用try...except...方法
5. 查询向量数据库中的数据
    Chroma 方法（集合名称，数据库路径）
6. 初始化大语言模型
    导包：ChatOpenAI、os
    -- ChatOpenAI()
    非流式 -- invoke()
7. 问答：不使用RAG
    设置：系统和角色信息，调用llm生成回复，打印回复（get方法）
    存在幻觉问题
8. 问答：使用RAG
    -- 先用 langchain 封装的QA链实现
    导包：RetrievalQA
    初始化向量化模型（和创建时的模型一致）、创建向量数据库对象、调用QA链、通过QA链生成回复
9. 执行，调用函数
"""

# 模型
from langchain_openai import ChatOpenAI
# 路径
import os
# 加载器
from langchain_community.document_loaders import TextLoader
# 分割器
from langchain_text_splitters import RecursiveCharacterTextSplitter
# 向量化模型
from langchain_huggingface import HuggingFaceEmbeddings
# 向量数据库
from langchain_chroma import Chroma
# 问答链
from langchain_classic.chains.retrieval_qa.base import RetrievalQA



"""一、项目配置"""
# 原始文档路径
txt_path = r"G:\GitHub\Stu_AI\StuRAG\datasets\测试.txt"
# ChromaDB 数据库持久化存储路径
vector_path = r"G:\GitHub\Stu_AI\StuRAG\chromadb_data"
# ChromaDB 集合名称
collection_name = "an_li01"
# Embedding 模型名称
model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
# Embedding 模型本地存储路径
model_path = r"G:\models\paraphrase-multilingual-MiniLM-L12-v2"
# model_name 用于指定 Hugging Face 模型名称；
# model_path 用于指定本地模型路径，本项目使用本地模型，因此实际加载的是 model_path。

"""二、初始化大语言模型"""
chatLLM = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen3.7-max",
)

"""三、创建向量数据库并添加数据"""
def build_vector_db():
    """ 加载器"""
    # 创建加载器对象
    loader = TextLoader(file_path=txt_path, encoding="utf-8")
    # 加载数据
    txt = loader.load()

    """ 分割器 """
    # 创建分割对象
    txt_fg = RecursiveCharacterTextSplitter(
        chunk_size=100, # 块大小
        chunk_overlap=20,   # 块重叠大小
        length_function=len,    # 计算块的长度
        separators=["\n\n", ".", "？", "！", "\n"]    # 分割符号
    )
    # 分割文本
    txt_list = txt_fg.split_documents(txt)

    """ 初始化 Embedding 模型 """  # 设置全部通过本地地址加载
    embedding_model = HuggingFaceEmbeddings(
        model_name=model_path,
        # 使用本地模型
        model_kwargs={
            "device": "cuda",
            "local_files_only": True,
        },
    )

    """ 创建 Chroma 向量数据库并写入文档 """   # 一步到位，直接就把数据存入到了向量数据库中
    try:
        Chroma.from_documents(
            documents=txt_list, # 数据内容
            embedding=embedding_model,  # 向量化模型
            persist_directory=vector_path,  # 数据库持久化存储路径
            collection_name=collection_name,    # 集合名称
            collection_metadata={"hnsw:space":"cosine"} # 相似度匹配
        )
        print("向量数据库创建成功")
    except Exception as e:
        print(f"向量数据库创建失败{e}")

"""四、查询向量数据库中的数据"""
def chaxun_vector_da():
    # 创建（连接）Chroma 向量数据库对象
    # 并连接指定的 Collection（集合）
    vector_db = Chroma(
        collection_name = collection_name,
        persist_directory = vector_path
    )
    # get()：获取当前集合中的全部数据
    print(vector_db.get())

"""五、问答：不使用RAG"""
def no_rag():
    messages = [
        # 系统角色提示
        {"role": "system", "content": "你是一个专业的学校百科全书，什么都知道"},
        # 用户问题
        {"role": "user", "content": "重庆三峡学院正式更名为重庆三峡大学？"}
    ]
    # LangChain 中调用大语言模型（LLM）生成回复的方式
    rs = chatLLM.invoke(messages)
    print(rs.content)

"""六、问答：使用RAG"""    # 先用langchain封装的QA链实现
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

    # 创建 QA 链（RAG 问答链）
    # 将大语言模型（LLM）和向量数据库（Retriever）组合起来，
    # 构建一个能够"先检索知识，再生成回答"的问答系统。
    qa_chain = RetrievalQA.from_chain_type(
        llm=chatLLM,  # 大语言模型（LLM）
        # 检索器，这个检索出来的结果就是召回，通常10-30条数据
        retriever=vector_db.as_retriever(search_kwargs={"k": 3}),  # 由 Chroma 转换得到的检索器
        return_source_documents=True  # 是否返回检索到的原始文档（可选），字典
    )

    # 调用 QA 链执行问答
    # QA 链会先检索相关文档，再结合检索结果生成最终回答。
    rs = qa_chain.invoke(question)

    # 输出模型生成的回答
    print(rs["result"])

"""七、执行"""
if __name__ == "__main__":
    # 创建向量数据库，存入数据
    # build_vector_db()
    # 查询
    # chaxun_vector_da()
    # 问答：不使用RAG
    # no_rag()
    # 问答：使用RAG
    question = input("请输入问题：\n")
    yes_rag_qa(question)