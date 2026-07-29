"""
步骤：
1. 导入加载器类、 OCR 软件接口、os、path
2. 配置OCR安装路径
3. 获取图片路径
4. 判断是否为执行文档
5. 创建加载器对象，加载数据，输出打印
"""
# 导入
from langchain_community.document_loaders import UnstructuredImageLoader
import unstructured_pytesseract.pytesseract as pytesseract
import os
from pathlib import Path

# 配置安装路径
pytesseract.tesseract_cmd = r"D:\MyDownload\tesseract-ocr\Tesseract-OCR\tesseract.exe"

# 获取图片路径
path_base = str(Path(os.path.dirname(__file__)).parent)
file_path = os.path.join(path_base,"datasets","黑神话.png")

# 判断
if __name__ == "__main__":
    # 创建加载器对象
    loader = UnstructuredImageLoader(
        file_path = file_path,
        mode = "elements",
        languages = ["chi_sim"]
    )
    # 加载数据
    data = loader.load()
    # 打印
    for item in data:
        print(item.page_content)