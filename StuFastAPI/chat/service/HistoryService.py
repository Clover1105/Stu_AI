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
    return {
        'code': 200,
        'msg': '查询成功',
        'data': data_list
    }

# 查询某条历史记录详情
def conversation_log(historyId):
    results = HistoryDao.conversation_log(historyId)
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

# 测试
if __name__ == '__main__':
    # print(query_history_menu('clover'))
    print(conversation_log(1)['data'])