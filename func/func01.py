# 可变参数+关键字参数
# 关键字参数：key = value

def add(a, b=10):
    result = a + b
    print(result)


# 调用
add(2)

add(4, 7)  # 此时7会覆盖原值


def func(**kwargs):
    print(kwargs)


# 调用

func(a=1, b=2, c=3)  #关键字参数 {'a': 1, 'b': 2, 'c': 3}




