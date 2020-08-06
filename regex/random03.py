# random 模块

import random

ran = random.random()  # 0~1之间的随机小数
print(ran)

ran = random.randrange(1, 10, 2)  # randrange(start,stop,step)  1~10 step=2 ---> 1,3,5,7,9
print(ran)

ran = random.randrange(1, 10)  # randrange(start,stop,step)  1~10 step=2 ---> 1,3,5,7,9
print(ran)

ran = random.randint(1, 10)
print(ran)

list1 = ['学强', '飞飞', '家伟', '鹏', '阿文']
ran = random.choice(list1)  # 随机选择列表的内容
print(ran)

pai = ['红桃A', '方片K', '梅花8', '黑桃J']
result = random.shuffle(pai)  # 打乱顺序
print(pai)

# 验证码  大小写字母与数字的组合
def func():
    code =''
    for i in range(4):
        ran1= str(random.randint(0,9))
        ran2 = chr(random.randint(65,90))  #
        ran3 = chr(random.randint(97,122))

        r = random.choice([ran1,ran2,ran3])

        code +=r
    return code

code = func()
print(code)