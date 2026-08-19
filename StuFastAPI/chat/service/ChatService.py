# 导入
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda, RunnableParallel
from ai.LoadLLM import create_model
from ai.LoadReranker import load_reranker
from ai.LoadChroma import load_chroma_conn
from chat.service import HistoryService
from chat.utils.IntentionUtil import intention_recognition
from chat.dao import ChatDao
from chat.utils import BM25Util,RRFUtil



def chat(question,historyId):
    # 查询对话历史记录，判断是否为新对话
    if historyId == 0:  # 若为新对话，id为0
        history = []
    else:
        history = HistoryService.conversation_log(historyId)['data']    # [{}, {}]

    # 意图识别
    is_legal = intention_recognition(question)["is_legal"]
    llm = create_model()    # 创建大模型对象

    # 判断用户的问题是否走RAG检索
    if not is_legal:    # 不合法
        history.append({"role": "user", "content": question})
        # 直接LLM回复
        for chunk in llm.stream(history):
            if chunk.content:
                yield chunk.content
        return

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
        历史记录：
            {history}
        知识内容：
            {context}
        用户问题：
            {question}
        回答：
    """

    # 创建提示词对象
    prompt = PromptTemplate(
        template=template,
        input_variables=["history","context", "question"],
    )

    # 创建检索器对象
    vector = load_chroma_conn()

    # 转为检索器接口
    v_retriever = vector.as_retriever(search_kwargs={"k": 10})

    # 打印召回结果
    def zh_answer(t,run_lambda):
        print(f"\n{t}到的文档内容：")
        print(run_lambda)
        print("*-"*20)
        for i in run_lambda:
            print(i.page_content)
            print("*-"*20)
        return run_lambda

    # 混合检索函数
    def rrf_retriever():
        # 向量
        v_result = v_retriever.invoke(question)
        zh_answer("向量检索",v_result)
        # bm25
        bm25,docs = BM25Util.build_bm25_index(vector)
        b_result = BM25Util.bm25_search(bm25,question,docs,10)
        zh_answer("bm25检索",b_result)
        # rrf
        rrf_result = RRFUtil.rrf(v_result,b_result)
        zh_answer("rrf检索",rrf_result)
        # 返回结果
        return rrf_result

    # 重排序
    def re_sort(data):
        print("\n开始重排：")
        # 创建重排序模型
        reranker = load_reranker()
        # 获取召回结果
        cons = data['context']
        # 获取问题
        que = data['question']
        # 取出历史记录
        history = data['history']
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
        for i,item in enumerate(cons_sorted[:5]):
            print(f"【第{i+1}条】：{item.page_content}")
        print()

        # 返回排序后的文档
        return {
            "context": cons_sorted,
            "history": history,
            "question": que
        }

    # 创建langchain链
    chain = (
        # 并行执行器
        RunnableParallel(
            {
                # 上下文，内容就是检索的内容
                "context": RunnableLambda(lambda _ : rrf_retriever()),
                # 对话历史记录
                "history": RunnableLambda(lambda _: history),
                # 透明传递，原样返回/输出
                "question": RunnablePassthrough(),
            }
        )
        | RunnableLambda(re_sort) # 重排序
        | prompt   # 提示词
        | llm # 大模型
        | StrOutputParser()  # 把llm输出的结果转为字符串输出
    )
    for chunk in chain.stream(question):
        if chunk:
            yield chunk


def save_conversation_result(conversationResultEntity):
    # 取出conversationResultEntity对象中的数据内容
    question = conversationResultEntity.question
    username = conversationResultEntity.username
    parent_id = conversationResultEntity.parentId
    answer = conversationResultEntity.answer
    # 存储
    history_id = ChatDao.save_conversation_result(question, username, parent_id, answer)
    if history_id != 0:
        return {
            "code": 200,
            "message": "保存成功",
            "data": history_id
        }
    return {
        "code": 500,
        "message": "保存失败",
        "data": None
    }

if __name__ == '__main__':
    for chunk in chat("《中华人民共和国反家庭暴力法》第十五条规定了什么内容？", 1):
        print(chunk)