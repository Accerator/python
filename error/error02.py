def func():
    stream = None
    try:
        stream = open(r'D:\p1.txt')
        container = stream.read()
        print(container)
        return 1
    except Exception as err:
        print(err)
        return 2
    finally:
        print('----finally----')
        if stream:
            stream.close()
        return 3

x =func()
print(x) #返回3 finally 覆盖了上一个return

#抛出异常

def register():
    username =input('输入用户名')
    if len(username) < 6:
        raise Exception('用户长度必须六位以上')
    else:
        print('输入的用户名为是：',username)

try:
    register()
except Exception as err:
    print(err)
    print('注册失败！')
else:
    print('注册成功')