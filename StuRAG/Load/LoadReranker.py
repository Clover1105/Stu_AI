from FlagEmbedding import FlagReranker

# 加载重排序模型
def load_reranker():
    return FlagReranker(
        model_name_or_path=r"G:\models\bge-reranker-large",
        use_fp16=True
    )
