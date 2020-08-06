# 类方法

'''
特点：
1.定义需要依赖装饰器@classmethod
2.类方法中参数不是一个对象，而是类
  print(cls)  #<class '__main__.Dog'>
3.类方法中只可以传类属性
4.类方法中不可以使用普通方法

作用：
因为只能访问类属性和类方法，所以可以在对象创建之前，如果需要完成的一些动作(功能)
'''


class Dog:
    def __init__(self, nickname):
        self.nickname = nickname

    def run(self):
        print('{}在院子里玩'.format(self.nickname))

    def eat(self):
        print('eat...')
        self.run()  # 类中方法的调用，需要通过self.方法名()

    @classmethod
    def text(cls):
        print(cls)  # <class '__main__.Dog'>
        # print(cls.nickname) 报错


d = Dog('dahuang')
d.text()

'''
静态方法：很类似类方法
1.需要装饰器@staticmethod
2.静态方法是无需传递参数(self,cls)
3.也只能访问类的属性和方法，对象的是无法访问的
4.加载时间同类方法

总结：
类方法 静态方法
 1.装饰器不同
 2.类方法有参数，静态无参数
 
相同：
 1.只能访问类的属性和方法，对象的是无法访问的
 2.都可以通过类名调用访问
 3.都可以在创捷对象之前使用，因为是不依赖于对象的

普通方法 与两者区别
'''

class Person1:
    __age = 18

    def __init__(self,name):
        self.name = name

    def show(self):
        print('------>', Person1.age)  #私有化，被藏起来了

    @classmethod
    def undate_age(cls):
        cls.__age = 20
        print('------>类方法')

    @classmethod
    def show_age(cls):
        print('update_age:',cls.__age)

    @staticmethod
    def text():
        print('------->静态方法')
        print(Person1.__age)

Person1.undate_age()
Person1.show_age()
Person1.text()

