"""
步骤：
1. 导入加载器类、os、path
2. 获取文件路径
3. 判断是否为执行文档
4. 创建加载器对象，加载数据，输出打印
"""

# 导入
from langchain_community.document_loaders import TextLoader
import os
from pathlib import Path

# 获取
path_base = str(Path(os.path.dirname(__file__)).parent)
file_path = os.path.join(path_base, "datasets","华清远见.txt")

# 加载器对象，加载数据，打印
def txt():
    # 对象
    loader = TextLoader(
        file_path = file_path,
        encoding = "utf-8"
    )
    # 数据
    data = loader.load()
    # 打印
    for index, item in enumerate(data):
        print(f"第{index+1}条数据：")
        # page_content -- 访问 Document 对象中文本内容的属性
        print(item.page_content)    # 只输出文本内容
        print("-"*50)

# 判断
if __name__ == "__main__":
    txt()