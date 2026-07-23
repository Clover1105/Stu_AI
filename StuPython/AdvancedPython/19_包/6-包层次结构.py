"""
知识点：包层次结构
- 包可以嵌套子包
- 每个子包都需要__init__.py文件
- 使用点号表示层级
"""

# 目录结构：
# webapp/
#   __init__.py
#   api/
#       __init__.py
#       users.py
#       products.py
#   utils/
#       __init__.py
#       validator.py


# 导入嵌套包中的模块
import webapp.api.users
from webapp.api import products
from webapp.utils.validator import is_email

print(webapp.api.users.get_user(100))
print(products.get_product(200))
print(f"邮箱验证：{is_email('test@example.com')}")