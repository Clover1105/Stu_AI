import  chromadb

vector = chromadb.PersistentClient(
    path = "../chromadb_data/test02"
)

print(vector)