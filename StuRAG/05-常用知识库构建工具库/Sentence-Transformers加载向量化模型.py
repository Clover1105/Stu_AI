from sentence_transformers import SentenceTransformer

# 测试数据
documents = [
    "FlagEmbedding 是一个由北京智源人工智能研究院开发的文本嵌入模型。",
    "它可以将文本转换为高维向量，用于计算语义相似度。",
    "BGE 模型在 Massive Text Embedding Benchmark (MTEB) 排行榜上取得了优异的成绩。",
    "RAG（检索增强生成）是一种利用外部知识库来增强大模型回答能力的技术。",
    "苹果公司由史蒂夫·乔布斯、史蒂夫·沃兹尼亚克和罗恩·韦恩于 1976 年创立。",
    "苹果最新款的智能手机是 iPhone 15系列，搭载了A17 Pro芯片。",
    "熊猫是中国的国宝，主要栖息地是四川、陕西和甘肃的山区。",
    "深度学习是机器学习的一个分支，它基于深层神经网络。"
]

# 问题
question = "苹果公司由谁创建的？"

# 加载模型
model = SentenceTransformer(
    # 模型下载路径
    model_name_or_path=r"G:\models\bge-base-zh-v1.5",
    # 运行设备
    device="cuda"
)
# 文本向量化 -- normalize_embeddings：将返回的向量归一化为长度为1
embeddings_1 = model.encode(documents, normalize_embeddings=True)
embeddings_2 = model.encode([question], normalize_embeddings=True)

# 计算获取相似度 -- 通过矩阵乘法（先转置，然后相乘再相加）
similarity = embeddings_1 @ embeddings_2.T

# 输出结果
print(similarity)
print("*-"*10)

# 提取结果
scores = [{index: round(item[0],2)} for index,item in enumerate(similarity.tolist())]
print(scores)
print("*-"*10)

# 排序
# sc_list = sorted(scores, key=lambda x: list(x.values())[0], reverse=True)
# print(sc_list)
scores.sort(key=lambda x: list(x.values())[0], reverse=True)
print(scores)
print("*-"*10)

# 提取documents
for item in scores[:3]:
    for i in item.keys():
        print(documents[i])


