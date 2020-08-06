dict = {'1': 'c', '2': 'c++', '3': 'python'}

#1.将字典进行拆包成为关键字的形式
#2.func里面都是关键字参数
#3.将关键字再进行一次装包动作

def func(**kwargs):
    print(kwargs)

func(**dict)


name = 'tom'

def func1():
    a = 'abcd'
    a += 'X'
    print(a, name)

def func2():
    global name
    print(name)
    name+='会弹吉他'
    print(name)

func1()
func2()

'''
闭包：
内部函数每次重新加载，但是 内部函数 访问的仍是同一个外部函数

缺点：
1.作用域没有那么重要
2.因为变量不会被垃圾回收所以有一定的内存

作用：
1.考研使用同级的作用域
2.读取其他元素的变量
3.延长作用域

总结：
1.闭包优化了变量，原来需要类的对象完成的工作，闭包也可以完成
2.由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存
3.好处是使代码更加的简洁，便于阅读
4.装饰器的基础

'''

#闭包
def func1():
    def func_son():
        a = 10
        print(a)

    return func_son  # 不加(), 返回的是函数，不是调用函数


x = func1()           # x 即为 func_son
x()                  # 给x加() 即 调用 func_son()


def func(number):
    a = 100

    def inner_func():
        nonlocal a
        for i in range(number):
            a += 1
        print('修改后的a：', a)

    return inner_func


f = func(5)
f()


# 地址引用
def text():
    print('-------text-----')


t = text
# text 和 t 地址相同  text()  t()

def func1(f):
    print(f)   #<function text at 0x000001C477CE9840>
    f()        #-------text-----
    print('--------->func')

func1(text)


'''
装饰器
特点：
1.函数A是作为参数出现的（函数B就接收函数A作为参数）
2.要有闭包的特点
'''

def decorate(func):
    a = 100
    print('wrapper外层打印测试')

    def wrapper():
        func()
        print('--------->刷漆')
        print('--------->铺垫版',a)

    print('wrapper加载完成......')
    return wrapper

#使用装饰器
@decorate
def house():
    print('我是毛坯房')
house()
'''
1.house被装饰函数
2.将被装饰函数作为参数传个decorate
3.执行decorate函数
4将返回值又赋值给house
'''

