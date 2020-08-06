'''
字典 dir
特点：
    1.符号{}
    2.关键字：dir
    3.保存的元素：key：value  一对
'''

#定义

dict1 ={}  #空字典

dict2 = dict()  #空字典   list1 = list() 空列表 tuple = tuple() 空元组

dict3 = {'id':'988552','name':'lucky'}  #{'id': '988552', 'name': 'lucky'}

dict4 = dict([('name','lucky'),('id','988552')])  #{'name': 'lucky', 'id': '988552'}

#注意：list可以转换成字典，但是需要列表中元素成对出现

'''
字典的增删改查：
增加：格式：dict6[key]=value
特点：按照上面的格式，如果在字典中存在同名的key，则发生值的覆盖（后面的值覆盖原来的）。
     如果没有同名的key，则实现的添加功能;(key;value添加到字典当中）
'''

dict6 = {}
dict6['brand'] = 'huawei'
#print(dict6)

dict6['brand'] = 'mi'
print(dict6)

'''
增加元素（key:value);
dict[key] = value ---->{key:value}

特点：key在字典中是唯一的，value值可以是不唯一的
{'name':'tom','name':'aaa'} 错误定义
{'张三',100,'李四',50,'王五',200}

增加元素的对比：
list = []
list.append(element)

dict1 = {}
dict[key] = value

修改：
list1[index] = newvalue
dict1[key]   = newvalue

查询元素
list[index]  -----> element
dicr1[key]   -----> value

取值：字典都是根据key和value值

'''

#列表中找元素的下标
list1 = [3,5,7,8]
print(list1[2])

#字典中找元素根据key
dict5 = {'1':'tom','2':'emy','3':'jack'}
print(dict5['2'])

dict_1 = {'tom':100,'emy':100,'jack':89,'girl':90}
print(dict_1['jack'])

#单独遍历字典的结果是：字典中的key
for i in dict_1:
    print(i)

#字典中的函数：
# item() values() keys()

print(dict_1.items())

#('tom', 100)('emy', 100)('jack', 89)('girl', 90)
for i in dict_1.items():
    print(i)

for key,value in dict_1.items():
    if value > 90:
        print(key)

#values:取出字典中的所有值，保存到列表中
result = dict_1.values()
print(result)

#求所有的学生考试成绩的平均分
for score in dict_1.values():
    print(score)

scores = dict_1.values()
totle = sum(scores)

avg = totle/len(scores)

print(avg)

#找人 ； in 也可以用于字典操作 用于判断元素有没有在字典的key出现
# 8 in list

'''
1.根据key的取值，如果key在字典中不存在则报出keyerror
   dict[key] -----> value
2.字典的内置函数
get(key) -----> value 如果key在字典中没有存在则不会报错，则返回None
get(key,dafault) ----->value 如果key在字典中没有存在则返回default的值
'''

print(dict_1.get('tom',99))

#del dict1['haha'] #keyError

#字典内置函数：删除
#dict.remove('李四') 不存在 不报错
#pop(key[,default]) ----->key: 要删除的键/值对所对应的键
#                         default: 可选参数，给定键不在字典中时必须设置，否者会报错(没有默认值)，此时返回default值

D = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj = D.pop('name')
pop_obj1 = D.pop('马云', '笨蛋')
print(D)
print(pop_obj)     #菜鸟教程
print(pop_obj1)    #笨蛋

#popitem() 方法随机返回并删除字典中的最后一对键和值。
#          如果字典已经为空，却调用了此方法，就报出KeyError异常。

site = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj = site.popitem()
print(pop_obj)  #('url', 'www.runoob.com')
print(site)

'''
其他内置函数：
update() []+[]   合并操作
fromkeys(seq,[default])  fromkeys() 1.函数用于创建一个新字典，以序列 seq 中元素做字典的键，
                                     value 为字典所有键对应的初始值,如果没有返回None
                                    2.如果指定default，则用default替代None的value值
'''

seq = ('Google', 'Runoob', 'Taobao')
#新字典为 : {'Google': None, 'Runoob': None, 'Taobao': None}
dict = dict.fromkeys(seq)
print("新字典为 : %s" %  str(dict))
#新字典为 : {'Google': 10, 'Runoob': 10, 'Taobao': 10}
dict = dict.fromkeys(seq, 10)
print("新字典为 : %s" %  str(dict))
                         

