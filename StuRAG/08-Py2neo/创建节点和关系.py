from Load import Neo4jUtil

# 获取连接对象
conn = Neo4jUtil.get_neo4j_conn()

# 定义节点和关系创建的CQL
cql = """
    CREATE
    (P:Person {name: 'CLOVER'})
    -[F:FRIEND {name: '籍贯'}]
    ->(H:Hometown {name: 'CQ'})
"""

# 执行cql
result = conn.run(cql)
print(f"执行成功：{result}")