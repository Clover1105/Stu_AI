"""
包别名导入
    - import 包名.模块名 as 别名
    - from 包名 import 模块名 as 别名
"""

# 目录结构：
# data/
#   __init__.py
#   json_parser.py
#   xml_parser.py


# 给模块取别名
import data.json_parser as json
from data import xml_parser as xml

json_result = json.parse('{"name":"张三"}')
xml_result = xml.parse('<name>张三</name>')

print(json_result)
print(xml_result)