"""
    参考网站：
        https://github.com/FlagOpen/FlagEmbedding/blob/master/README_zh.md
    选择模型：
        BAAI/bge-base-zh-v1.5
    下载模型地址：
        https://huggingface.co/BAAI/bge-base-zh-v1.5
"""
"""
1. 准备测试数据
2. 将数据向量化
3. 将向量化后的数据存起来
4. 
"""
from FlagEmbedding import FlagAutoModel
import numpy as np

# 准备测试数据
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

# 加载向量化模型
em_moldel = FlagAutoModel.from_finetuned(
    # 模型路径 -- 名称：BAAI/bge-base-zh-v1.5
    model_name_or_path = r"G:\models\bge-base-zh-v1.5",
    # 模型缓存路径
    cache_dir = r"G:\models\bge-base-zh-v1.5",
    # 检索指令
    query_instructions_for_retrieval = "请根据用户问题检索最相关的文档。",
    # 半精度模式
    use_fp16= True,
)

# 向量化数据
em_docs = em_moldel.encode(documents)

# 存储向量化数据
"""
    参数：
        1、存储的文件名字
        2、存储的原始文本数据
        3、存储的向量化数据
"""
np.savez(
    r"G:\GitHub\Stu_AI\StuRAG\datasets\flag_embedding_data.npz",
    documents=documents,embedding_docs=em_docs
)
