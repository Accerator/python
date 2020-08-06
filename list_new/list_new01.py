#列表推导式
#旧的列表———》新的列表

#1.列表推导式 格式：[表达式 for 变量 in 旧列表] 或者 [表达式 for 变量 in 旧列表 if 条件]

names = ['tom', 'lily', 'abc', 'jack', 'bob']
result = [name for name in names if len(name) > 3]
print(result)  # ['lily', 'jack']

result = [name.capitalize() for name in names if len(name) > 3]
print(result)  # ['Lily', 'Jack']

newlist = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print(newlist)  # [15, 30, 45, 60, 75, 90]

newlist = [(x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 != 0]
print(newlist)
#[(0, 1), (0, 3), (0, 5), (0, 7), (0, 9), (2, 1)...]

list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]]
newlist = [i[-1] for i in list]
print(newlist)  # [3, 6, 9, 5]

dict1 = {'name':'tom','salary':5000}
dict2 = {'name':'lily','salary':6000}
dict3 = {'name':'amy','salary':4000}

list = [dict1,dict2,dict3]
newlist = [employee['salary']+200 if employee['salary']>5000 else employee['salary']+500 for employee in list]
print(newlist) #[5500, 6200, 4500]



