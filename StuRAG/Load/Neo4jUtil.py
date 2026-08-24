from py2neo import Graph

def get_neo4j_conn():
    return Graph(
        profile="neo4j://127.0.0.1:7687",  # 连接地址
        auth=("neo4j", "12345678"),  # 连接账号和密码
        name='test',  # 数据库名称
    )