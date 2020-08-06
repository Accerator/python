# 生成器方式二：
# 出现yield关键字，说明就不是函数了 yield = return + 暂停

'''
步骤：
1.定义一个函数，函数中使用yield关键字
2.调用函数，接收调用结果
3.得到的结果就是生成器
4.借助next(),__next__()得到元素
'''


def func():
    n = 0
    while True:
        n += 1
        yield n


g = func()
print(next(g))
print(next(g))

'''
生成器方法：
  __next__()  获取下一个元素
  send(value)  每次向生成器调用传信 第一次用none

'''


def gen():
    i = 0
    while i < 5:
        temp = yield i
        print('temp', temp)
        for x in range(temp):
            print('------->', x)
        print('***********')
        i += 1
    return '没有更多的值了'


g = gen()

# can't send non-None value to a just-started generator
g.send(None)
n1 = g.send(3)
print(n1)
