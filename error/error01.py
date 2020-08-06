#异常:程序运行的时候报出来的
'''
def chu(a,b):
    return a/b
#ZeroDivisionError: division by zero
chu(1,0)   
'''

#异常处理
'''
情况一：
try:
    可能出现异常的代码
    
except：输入的异常类型
    如果有异常执行的代码
    
except：输入的异常类型
    如果有异常执行的代码
    
except Exception:
     如果有异常执行的代码   
     
finally:
    无论是否异常都会被执行的代码
    
情况二：   
try:
    可能出现异常的代码
    
except：输入的异常类型
    如果有异常执行的代码
    
except：输入的异常类型
    如果有异常执行的代码
    
except Exception as err:  
    print('出错了',err)  #明确原因是什么
     
finally:
    无论是否异常都会被执行的代码
'''


def func():
    try:
        p1 = int(input('请输入一个数字'))
        p2 = int(input('请输入一个数字'))
        per = input('请输入运算符')
        result = 0
        if per == '+':
            result = p1 + p2
        elif per == '-':
            result = p1 - p2
        elif per == '*':
            result = p1 * p2
        elif per == '/':
            result = p1 / p2
        print('答案为：', result)

        #文件操作
        with open(r'D:\p1.txt','r') as wstream:
            print(wstream.read())

    except ZeroDivisionError:
        print('除数不能为0！！！')
    except ValueError:
        print('必须输入数字')
    except FileNotFoundError:
        pass
    except Exception as err:
        print('出错了',err)  #明确原因是什么

func()
