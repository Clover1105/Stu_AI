from Load import Neo4jUtil
conn = Neo4jUtil.get_neo4j_conn()

cql = """
    // 1. 创建主实体节点：竞赛名称
    MERGE (comp:竞赛名称 {name: '语言与智能技术竞赛', probability: 0.6310065965976648})
    
    // 2. 创建主办方实体节点及关系
    MERGE (org1:机构 {name: '中国计算机学会', probability: 0.7511016583800938})
    MERGE (comp)-[:主办方]->(org1)
    
    MERGE (org2:机构 {name: '中国中文信息学会', probability: 0.8484645105804987})
    MERGE (comp)-[:主办方]->(org2)
    
    // 3. 创建承办方实体节点及关系
    MERGE (cont1:机构 {name: '百度公司', probability: 0.8332406110869108})
    MERGE (comp)-[:承办方]->(cont1)
    
    MERGE (cont2:机构 {name: '中国计算机学会自然语言处理专委会', probability: 0.6294969648882613})
    MERGE (comp)-[:承办方]->(cont2)
    
    MERGE (cont3:机构 {name: '中国中文信息学会评测工作委员会', probability: 0.7172121474980742})
    MERGE (comp)-[:承办方]->(cont3)
    
    // 4. 创建时间实体节点及关系
    MERGE (time:时间 {name: '2022年', probability: 0.9482227255116413})
    MERGE (comp)-[:举办时间]->(time)
"""

result = conn.run(cql)
print(f"执行成功：{result}")