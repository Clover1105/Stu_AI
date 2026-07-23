"""
知识点：包内相对导入
- . 代表当前目录
- .. 代表上一级目录
- 用于包内模块之间的相互引用
"""

# 目录结构：
# shop/
#   __init__.py
#   cart.py
#   order.py
#   utils/
#       __init__.py
#       helper.py


# 测试包内导入
from shop.cart import Cart
from shop import order

my_cart = Cart()
my_cart.add_item(10.5)
my_cart.add_item(20.3)
my_cart.add_item(5.8)

print(order.create_order(my_cart.items))