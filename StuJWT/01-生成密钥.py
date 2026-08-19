import secrets

# 生成32位随机字符组成的字符串密钥
mi_key = secrets.token_urlsafe(32)
print(mi_key)