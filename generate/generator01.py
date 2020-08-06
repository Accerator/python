'''
得到生成器的方式：
1.通过列表推导式得到生成器

'''

#得到生成器
newlist = (x*3 for x in range(5))
print(type(newlist))

#方式一：通过调用__next__方式得到元素
print(newlist.__next__()) #0
print(newlist.__next__()) #3

#方式二： next()
#每调用一次next则会产生一个元素
#异常：StopIteration
print(next(newlist))      #6
print(next(newlist))      #9

newlist1 = (x*4 for x in range(5))

while True:
    try:
        e = next(newlist1)
        print(e)
    except:
        print('没有更多的元素了')
        break


