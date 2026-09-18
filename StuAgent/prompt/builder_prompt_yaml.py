import os
import yaml

class BuilderPromptYaml:
    _prompt = None

    # 定义静态函数
    @staticmethod
    def get_prompt(file_name):
        # 获取yaml文件所在目录
        dirname = os.path.dirname(os.path.abspath(__file__))
        # 拼接yaml文件路径
        file_path = os.path.join(dirname, file_name)
        # 读取yaml文件，转为python数据类型
        with open(file_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        # print(config)
        # print(type(config)) # <class 'dict'>

        # 字符串拼接 -- 构建提示词
        BuilderPromptYaml._prompt = f"""
        1. 角色：{config['role']}\n2. 任务：{"\n".join(config['task'])}\n3. 规则：{"\n".join(config['rule'])}\n
        """
        return BuilderPromptYaml._prompt.strip()


"""
os.path.abspath(__file__) -- 获取当前文件的绝对路径
os.path.dirname(os.path.abspath(__file__)) -- 获取当前文件的父目录
"""
if __name__ == '__main__':
    rs = BuilderPromptYaml.get_prompt("send_email_agent.yaml")
    print(rs)


