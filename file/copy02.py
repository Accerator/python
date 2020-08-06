import os

#文件复制
src_path = r'D:\p1'
target_path = r'D:\p3'

filelist = os.listdir(src_path)
print(filelist)


def copy(src_path, target_path):
    #获取文件夹中的目录
    filelist = os.listdir(src_path)
    #遍历列表
    for file in filelist:
        #拼接路径
        path = os.path.join(src_path, file)
        #判断是否为文件夹
        if os.path.isdir(path):
            #递归调用
            copy(path, target_path)
        else:
            #不是文件夹直接复制
            with open(path, 'rb') as rstream:
                container = rstream.read()

            path1 = os.path.join(target_path, file)
            with open(path1, 'wb') as wstream:
                wstream.write(container)
    else:
        print('复制完成')


#调用函数
copy(src_path,target_path)
