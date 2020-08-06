#内部函数
'''
特点：
1.可以访问外部函数的变量
2.内部函数可以修改外部函数的可变类型的变量比如：list1
3.内部函数修改全局的不可不变量时，需要在内部函数声明global变量名
  内部函数修改外部函数的不可变变量时，需要在内部函数中声明；nonlocal变量名
4.locals()查看本地变量有哪些，以字典形式输出
  globals()查看全局变量有那些，以字典的形式输出
'''

#闭包  内部函数每次重新加载，但是 内部函数 访问的仍是同一个外部函数
#在函数中提出概念

'''
条件：
1.外部函数中定义了内部函数
2.外部函数是有返回值的
3.返回的值是：内部函数名
4.内部函数引用了外部函数的变量

格式：
def 外部函数()
    pass
    def 内部函数()
        pass
    return 内部函数
'''

def func():
    a = 100

    def inner_func():
        b = 99
        print(a, b)

    print(locals())
    return inner_func


x = func()
print(x)

#x为内部函数 x加上括号表示调用
x()


def func(a, b):
    c = 10

    def inner_func():
        s = a + b + c
        print(s)

    return inner_func

 # ifunc为inuer_func   ifunc = inner_func
ifunc = func(6, 9)
# 调用函数
ifunc()

def func():
    #声明变量
    n = 100 #局部变量
    list1 = [3,6,9,4]

    #声明内部函数
    def inner_func():
        pass

    #调用内部函数
    inner_func()
    print(list1)

#调用func
func()

list1 = [3, 6, 9, 4]

def func1():
    # 声明变量
    global list1
    n = 100  # 局部变量

    def inner_func1():
        nonlocal n
        for index, i in enumerate(list1):
            list1[index] = i + n
        list1.sort()

        n += 101

    inner_func1()
    print(list1)

func1()

#计数器
def generate_count():
    container = [0]

    def add_one():
        container[0] = container[0] + 1
        print('当前是第{}次访问'.format(container[0]))

    return add_one

#内部函数就是一个计数器
counter = generate_count()

counter()   #当前是第1次访问
counter()   #当前是第2次访问

#闭包的同级的访问

def func():
    a = 100

    def inner_func1():
        b = 90
        s = a + b
        print(s)

    def inner_func2():
        inner_func1()  # 调用inner_func1
        print('----------> inner_func2', a)
        return 'hello'

    return inner_func2  # 0x000002ABC8D89950


f = func()
f()
ff = f()
print(ff)
