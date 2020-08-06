# 进程>线程>协程

def task(n):
    for i in range(n):
        print('搬第{}块砖'.format(i+1))
        yield None

def task1(n):
    for i in range(n):
        print('听第{}首歌'.format(i+1))
        yield None

g1 = task(5)
g2 = task1(5)
while True:
    try:
        g1.__next__()
        g2.__next__()
    except:
        break


