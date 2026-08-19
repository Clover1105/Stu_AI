from langchain_ollama import ChatOllama
import os
from dotenv import load_dotenv
load_dotenv()
import json

def intention_recognition(question):
    llm = ChatOllama(
        model=os.getenv("OLLAMA_MODEL_NAME"),
        base_url=os.getenv("OLLAMA_BASE_URL"),
    )

    intention_prompt = """
        角色设定：
            你是一个专业的法律意图识别助手。你的任务是分析用户的输入，判断其是否包含法律相关的内容或诉求。
        判定标准：
            相关：用户的问题涉及法律法规、司法程序、合同协议、纠纷解决、维权咨询、法律责任、行政处罚、婚姻家庭法律事务、知识产权、劳动法等。即使问题表述口语化或存在错别字，只要核心诉求是寻求法律层面的解答或帮助，均判定为“相关”。
            不相关：用户的问题仅涉及日常闲聊、通用知识问答、情感倾诉（无法律诉求）、纯技术问题、娱乐八卦等，不包含任何法律要素。
        输出要求：
            仅输出一个JSON对象，不要包含任何其他解释文字：
            {
                "is_legal": True/False,
                "confidence": "high/medium/low",
            }
            不要输出任何解释、标点符号或其他多余的文字。
        示例参考：
            用户输入：老板拖欠工资三个月了，我该怎么办？
            输出：{"is_legal": true, "confidence": "high"}
            用户输入：今天天气真好，适合去公园散步。
            输出：{"is_legal": false, "confidence": "high"}
            用户输入：我朋友出轨了，我好难过，不知道该怎么安慰她。
            输出：{"is_legal": false, "confidence": "high"}
            用户输入：邻居家的树长到我家院子了，好烦。
            输出：{"is_legal": false, "confidence": "medium"}
        待分析的用户输入：
            {question}
        输出：
    """

    rs = llm.invoke([
        {"role": "system", "content": intention_prompt},
        {"role": "user", "content": question}
    ])
    # print(f"\n意图识别结果 -- rs: {rs}\n")
    """
    意图识别结果 -- rs: 
    content='{"is_legal": false, "confidence": "high"}' 
    additional_kwargs={} 
    response_metadata={'model': 'qwen2.5:7b', 'created_at': '2026-08-07T01:06:03.9603814Z', 'done': True, 'done_reason': 'stop', 'total_duration': 40265647800, 'load_duration': 23917345700, 'prompt_eval_count': 366, 'prompt_eval_duration': 15495132000, 'eval_count': 13, 'eval_duration': 826864000, 'logprobs': None, 'model_name': 'qwen2.5:7b', 'model_provider': 'ollama'} 
    id='lc_run--019fd9c0-d6ef-74a1-b958-89e1ac08aea9-0' 
    tool_calls=[] 
    invalid_tool_calls=[] 
    usage_metadata={'input_tokens': 366, 'output_tokens': 13, 'total_tokens': 379}
    """
    return json.loads(rs.content)   # loads() -- JSON转换为字典

# 测试
if __name__ == "__main__":
    re = intention_recognition("今天天气真好，适合去公园散步。")
    print(re)
    print(type(re))


