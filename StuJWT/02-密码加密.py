from passlib.context import CryptContext

# 创建密码加密上下文对象
crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 对密码进行加密处理
def hash_password(psaaword: str) -> str:
    hash_pw = crypt_context.hash(psaaword)
    return hash_pw

# 验证
def ver_password(plain_pw: str, hash_pw: str) -> bool:
    result = crypt_context.verify(plain_pw, hash_pw)
    return result

if __name__ == '__main__':
    # hp = hash_password("123456")
    # print(hp)
    """
    $2b$12$hCgTBvG4z2IRPqDwCvvDJOD6kzInLwrtk12cItzp6axRQFNGvyrOC
    $2b$12$H1m5peHJT2MtYHNKSUmRLeuw5RnwmrQnp8nRz/zQ9Zyt0KbK19ltm
    """
    # hp = hash_password("123")
    # print(hp)
    """
    $2b$12$10iejQKz70VhksVMy03G2eeWQmtQ4AABDxH1apMd3q0z9cy1ppk.e
    $2b$12$noE.x6Wx7VXd/UXWpNIkb.UZKeuDo5v.9bmdFNQS7DKsthOwUlst2
    """
    plain_pw = "123456"
    hash_pw = "$2b$12$hCgTBvG4z2IRPqDwCvvDJOD6kzInLwrtk12cItzp6axRQFNGvyrOC"
    vp = ver_password(plain_pw, hash_pw)
    print(vp)