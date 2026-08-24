from Load import Neo4jUtil
conn = Neo4jUtil.get_neo4j_conn()

# 创建节点和关系
def create_node_relationship():
    cql = """
        MERGE (p:Person {name: '乔布斯'})
        MERGE (place:Place {name: '旧金山'})
        MERGE (company:Company {name: '苹果公司'})
        MERGE (category:Category {name: '科技公司'})
        
        MERGE (p)-[:BORN_IN]->(place)
        MERGE (p)-[:FOUNDED]->(company)
        MERGE (company)-[:HAS_TYPE]->(category)
    """
    result = conn.run(cql)
    print(f"执行成功：{result}")


# 查询节点和关系
def query_node_relationship():
    # 查询所有三元组
    cql = """
        MATCH (s)-[r]->(o)
        RETURN s.name AS 主语, type(r) AS 谓语, o.name AS 宾语;
    """
    result = conn.run(cql)
    print(f"执行成功：\n{result}")
    # 查询某个实体的关系
    cql = """
        MATCH (s:Person {name: '乔布斯'})-[r]->(o)
        RETURN s.name AS 主语, type(r) AS 谓语, o.name AS 宾语;
    """
    result = conn.run(cql)
    print(f"\n执行成功：\n{result}")
    # 查询与某个实体相关的所有节点
    cql = """
        MATCH (s {name: '旧金山'})-[r]-(o)
        RETURN s, r, o;
    """
    result = conn.run(cql)
    print(f"\n执行成功：\n{result}")

if __name__ == '__main__':
    # create_node_relationship()
    query_node_relationship()
