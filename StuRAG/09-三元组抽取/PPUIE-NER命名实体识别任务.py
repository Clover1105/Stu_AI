from paddlenlp import Taskflow

# 抽取的内容
schema = ['时间', '选手', '赛事名称']

ie = Taskflow(
    'information_extraction',
    schema=schema,
    schema_lang="zh",
    batch_size=1,
    task_path=r'G:\models\PP-UIE-0.5B',
    precision='float16'
)

print(ie("2月8日上午北京冬奥会自由式滑雪女子大跳台决赛中中国选手谷爱凌以188.25分获得金牌！"))