# 导入
from langchain_core.output_parsers import StrOutputParser
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda, RunnableParallel
from Load.LoadEmbeddingModel import load_embedding_model
from Load.LoadLLM import load_model
from Load.LoadReranker import load_reranker

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
    embedding_function=load_embedding_model()
)

# 转为检索器接口
retriever = vector.as_retriever(search_kwargs={"k": 5})

# 问题
wt = "长城是什么？"

# 打印召回结果
def zh_answer(run_lambda):
    print("检索到的文档内容：")
    for i in run_lambda:
        print(i.page_content)
        print("*-"*20)
    return run_lambda

# 重排序
def re_sort(data):
    print("\n开始重排：")
    # 创建重排序模型
    reranker = load_reranker()
    # 获取召回结果
    cons = data['context']
    # 获取问题
    que = data['question']
    # 问题和召回文档 进行包装 构造reranker输入
    reranker_input = [(que,con.page_content) for con in cons]
    # 调用重排序模型，计算得分
    scores = reranker.compute_score(reranker_input)
    # print(f"得分：\n{scores}\n")
    # 文档和分数进行包装
    con_score = list(zip(cons,scores))
    # print(f"包装后的文档和得分：\n{con_score}\n")
    # 排序
    con_score.sort(key=lambda x: x[1], reverse=True)
    # print(f"重排序后的文档和得分：\n{con_score}\n")
    # 获取排序后的文档
    cons_sorted = [con[0] for con in con_score]
    # print(f"重排序后的文档：")
    for i,item in enumerate(cons_sorted[:3]):
        print(f"【第{i+1}条】：{item.page_content}")

    # 返回排序后的文档
    return {
        "context": cons_sorted,
        "question": que
    }

# 创建langchain链
chain = (
    # 并行执行器
    RunnableParallel(
        {
            # 上下文，内容就是检索的内容
            "context": retriever | RunnableLambda(zh_answer),
            # 透明传递，原样返回/输出
            "question": RunnablePassthrough(),
        }
    )
    | RunnableLambda(re_sort) # 重排序
    | prompt   # 提示词
    | load_model() # 大模型
    | StrOutputParser() # 转字符串
)

# 测试
ce_shi = chain.invoke(wt)
print(f"\n回答：\n{ce_shi}")
