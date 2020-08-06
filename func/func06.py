#匿名函数：简化函数的定义
#格式：lambda 参数一，参数二... ：运算

'''
def func1():
    s = a + b
    return a
    
f = func1
f()
'''

s = lambda a, b,: a + b
print(s)  #函数<function>

result = s(1,2)
print(result)

#匿名函数作为参数
def func(x, y, func):
    print(x, y)
    print(func)
    s = func(x, y)
    print(s)

#调用匿名函数
func(1, 2, lambda a, b: a + b)

list1 = [3, 6, 9, 10, 12]
m = max(list1)
print(m)

list2 = [{'a': 10, 'b': 11}, {'a': 18, 'b': 15}, {'a': 14, 'b': 16}]
m = max(list2, key=lambda x: x['a'])
print(m)

# map()
list3 = [3, 4, 5, 9, 5, 8, 7, 6]

result = map(lambda x: x + 2, list3)
print(list(result))  # [5, 6, 7, 11, 7, 10, 9, 8]

func = lambda x:x if x%2==0 else x+1
result = func(5)
print(result)

result = map(lambda x:x if x%2==0 else x+1,list3)
print(list(result))

# reduce()  对列表函数进行加减乘除

from functools import reduce

tuple1 = (3, 5, 7, 8, 9, 1)

result = reduce(lambda x, y: x + y, tuple1)
print(result)

tuple2 = (1,)
# reduce(function, sequence, initial=None)
result = reduce(lambda x, y: x + y, tuple2, 10)
print(result)

list5 = [12, 8, 9, 15, 13, 8]

result = filter(lambda x: x > 10, list5)
print(list(result))

list7 = [{'name':'mack','age':11},
         {'name':'jack','age':12},
         {'name':'tom','age':23}
        ]
result = filter(lambda x:x['age']>20,list7)
print(list(result))

r1 = sorted(list7,key=lambda x:x['age'],reverse=True)
print(r1)

#递归函数
'''
1.递归函数必须要特定的终点
2.通常有一个入口

'''
def sum(n):
    if n == 0:
        return 0
    else:
        return n+sum(n-1)

result = sum(10)
print(result)