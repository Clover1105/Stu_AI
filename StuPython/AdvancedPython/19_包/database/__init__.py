print("数据库包正在初始化...")

# 初始化配置
DB_HOST = "localhost"
DB_PORT = 3306

print(f"数据库配置加载完成：{DB_HOST}:{DB_PORT}")

def init():
    print("执行数据库初始化函数")
init()