"""
步骤：
1. 导入加载器类、os、path
2. 获取文件路径
3. 判断是否为执行文档
4. 创建加载器对象，加载数据，输出打印
"""

# # 方法一：使用PyPDFLoader
# # 导入
# from langchain_community.document_loaders import PyPDFLoader
# import os
# from pathlib import Path
#
# # 获取文件路径
# path_base = str(Path(os.path.dirname(__file__)).parent)
# pdf_path = os.path.join(path_base,"datasets","09.算力租赁.pdf")
#
# # 判断
# if __name__ == "__main__":
#     # 创建加载器对象
#     loader = PyPDFLoader(
#         pdf_path
#     )
#     # 加载数据
#     data = loader.load()
#     # 输出打印
#     for items in data:
#         print(items.page_content)



"""
步骤：
1. 导入加载器类、os、path
2. 获取文件路径
3. 判断是否为执行文档
4. 提取文本，输出打印
"""

# 方法二：使用extract_text
# 导入
from pdfminer.high_level import extract_text
import os
from pathlib import Path

# 获取文件路径
path_base = str(Path(os.path.dirname(__file__)).parent)
pdf_path = os.path.join(path_base,"datasets","09.算力租赁.pdf")

# 判断
if __name__ == "__main__":
    # 提取文本
    text = extract_text(pdf_path)
    # 输出打印
    print(text)