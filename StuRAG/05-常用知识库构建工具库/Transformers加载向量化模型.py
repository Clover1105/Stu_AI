from transformers import AutoTokenizer, AutoModel
import torch

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

# 加载分词模型
tokenizer = AutoTokenizer.from_pretrained(
    pretrained_model_name_or_path=r"G:\models\bge-base-zh-v1.5"
)

# 加载模型
model = AutoModel.from_pretrained(
    pretrained_model_name_or_path=r"G:\models\bge-base-zh-v1.5"
)

# 模型评估模式，可以注释掉不使用
# model.eval()

# 封装得到文本向量数据 -- 将文本转换为向量
def get_em(texts):
    # 分词模型处理输入的文本 -- 文本分词
    # 使用 tokenizer 对输入的 sentences 进行分词和编码，将文本转换为模型能够处理的输入格式，并返回 PyTorch 张量。
    encoded_input = tokenizer(texts, padding=True, truncation=True, return_tensors='pt')

    # 计算文本（token）向量
    # 关闭梯度计算，使用模型对编码后的输入进行前向推理，得到模型输出。
    with torch.no_grad():
        model_output = model(**encoded_input)

        # 提取 CLS 向量：从模型输出中提取每个句子的 CLS Token 向量，作为整个句子的语义表示（Sentence Embedding）
        sentence_embeddings = model_output[0][:, 0]

        # 向量归一化：对每个句子向量进行 L2 归一化，使每个向量的长度为 1，便于后续计算余弦相似度
        return torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)

# 调用get_em函数处理文档 --》向量
docs_em = get_em(documents)
print(docs_em)
print("*-"*10)

# 准备查询问题
query = "如何使用深度学习？"

# 问题向量化
query_em = get_em([query])

# 获取相似度
cos_sim = torch.matmul(docs_em, query_em.T)

# 打印结果
print(f"相似度：{cos_sim}")

# 处理结果 -- 结果为tensor，需要转换成list
scores = [{index: round(item[0], 2)} for index,item in enumerate(cos_sim.tolist())]
print(scores)
