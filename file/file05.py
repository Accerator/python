import os
#获取当前目录
dir = os.getcwd()
print(dir)

all = os.listdir(r'D:\p1')  #返回指定目录下所有的文件和文件夹，保存到列表中
print(all)

#创建文件夹
if not os.path.isdir(r'D:\p3'):
    f = os.mkdir(r'D:\p3')
    print(f)

#删除空的文件夹
f = os.rmdir(r'D:\p3')
print(f)

f = os.removedirs(r'D:\p3')
print(f)

os.remove(r'D:\p3\aa.txt')

#删除p4文件夹
path = r'D:\p3\p4'

filelist = os.listdir(path)

for file in filelist:
    path1 = os.path.join(path,file)
    os.remove(path1)
else:
    os.rmdir(path)

print('ok')

#切换目录
os.chdir(r'D:\p1')
print(f)
path = os.getcwd()
print(path)