from Load import Neo4jUtil

conn = Neo4jUtil.get_neo4j_conn()

cql = """
    match (P:Person {name: 'CLOVER'})
    return P;
"""

result = conn.run(cql)
print(result)   # 表格形式
print(type(result))   # class 'py2neo.database.Result'

# data函数：可以获取到数据内容
data = result.data()
print(f"data: {data}")      # data: [{'P': Node('Person', name='CLOVER')}, {'P': Node('Person', name='CLOVER')}]
print(type(data))   # class 'list'

p1 = data[0]
print(f"p1: {p1}")  # p1: {'P': Node('Person', name='CLOVER')}
print(type(p1))   # class 'dict'

p2 = data[0]['P']
print(f"p2: {p2}")  # p2: (_6:Person {name: 'CLOVER'})
print(type(p2)) # class 'py2neo.data.Node'


# 查询全部数据
cql = """
    match (n) return n;
"""
result = conn.run(cql)
data = result.data()
print(f"\ndata: {data}")

# where 条件查询
cql = """
    match (n)
    where n.name = 'clover'
    return n;
"""
result = conn.run(cql)
data = result.data()
print(f"\ndata: {data}")

cql = """
    match (n:Person)
    where n.name in ['clo','year']
    return n;
"""
result = conn.run(cql)
data = result.data()
print(f"\ndata: {data}")

# 查询节点和关系
cql = """
    match (P:Person)-[F:FRIEND]->(H:Hometown)
    where P.name = 'clover' or H.name = "CQ"
    return P, F, H;
"""
result = conn.run(cql)
data = result.data()
print(f"\ndata: {data}")

