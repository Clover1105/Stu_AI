from common import MySQLUtil

def check_email(email):
    # 1. 获取数据库连接对象
    conn = MySQLUtil.get_mysql_conn()
    # 2. 获取游标对象
    cur = conn.cursor()
    # 3. 编写sql语句
    sql = "select * from users where email = %s;"
    # 4. 执行sql语句
    cur.execute(sql, [email])
    # 5. 获取结果
    result = cur.fetchall()
    print(f"获取的结果为: {result}")    # 结果为一个列表，表示有数据
    # 6. 关闭连接
    MySQLUtil.close_mysql_conn(cur, conn)
    # 返回结果
    return result

if __name__ == "__main__":
    print(check_email("c@qq.com"))

# [{'users_id': 1001, 'username': 'clover', 'email': 'c@qq.com', 'create_time': datetime.datetime(2026, 7, 30, 11, 37, 29)}]