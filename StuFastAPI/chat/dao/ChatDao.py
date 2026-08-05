from common import MySQLUtil
"""
    查询操作不需要做事务管理
    增删改操作需要事务管理
    操作成功 --- commit 提交事务：执行当前操作
    操作失败 --- rollback回滚事务：不执行当前操作
"""
def save_conversation_result(question, username, parent_id, answer):
    # 创建数据库连接对象
    conn = MySQLUtil.get_mysql_conn()
    cur = conn.cursor()
    try:
        # 执行SQL语句
        sql = "INSERT INTO history VALUES (null, %s, %s, %s, %s, now());"
        cur.execute(sql, [question, username, parent_id, answer])
        conn.commit()   # 提交事务
        # 返回当前新增数据的主键自增ID -- history_id
        return cur.lastrowid    # 返回最后一个插入的行ID
    except Exception as e:
        print(f"新增对话结果失败：{e}")
        conn.rollback() # 回滚事务
        return 0
    finally:
        # 关闭连接
        MySQLUtil.close_mysql_conn(cur, conn)

