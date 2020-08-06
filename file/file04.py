import os

'''
absolute 绝对的
同级别的可以直接进
r = os.path.isabs(r'..\p1.txt')  # ..\表示返回当前文件的上一级 code
'''

r = os.path.isabs(r'D:\p1.txt')
print(r)

#获取路径
#当前文件所在文件夹的绝对路径
path = os.path.dirname(__file__)
print(path)    #F:/python/新建文件夹/file

#通过相对路径得到绝对路径
path = os.path.abspath('aa.txt')
print(path)  #F:\python\新建文件夹\file\aa.txt

#当前文件所在文件夹的绝对路径
path = os.path.abspath(__file__)
print(path)    #F:\python\新建文件夹\file\file04.py

path = os.getcwd()
print(path)   #F:\python\新建文件夹\file

path = os.path.join(os.getcwd(),'a','a.txt')
print(path)   #F:\python\新建文件夹\file\a\a.txt

path = r'F:\python\新建文件夹\file\file04.py'
result = os.path.split(path)
print(result)    #('F:\\python\\新建文件夹\\file', 'file04.py')
print(result[1]) #file04.py

#分割文件与扩展名
result = os.path.splitext(path)
print(result)    #('F:\\python\\新建文件夹\\file\\file04', '.py')

#获取文件大小  字节
size = os.path.getsize(path)
print(size)      #1067