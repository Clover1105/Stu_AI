from . import cart  # 导入同级模块
from .utils import helper

def create_order(cart_items):
    total = helper.calculate_total(cart_items)
    return f"订单创建成功，总金额：{helper.format_price(total)}"
