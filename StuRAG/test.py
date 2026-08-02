
"""
一、创建向量数据库
    1. 创建向量化模型（和创建向量数据库时使用的模型一致）：
        HuggingFaceEmbeddings()
    2. 创建向量数据库对象：
        Chroma()
    3. 转为检索器接口：
        as_retriever(),k=n
    4. 存入数据：
        测试数据 -- txt
        创建分割器对象 -- RecursiveCharacterTextSplitter()
        分割数据 -- split_text()
        将数据转为Document对象 -- [Document()+for]
        将Document对象存入数据库 -- add_documents()
        将数据存储到em_DB中 -- Chroma.from_documents() -- 数据文本、em模型、db_save_path、检索方式、集合name
    5. 查询全部数据：
        建立连接 -- Chroma() -- 集合name、db_save_path
        获取全部数据 -- get()
二、创建langchain链
    1. 创建系统提示词
    2. 创建系统提示词对象：PromptTemplate
        提示词、输入变量（内容，问题）
    3. 创建检索器对象：Chroma
        集合name、db_save_path、向量化模型
    4. 转为检索器接口：as_retriever()
    5. 打印召回结果：创建函数，后期执行器中调用
    6. 重排序（作业）
    7. 创建langchain链：RunnableParallel、RunnableLambda、RunnablePassthrought、StrOutParser
        执行器、重排序、提示词、大模型对象、转字符串
    8. 测试：非流式
"""