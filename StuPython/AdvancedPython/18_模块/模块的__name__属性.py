"""
- 直接运行模块时，__name__等于'__main__'
- 被导入时，__name__等于模块名
"""

# 根据运行方式执行不同代码
print(f"当前模块的__name__：{__name__}")

if __name__ == "__main__":
    print("这个模块被直接运行")
else:
    print("这个模块被导入")