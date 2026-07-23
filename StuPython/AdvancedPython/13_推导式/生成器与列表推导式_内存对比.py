"""
生成器vs列表推导式内存对比
    - 列表推导式：一次性生成所有数据，占用内存大
    - 生成器表达式：按需生成，占用内存小
    - 适合处理大量数据
"""
import sys  # 导入sys模块，用于获取内存占用

"""1.内存占用对比"""
print("=== 内存占用对比 ===")

# 列表推导式
list_data = [x ** 2 for x in range(1000000)]
list_memory = sys.getsizeof(list_data)  # sys.getsizeof()获取对象占用内存大小
print(f"列表推导式内存：{list_memory / 1024 / 1024:.2f} MB")

# 生成器表达式
gen_data = (x ** 2 for x in range(1000000))
gen_memory = sys.getsizeof(gen_data)    # sys.getsizeof()获取对象占用内存大小
print(f"生成器表达式内存：{gen_memory} 字节")




"""2.处理大文件数据（模拟）"""
print("\n=== 模拟处理大数据 ===")

def large_data():
    """模拟大数据生成器"""
    for i in range(10000000):
        yield i # yield关键字 --> 生成器表达式

# 使用生成器处理
total = sum(x for x in large_data() if x % 2 == 0)
print(f"使用生成器计算偶数和（前1000万）：{total}")




"""3.什么时候用列表，什么时候用生成器"""
print("""
\n=== 使用建议 ===
使用列表推导式的场景：
1. 数据量小，需要多次访问
2. 需要随机访问元素（索引）
3. 需要修改数据
\n使用生成器的场景：
1. 数据量巨大
2. 只需遍历一次
3. 内存有限
""")