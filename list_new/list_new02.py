#集合推导式  {}在列表的推导式的基础上，添加了一个去除重复项的功能
list1 = [1, 2, 3, 4, 1, 2, 5, 6, 7]
set1 = {x + 1 for x in list1 if x > 5}
print(set1)

#字典推导式
dict1 = {'a':'A','b':'B','c':'C'}
newdict = {value:key for key,value in dict1.items()}
print(newdict)