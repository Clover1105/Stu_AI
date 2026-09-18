import pymysql
import os
from dotenv import load_dotenv
load_dotenv()
# 获取连接
def GetMySQLConn():
    try:
        host = os.getenv("MYSQL_HOST")
        port = int(os.getenv("MYSQL_PORT"))
        user = os.getenv("MYSQL_USER")
        password = os.getenv("MYSQL_PASSWORD")
        database = os.getenv("MYSQL_DATABASE")
        charset = os.getenv("MYSQL_CHARSET")
        return pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset=charset,
            # # 以 dict 的方式返回查询结果
            cursorclass=pymysql.cursors.DictCursor
        )
    except Exception as e:
        print(f"获取数据库连接失败：{e}")
        return None

# 关闭连接
def CloseMySQLConn(cursor,conn):
    cursor.close()
    conn.close()

if __name__ == '__main__':
    conn = GetMySQLConn()