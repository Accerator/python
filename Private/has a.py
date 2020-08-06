'''

has a   
1.对象 与 其成员的 从属关系
 学生类 借阅 了 一本书(书 属于 图书类)
 那么 学生来 has a 图书类
 即 一个类中使用了另一个类
 
2.类型：
    系统类型：
        str int float
        list dict tuple set
    自定义类型
        算是自定义的类，都可以将其当成一种容器
        s = Student()
        s是Student类型的对象       
'''


class Computer:
    def __init__(self, brand, type, color):
        self.brand = brand
        self.type = type
        self.color = color

    def Onlion(self):
        print('正在使用电脑上网...')

    def __str__(self):
        return self.brand + '---' + self.type + '---' + self.color


class Book:
    def __init__(self, bname, author, number):
        self.bname = bname
        self.author = author
        self.number = number

    def __str__(self):
        return self.bname + '---' + self.author + '---' + self.number


class Student:
    def __init__(self, name, computer, book):
        self.name = name
        self.computer = computer
        self.books = []
        self.books.append(book)

    def borrow_book(self, book):
        for book1 in self.books:
            if book1.bname == book.bname:
                print('已经借过这本书了')
                break
        else:
            #添加新书
            self.books.append(book)
            print('添加成功')

    def show_book(self):
        for book in self.books:
            print(book.bname)

    def __str__(self):
        return self.name + '---' + str(self.computer) + '---' + str(self.books)


# 创建对象
computer = Computer('mac', 'mac pro 2018', 'red')
book = Book('盗墓笔记', '三叔', 10)
stu = Student('songsong', computer, book)
print(stu)
#看借了什么书
stu.show_book()
print('------->')
book1 = Book('龙珠', '江南', 10)
stu.borrow_book(book1)
stu.show_book()

