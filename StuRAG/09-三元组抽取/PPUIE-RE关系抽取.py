from paddlenlp import Taskflow

# 抽取的内容 --- 竞赛名称：起始实体；主办方、承办方、时间：关系
# 是在给 PaddleNLP 的 UIE（信息抽取）模型定义"抽取模式"，也就是告诉模型：你要从文本里抽什么、按什么结构抽。
# 这是一个字典，结构是 {主体类型: [要抽取的属性列表]}
schema = {'竞赛名称': ['主办方', '承办方', '时间']}

ie = Taskflow(
    'information_extraction',
    schema=schema,
    schema_lang="zh",
    batch_size=1,
    task_path=r'G:\models\PP-UIE-0.5B',
    precision='float16'
)

print(ie('2022年的语言与智能技术竞赛由中国中文信息学会和中国计算机学会联合主办，'
       '百度公司、中国中文信息学会评测工作委员会和中国计算机学会自然语言处理专委会承办，'
       '已连续举办4届，成为全球最热门的中文NLP赛事之一。'))