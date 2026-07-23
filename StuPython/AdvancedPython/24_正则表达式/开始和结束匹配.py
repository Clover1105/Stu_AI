"""
- ^：匹配字符串开头
- $：匹配字符串结尾
"""

import re

text = "hqyj66abc hqyj123"

# 匹配开头的hqyj后跟数字
data1 = re.findall("^hqyj\\d+", text)
print(f"^开头匹配：{data1}")

# 匹配结尾的hqyj后跟数字
data2 = re.findall("hqyj\\d+$", text)
print(f"$结尾匹配：{data2}")