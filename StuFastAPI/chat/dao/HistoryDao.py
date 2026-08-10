from common import MySQLUtil

# 查询历史记录菜单栏
def query_history_menu(username):
    conn = MySQLUtil.get_mysql_conn()
    cur = conn.cursor() # 获取游标
    sql = 'select history_id,question,create_time from history where username = %s and parent_id = 0;'
    cur.execute(sql, [username])    # 执行sql语句
    result = cur.fetchall() # 获取所有结果
    MySQLUtil.close_mysql_conn(cur, conn)   # 关闭连接
    return result

# 查询某条历史记录详情
def conversation_log(historyId):
    conn = MySQLUtil.get_mysql_conn()
    cur = conn.cursor() # 获取游标
    sql = 'select question,answer from history where history_id = %s or parent_id = %s order by history_id asc;'
    cur.execute(sql, [historyId, historyId])    # 执行sql语句
    result = cur.fetchall() # 获取所有结果
    MySQLUtil.close_mysql_conn(cur, conn)   # 关闭连接
    return result

def delete_history(historyId):
    conn = MySQLUtil.get_mysql_conn()
    cur = conn.cursor() # 获取游标
    is_TF = 0
    try:
        sql = 'delete from history where history_id = %s or parent_id = %s;'
        cur.execute(sql, [historyId, historyId])    # 执行sql语句
        conn.commit()
        print(f"删除历史记录成功：{cur.rowcount}条数据被删除")
        is_TF = 1
    except Exception as e:
        print(f"删除历史记录失败：{e}")
        conn.rollback()
        is_TF = 0
    finally:
        MySQLUtil.close_mysql_conn(cur, conn)   # 关闭连接
        return is_TF

def search_history(username, searchHistory):
    conn = MySQLUtil.get_mysql_conn()
    cur = conn.cursor() # 获取游标
    try:
        sql = 'select history_id,question,create_time from history where username = %s and parent_id = 0 and question like %s;'
        cur.execute(sql, [username, '%'+searchHistory+'%'])    # 执行sql语句
        result = cur.fetchall() # 获取所有结果
        print(f"搜索历史记录成功，id：{result[0]['history_id']}")
        return result
    except Exception as e:
        print(f"搜索历史记录失败：{e}")
        return None
    finally:
        MySQLUtil.close_mysql_conn(cur, conn)   # 关闭连接

# 测试
if __name__ == '__main__':
    # print(query_history_menu('clover'))
    # print(conversation_log(1))
    # print(delete_history(12))
    print(search_history('clover', '你'))


