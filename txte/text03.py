#集合set 不重复的特点

s1 = set() #创建空的集合，只能用set

list = [3,5,8,9,1,8,9,7,6,8,9]

#应用：把一个列表快速去重

s3 = set(list)
print(s3)      #{1, 3, 5, 6, 7, 8, 9}

#增删改查

#增加 s1 = set()
s1.add('hello')
s1.add('lucy')

#add() 添加一个元素
#update() 可以添加多个元素

t1 = ('hi','hello1')
s1.update(t1)
print(s1)   #{'hello1', 'hello', 'lucy', 'hi'}

s1.add(t1)
print(s1)   #{('hi', 'hello1'), 'lucy', 'hello', }

#2. 删除  remove 如果元素存在就是删除，不存在就报错keyError pop 随机删除（一般删除第一个元素） clear

s1.remove('hello1')
print(s1)

s1.pop()
print(s1)

s1.clear()
print(s1)

#dicard() 类似remove() 在移除不存在的元素不会报错

#差集 difference()

a = ["a", "b", "c"]
b = ["b", "d"]
set1 = set(a)
set2 = set(b)
set4 = set1 - set2
print(set4)  # {'c', 'a'}

set5 = set1.difference(set2)
print(set5)

#& 交集 intersection()

set6 = set1 & set2
print(set6)

set7 = set1.intersection(set2)
print(set7)

# | 并集  union()

set8 = set1 | set2
print(set8)

set9 = set1.union(set2)
print(set9)

# 对称差集
result = (set1 | set2) - (set1 & set2)
print(result)  # {'a', 'c', 'd'}

result = set1 ^ set2
print(result)

'''
difference_update()
    s1 = s1.difference(s2)
    print(s1)
    相同
    s1.difference_update(s2)
    
intersection_update()  交集并赋值
union_update()         并集并赋值
symmetric_difference_update()   对称差集并赋值
     
'''


