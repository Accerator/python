# 写  会覆盖原文件
'''
    'r'       open for reading (default)                                       读
    'w'       open for writing, truncating the file first                      写
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists  追加
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
方法：
  write(内容)  每次都会将原来的内容清空，然后写当前的内容
  writelines   没有换行效果，必须自己加
'''
stream = open(r'D:\aa.txt', 'w')
s = 'hello underworld'
result = stream.write(s)
stream.write('hahaha')
stream.writelines(['where\n', 'when\n', 'how\n'])
print(result)

stream.close()

#文件的复制
'''
with与open联用可以自动释放资源

'''
with open(r'D:\aa.jpg', 'rb') as stream:
    container = stream.read()
    with open(r'D:\百度云\aa.jpg', 'wb') as wstream:
        wstream.write(container)
print('文件复制完成')
