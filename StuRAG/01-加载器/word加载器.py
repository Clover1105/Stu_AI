"""
步骤：
1. 导入加载器类、os、path
2. 获取文件路径
3. 判断是否为执行文档
4. 创建加载器对象，加载数据，输出打印
"""
# # 导入
# from langchain_community.document_loaders import Docx2txtLoader
# import os
# from pathlib import Path
#
# # 获取文件路径
# path_base = str(Path(os.path.dirname(__file__)).parent)
# docx_path = os.path.join(path_base, "datasets","test.docx")
#
# # 判断
# if __name__ == "__main__":
#     # 创建加载器对象
#     loader = Docx2txtLoader(
#         file_path = docx_path
#     )
#     # 加载数据
#     data = loader.load()
#     # 输出打印
#     for item in data:
#         print(item.page_content)

"""
步骤：
1. 导入库、os、path
2. 获取文件路径
3. 判断是否为执行文档
4. 创建 Document 对象，创建打印列表
5. 按 表格==>行==>单元格 遍历 Document 对象，添加到打印列表
6. 打印 -- 打印列表
"""
# 导入
from docx import Document
import os
from pathlib import Path

# 获取文件路径
path_base = str(Path(os.path.dirname(__file__)).parent)
docx_path = os.path.join(path_base, "datasets","test.docx")

# 判断
if __name__ == "__main__":
    # 创建 Document 对象
    doc = Document(docx_path)
    # 创建打印列表
    list = []
    # 遍历
    for table in doc.tables:    # 表格，表格对象
        # print(table,"*-"*10)
        for row in table.rows:  #  行，行对象
            # print(row,"**"*10)
            # 创建行列表
            row_list = []
            for cell in row.cells:  # 单元格，单元格对象
                # print(cell)
                # print(cell.text)    # 获取单元格对象的文本内容
                row_list.append(cell.text)
            list.append(row_list)
    # 打印
    for items in list:
        print(items)