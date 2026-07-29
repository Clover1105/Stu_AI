# 导入 ModelScope 相关模块
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
# 导入 TextLoader 文档加载器
from langchain_community.document_loaders import TextLoader
# 导入路径包
import os
from pathlib import Path

# 获取项目根路径
base_path = str(Path(os.path.dirname(__file__)).parent)
# 拼接数据集路径
file_path = os.path.join(base_path, "datasets", "测试.txt")

# 创建 TextLoader 加载器对象
loader = TextLoader(file_path, encoding="utf-8")
data = loader.load()    # 加载文档，返回 Document 对象列表
# print(data)
text = data[0].page_content # 提取文档正文内容

# 本地分割模型路径
model_path = r"G:\models\nlp_bert_document-segmentation_chinese-base"

# 创建文档分割 Pipeline
p = pipeline(
    task=Tasks.document_segmentation,
    model=model_path,
    model_revision='master')

# 使用模型对文档进行语义分割
result = p(
    documents=text,
)

# 输出分割结果
chunks = result[OutputKeys.TEXT].split("\n")    # 按行分割
print(f"共分割得到 {len(chunks)} 个文本块：\n")
for i, chunk in enumerate(chunks, start=1):
    print(f"========== 文本块 {i} ==========")
    print(chunk)