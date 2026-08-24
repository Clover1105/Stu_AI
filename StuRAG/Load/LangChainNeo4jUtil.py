from langchain_neo4j import Neo4jGraph

def get_neo4j_conn():
    return Neo4jGraph(
        url="bolt://127.0.0.1:7687",
        username="neo4j",
        password="12345678",
        database="neo4j"
    )

if __name__ == '__main__':
    conn = get_neo4j_conn()
    print(f"连接成功：{conn}")