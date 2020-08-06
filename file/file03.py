import os

#文件路径查找(绝对路径)  os.path.dirname(_file_)
#文件路径拼接           os.path.join(path,'')

with open(r'D:\aa.jpg', 'rb') as stream:
    container = stream.read()
    print(stream.name)
    file = stream.name
    filename = file[file.rfind('\\') + 1]

    path = os.path.dirname(__file__)
    path1 = os.path.join(path, 'a1.jpg')

    with open(r'D:\百度云\aa.jpg', 'wb') as wstream:
        wstream.write(container)
print('文件复制完成')

