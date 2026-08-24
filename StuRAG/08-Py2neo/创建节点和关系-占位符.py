from Load import Neo4jUtil

# 获取连接对象
conn = Neo4jUtil.get_neo4j_conn()

# cql 的占位符是 $，例如 $name

cql = """
    CREATE
    (P:Person {name: $p_name})
    -[C:CONTACT {name: $c_name}]
    ->(H:Hometown {name: $h_name})
"""

# 定义占位符的值，字典格式
params = {
    "p_name": "CLOVER",
    "c_name": "籍贯",
    "h_name": "CQ"
}

# 执行cql
result = conn.run(cql, params)
print(f"执行成功：{result}")