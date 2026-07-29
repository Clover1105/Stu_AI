import  numpy as np
from FlagEmbedding import FlagAutoModel

# 加载npz文件 -- 数据
data = np.load(r"G:\GitHub\Stu_AI\StuRAG\datasets\flag_embedding_data.npz")
# print(data)

# 获取原始文档
docs = data['documents']
print(f"原始数据：\n{docs}")

# 获取向量化数据
em_data = data['embedding_docs']
# print(f"向量化数据：\n{em_data}")

# 测试问题
# 比对方法：将问题转换为向量后，和向量化数据中的每一个向量进行余弦相似度的比对
question = "什么是BGE模型？"

# 加载向量化模型
em_moldel = FlagAutoModel.from_finetuned(
    # 模型路径 -- 名称：BAAI/bge-base-zh-v1.5
    model_name_or_path = r"G:\models\bge-base-zh-v1.5",
    # 检索指令
    query_instructions_for_retrieval = "请根据用户问题检索最相关的文档。",
    # 半精度模式
    use_fp16= True,
)

# 问题向量化（要和之前的模型一致）
qu_em = em_moldel.encode(question)
# print(f"问题向量化：\n{qu_em}")

# 计算两个向量的余弦相似度
def cos_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# # 定义一个存放所有结果的列表
# sc_list = []
#
# # 遍历原始文档的向量化数据结果，和问题向量进行余弦相似度计算
# for item in em_data:
#     sc_list.append(cos_sim(item,qu_em))
#
# # 打印未排序结果
# print(f"未排序结果：\n{sc_list}")

# 获取未排序列表，元素为字典 -- 召回开始
sc_list = [{index: cos_sim(item,qu_em)} for index, item in enumerate(em_data)]
print(f"未排序结果：\n{sc_list}")

# 排序 -- 粗排
sc_list.sort(key=lambda x: list(x.values())[0], reverse=True)
print(f"排序结果：\n{sc_list}")

# 获取top-k文档 -- 最终召回结果
tok_k = 3
# 定义一个存放检索结果的列表
retriever_re = []
for index,item in enumerate(sc_list[:tok_k]):
    for j in item.keys():
        print(f"第{index+1}个文档：\n{docs[j]}")
        retriever_re.append(docs[j])
# re = [docs[j] for index,item in enumerate(sc_list[:tok_k]) for j in item.keys()]
# print(f"最终检索结果：\n{re}")
# print(f"最终检索结果：\n{retriever_re}")

# 对召回的结果进行重排序
"""
把question和召回【粗排--以上步骤】的文档再次计算 
    --- 通过重排序模型来实现【重排序模型一般都是cross-encoder】
    --- 本质上就是计算question和召回的文档之间的相似度【自注意力机制来实现的】 --- 精排
过程：
    需要把问题和召回的文档包装成(question, doc1)、(question, doc2)、(question, doc3)...
重排序发生在粗排之后，注入上下文给大模型之前
"""

from FlagEmbedding import FlagReranker

# 加载重排序模型
reranker = FlagReranker(
    model_name_or_path=r"G:\models\bge-reranker-large",
    use_fp16=True
)

# 把问题和召回的文档进行包装 -- 重排序发生在粗排之后，大模型回复之前
reranker_input = [(question, doc) for doc in retriever_re]
print(f"重排序输入：\n{reranker_input}")

# 调用重排序方法 -- 计算得分
scores = reranker.compute_score(reranker_input)
print(scores)
