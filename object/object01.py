'''
class 类名[(父类)]：
    属性：特征
    
    方法：动作
'''

'''
普通方法格式：
def 方法名（self[,参数,参数]
    pass
'''


class Phone:
    brand = '华为'
    price = 4999
    type = 'mate 80'

    # 普通方法
    def call(self):
        print(self)
        print('正在打电话...')
        print('正在访问通信录：')
        for person in self.address_book:
            print(person.items())
        print('留言：',self.note)   #不能保证每个self都有note

    #魔术方法之一：称为魔术方法 __名字__()
        def __int__(self):
            print('----------->init')


print(Phone)  # <class '__main__.Phone'>

phone = Phone()
phone.note = 'haha'
phone.address_book = [{'13578718521':'tom'},{'13778718525':'amy'}]
print(phone.brand)
phone.call()

phone1 = Phone()
phone1.note = 'what'
phone1.call()