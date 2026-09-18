from  langchain.tools import tool
from app.ai.util.mysql_conn import GetMySQLConn
from app.ai.tool.schema.mysql_schema import MysqlSchema


@tool(
    description="生成查询员工信息的mysql查询语句，并执行查询语句",
    args_schema=MysqlSchema
)
def mysql_tool(sql:str):
    """
    执行 sql 语句查询
    数据库模型：
        表名：employee
        字段：user_id 员工ID编号,user_name 员工名字,email 员工邮箱,department 员工所属部门
    规则：
        禁止生成DELETE、UPDATE、INSERT语句
    """
    print("\n【测试】这里是 -- mysql_tool.py")
    print(f"【测试】生成的sql语句：{sql}")
    conn = None
    cur = None
    if "DELETE" in sql.upper() or "UPDATE" in sql.upper() or "INSERT" in sql.upper() or "DROP" in sql.upper() or "CREATE" in sql.upper() or "ALTER" in sql.upper():
        return "禁止执行非法sql语句操作"
    try:
        conn = GetMySQLConn()
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        return result
    except Exception as e:
        print(f"执行sql语句失败：{e}")
        return "执行sql语句失败"
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()