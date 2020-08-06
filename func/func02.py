'''
return 返回值
1.return后面可以是一个参数 接收的时候 x = add(1,2)
2.return后面也可以是多个参数，如果是多个参数，如果是多个参数则底层会将多个参数先放到一个元组中
  将元组作为整体的返回  x = add(1,2)  x ---->(1,2,3)
3.接收的时候也可以是多个：return 'hello','world' x,y = ('hello','world') ---->x = 'hello' y='world'
'''

#global 变量的范围
#局部变量  全局变量
#声明在函数外层是全局的，所有函数都是可以访问的

neme = 'what'
def func():
    # 函数内部声明的变量为局部变量，局部变量仅限于在函数内部使用
    global name
    s = 'abcd'
    s += 'x'
    print(s, name)

def func1():
    global name
    print(name)
    name += '会弹吉他'

func()
func1()

