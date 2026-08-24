from fontTools.misc.bezierTools import calcQuadraticArcLength

from Load import Neo4jUtil

conn = Neo4jUtil.get_neo4j_conn()

# # 删除没有关系的节点
# cql = """
#     match (n:Person)
#     where n.name='clover'
#     delete n;
# """
# result = conn.run(cql)
# data = result.data()
# print(f"data: {data}")
#
# # 删除有关系的节点 -- 不能直接删除，要先删除关系或者用detach delete
# cql = """
#     match (n:Person)
#     where n.name='CLOVER'
#     detach delete n;
# """
# result = conn.run(cql)
# data = result.data()
# print(f"data: {data}")
#
# # 只删除关系
# cql = """
#     match (n:Person)-[r:CONTACT]->(p:Hometown)
#     where n.name = 'CLOVER'
#     delete r;
# """
# result = conn.run(cql)
# data = result.data()
# print(f"data: {data}")

# 删除所有节点和关系
cql = """
    match (n)
    detach delete n;
"""
result = conn.run(cql)
data = result.data()
print(f"data: {data}")