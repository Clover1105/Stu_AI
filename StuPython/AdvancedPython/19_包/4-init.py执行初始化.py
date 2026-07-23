"""
__init__.py执行初始化
    - 包被导入时自动执行__init__.py中的代码
    - 用于初始化操作：加载配置、设置变量等
"""

# 目录结构：
# database/
#   __init__.py
#   mysql.py
#   redis.py


# 测试初始化
import database

print(f"访问包中变量：{database.DB_HOST}")