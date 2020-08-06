# 私有化
# 封装：1.私有化属性 2.定义公有set和get
# __属性：就是将属性的私有化，访问范围仅仅限于类中

'''
好处：
1.隐藏属性不被修改

2.也可以修改，通过函数
   def setXXX(self,xxx)
   
3.筛选赋值内容
    if xxx是否符合条件:
        赋值
    else:
        不赋值
        
4。如果想要获取一个具体的某一个属性
   用get函数
   def getXXX(self):
        return self.__xxx
        
'''


class Person(object):
    # __age = 18

    def __init__(self, name, age):
        self.__name = name  # 私有化 外界无法修改
        self.__age = age

    # 定义公有的set get 方法：赋值 取值
    def setAge(self, age):
        if age > 0 and age < 120:
            self.__age = age
        else:
            print('输入age 年龄参数 不合法')

    def setName(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            print('请输入string类型的名字')

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def __str__(self):
        return '姓名：{} 年龄:{}'.format(self.__name, self.__age)


jam = Person('尚尚', 20)

# print(jam.__age)      # 无法访问私有
# jam.__age = 21      # 修改失败

jam.setAge(99)
jam.setName('JamSang')

print(jam.getAge())

# dir() 显示的，均可以 通过 .方法调用
print(dir(Person))
print(dir(jam))
print(jam.__dir__())  # 同dir(jam)
# 并非真正的私有，仍可以访问，但不建议
print(jam._Person__age)


class Person1(object):
    # __age = 18

    def __init__(self, name, age):
        self.name = name  # 私有化 外界无法修改
        self.__age = age

    def setName(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            print('请输入string类型的名字')

    def getName(self):
        return self.name

    # 使用装饰器来进行私有化
    @property  # 这是个类 做的装饰器
    def age(self):      # 功能同getAge，可以直接调用
        return self.__age

    # @property.setter
    @age.setter         # 此处age是上面@property装饰的age，功能同 set
    def age(self, age):
        if 0 < age < 120:
            self.__age = age
        else:
            print('输入age 年龄参数 不合法')

    def __str__(self):
        return '姓名：{} 年龄:{}'.format(self.name, self.__age)

jam = Person1('Jam', 18)
print(jam.age)
jam.age = 20
print(jam.age)