'''
元组：
类似列表（当成容器）
特点：
1.定义的符号()
2.元组中的内容不可修改
3.关键字：tuple
    列表              元组
     []               （）
    [1,2]             （1，2）
    
4.符号
+                *
is not       is not in

函数：
max() min() sum() len() sorted() tuple()

元组自带函数：
index()
count()

拆装包：
x,*y = (1,2,3,4,5)
print(y)
print(*y)
'''

t1 = ()
print(type(t1))  #<class 'tuple'>

t2 = ('hello',)
print(type(t2))

t3 = ('aa','bb')
print(type(t3))

#变量个数与元组个数不一致
t1 = (2,5,8,9,10)
a,*_,c = t1
print(a,c,_) # 2 10 [5,8,9]

a,b,*c = t1
print(a,b,c) # 2 5 [8,9,10]

t1 = (9,)
a,*b =t1
print(a,b) #*b表示未知数个数0~n，0--[] 多个元素的话~[1,2,3...]

t2 = (4,5)+(1,2) #(4, 5, 1, 2)
print(t2)

t3 = (3,4)*2
print(t3)   #(3, 4, 3, 4)