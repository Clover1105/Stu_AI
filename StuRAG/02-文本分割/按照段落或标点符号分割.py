# 导入加载器
from langchain_community.document_loaders import TextLoader
# 导入分割器
from langchain_text_splitters import RecursiveCharacterTextSplitter
# 导入路径包
import os
from pathlib import Path

# 获取文件路径
path_base = str(Path(os.path.dirname(__file__)).parent)
text_path = os.path.join(path_base, "datasets","测试2.txt")

# 文档加载器
loader = TextLoader(text_path,encoding="utf-8")
data = loader.load()
txt = data[0].page_content
# print(txt)  # 获取文本内容

# 创建分割器对象
txt_fg = RecursiveCharacterTextSplitter(
    chunk_size = 300,    # 分割块的大小
    # chunk_overlap = 20,   # 块的重叠大小
    # 分割符号
    separators = [    "\n\n","\n",
            "。", "，", "？", "、", "：", "；", "！", "“", "”", "（",
            "）", "《", "》", "……", "——", "‘", "’", "·", "【", "】",
    ],
    # 计算块的长度
    length_function = len
)

# 分割文本
txt_list = txt_fg.split_text(txt)   # 返回的是列表
# 遍历输出
for item in txt_list:
    print(item)
    print("*-"*10)
