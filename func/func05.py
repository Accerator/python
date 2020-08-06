# 登陆校验
'''
如果装饰器有多个，谁距离最近先装饰谁
'''
import time


def decorate(func):    #[] {}
    def wrapper(*args,**kwargs):
        print("正在校验中...")
        time.sleep(2)
        print("校验完成。")
        # 调用原函数
        func(*args,**kwargs)

    return wrapper


@decorate
def f1(n):
    print('-----f1------',n)

@decorate
def f2(name,age):
    print('-----f2------',name,age)

@decorate
def f3(name,clazz='1904'):
    print('{}班级的学生如下'.format(clazz))
    for stu in name:
        print(stu)

f1(5)
f2('tom',20)

name= ['tom','lidy','amy']
f3(name,clazz='1904')


# 装饰器带参数
'''
带参数的装饰器是三层
最外层的函数负责接收装饰器参数
里面的内容还是原装饰器的内容
'''
def outer(a):
    def decorate(func):
        def wrpper(*args, **kwargs):
            func(*args)
            print('----->铺地板{}块'.format(a))

        return wrpper

    return decorate


@outer(10)
def house(time):
    print(time)

house('2019-6-12')
