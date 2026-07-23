# 思考题
def fun(n=None,o=None):
    print(o)
    def fn(m):
        return fun(m,n)
    return fn
a=fun("华")("清")
a("远")
a("见")
b=fun("华")("清")("远")
b("见")

# 思考过程见图片