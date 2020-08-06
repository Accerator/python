'''
is a

类之间的继承
例如：PC机 和 工作站 都继承计算机的共同属性
父类 基类(子类)
'''

'''
继承:
    Student，Employee,Doctor --->都属于类
    相同代码  ----> 代码冗余，可读性不高
    
    将相同代码提取 ----> Person类
    Student，Employee,Doctor  ---> 继承Person类

    class Student(Person):
        pass
特点：
    1.如果类中不定义__init__,调用父类 super class的__init__
    2.如果类继承父类也需要定义自己的__init__，就需要在当前类的__init__调用父类__init__
    3.如何调用父类__init__(参数)
      super().__init__(参数)
      super(类名，参数).__init(参数)
    4.如果父类有eat(),子类也定义一个eat方法。默认搜索的原则：先找当前类，再去找父类
      s.eat()
      override:重写
      父类提供的方法不能满足子类的需求，就需要在子类中定义一个同名的方法。这种行为：重写
    5.子类的方法中也可以调用父类的方法：、
      super().方法名(参数)
'''

class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name+'正在吃饭。。。')

    def run(self):
        print(self.name+'正在跑步。。。')

class Student(Person):
    def __init__(self,name,age,clazz):
        #调用父类对象
        super().__init__(name,age) #super() 父类对象
        self.clazz = clazz

    def Study(self,course):
        print('{} studying {}'.format(self.name,course))

    def eat(self):
        print(self.name+'正在吃饭，喜欢吃粉浆饭')

class Employee(Person):
    def __init__(self,name,age,salary):
        #调用父类对象
        super().__init__(name,age) #super() 父类对象
        self.salary = salary


class Doctor(Person):
    def __init__(self,name,age,salary,patient):
        #调用父类对象 进行了一个类型的判断
        super(Doctor,self).__init__(name,age) #super() 父类对象
        self.salary = salary
        self.patient = patient

s = Student('jack',18,2)
s.run()
s.Study('python')
s.eat()

e = Employee('tom',20,5000)
e.run()
list1 = ['tom','amy','lidy']
d = Doctor('amy',12,5000,list1)
d.run()