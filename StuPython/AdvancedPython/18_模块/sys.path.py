"""
模块搜索路径（sys.path）
    - Python在sys.path中列出的路径中搜索模块
    - 可以通过sys.path.append()添加自定义路径
"""

# 查看和添加模块搜索路径
import sys

print("默认搜索路径：")
for path in sys.path[:3]:
    print(f"  {path}")

# 添加自定义路径
sys.path.append("D:/my_modules")
print(f"\n添加后路径数量：{len(sys.path)}")