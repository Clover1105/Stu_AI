"""
步骤：
1. 导入加载器类、网页解析、os、path
2. 获取网页路径
3. 判断是否为执行文档
4. 创建加载器对象，加载数据，输出打印
"""
# 导入
from langchain_community.document_loaders import WebBaseLoader
from bs4 import SoupStrainer

# 获取网页路径
url = "https://www.sanxiau.edu.cn/"

# 判断
if __name__ == "__main__":
    # 创建加载器对象
    loader = WebBaseLoader(
        url,
        bs_kwargs = {
            # 只解析标题和div标签
            "parse_only": SoupStrainer(("title","div")),
            # 只解析指定的具体标签
            # "parse_only": SoupStrainer("div",{"class":"wrap"})
        }
    )
    # 加载数据
    data = loader.load()
    # 输出打印
    for items in data:
        print(items.page_content)