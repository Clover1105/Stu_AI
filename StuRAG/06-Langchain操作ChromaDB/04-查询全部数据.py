from langchain_chroma import Chroma

# 建立连接
vector = Chroma(
    collection_name="hqyj",
    persist_directory=r"G:\GitHub\Stu_AI\StuRAG\chromadb_data",
)
# 获取全部数据
results = vector.get()
print(results)