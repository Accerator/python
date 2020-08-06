class Phone:
    #魔术方法之一：称为魔术方法 __名字__()
    def __init__(self):
        self.brand = 'xiaomi'
        self.price = 4999

    def call(self):
        print('------------>call')
        print('价格',self.price) #不能保证每个self中都存在



p1 = Phone()
p1.price = 5999
p1.call()
print(p1.price)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self,food):
        print('{}正在吃{}！'.format(self.name,food))

    def run(self):
        print('{},今年{}，正在跑步'.format(self.name,self.age))

p = Person('lisi',20)
p.name = '李四'
p.eat('狮子头')
p.run()

p1 = Person('王五',30)
p1.name = 'wangwu'
p1.eat('红烧肉')