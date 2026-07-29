"""
步骤：
1. 导入加载器类、os、path
2. 获取文件路径
3. 判断是否为执行文档
4. 创建加载器对象，加载数据，输出打印
"""
# 导入
from langchain_community.document_loaders import JSONLoader
import os
from pathlib import Path

# 获取文件路径
path_base = str(Path(os.path.dirname(__file__)).parent)
file_path = os.path.join(path_base, "datasets","Chinese.json")

# 判断
if __name__ == "__main__":
    # 创建加载器对象
    loader = JSONLoader(
        file_path = file_path,
        jq_schema = '.[] | "instruction:" + .instruction + "\\n" + "input:" + .input + "\\n" + "output:" + .output'
    )
    # 加载数据
    data = loader.load()
    # 打印
    for item in data:
        print(item.page_content)