#文件操作
'''
文件上传

系统函数：
open() 默认读文本文件
'''
# 读
stream = open(r'D:\aa.txt')
container = stream.read()
print(container)

result = stream.readable()  # 判断
print(result)

line = stream.readline()  # 因为上面已经读完了，所以没有读到东西
print(line)  # 读一行 每读一行就换行

stream = open(r'D:\aa.jpg', 'rb')
container1 = stream.read()
print(container1)
