from chat.dao import HistoryDao

def query_history_menu(username):
    # 获取结果
    results = HistoryDao.query_history_menu(username)
    # 包装结果
    data_list = []
    for item in results:
        data_list.append({
            'historyId': item['history_id'],
            'title': item['question'],
            'time': item['create_time'].strftime('%Y-%m-%d %H:%M:%S'),
            "active": "false"
        })
    # print(f"\n查找菜单栏结果 -- data_list: {data_list}\n")
    # 查找菜单栏结果 -- data_list: [{'historyId': 4, 'title': '你好！', 'time': '2026-08-04 10:57:05', 'active': 'false'}]
    return {
        'code': 200,
        'msg': '查询成功',
        'data': data_list
    }

# 查询某条历史记录详情
def conversation_log(historyId):
    results = HistoryDao.conversation_log(historyId)
    # print(f"\n查找记录详情结果 -- results: {results}\n")
    """
    查找记录详情结果 -- results: 
    [{'question': 'hello', 'answer': "Hey! 👋 What's up?"}, 
    {'question': '你是谁?', 'answer': '你好呀！我是千问，是由阿里巴巴集团开发的AI助手。你也可以亲切地叫我“小酒窝”，这是我的数字人形象哦。\r\n不管你是想聊天、查资料，还是需要我帮你办点事，随时都可以找我！'}, 
    {'question': '一句话描述成都今天的天气', 'answer': '成都今天（8月4日）天气晴朗，气温在22~34℃之间，紫外线较强，体感闷热，外出需注意防暑防晒。'}, 
    {'question': '下午好！', 'answer': '下午好呀！☕️ 今天过得怎么样？有什么我可以帮你的吗，或者只是想随便聊聊天也可以哦~'}]
    """
    data_list = []
    for item in results:
        data_list.append({
            'role': 'user',
            'content': item['question']
        })
        data_list.append({
            'role': 'assistant',
            'content': item['answer']
        })
    return {
        'code': 200,
        'msg': '查询成功',
        'data': data_list
    }

def delete_history(historyId):
    result = HistoryDao.delete_history(historyId)
    if not result:
        return {
            'code': 500,
            'msg': '删除历史记录失败',
            'data': None
        }
    return {
        'code': 200,
        'msg': '删除历史记录成功',
        'data': None
    }

def search_history(username, searchHistory):
    results = HistoryDao.search_history(username, searchHistory)
    # 包装结果
    data_list = []
    for item in results:
        data_list.append({
            'historyId': item['history_id'],
            'title': item['question'],
            'time': item['create_time'].strftime('%Y-%m-%d %H:%M:%S'),
        })
    return {
        'code': 200,
        'msg': '搜索历史记录成功',
        'data': data_list
    }

# 测试
if __name__ == '__main__':
    # print(query_history_menu('clover'))
    # print(conversation_log(1)['data'])
    # print(delete_history(12))
    print(search_history('clover', '你'))