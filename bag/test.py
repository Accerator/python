# class Person:
#     def __init__(self):
#         self.__money = 200
#         self.name = '匿名'
#
#     def show1(self):
#         print(self.name,self.__money)
#
#
# class Student(Person):

#     def __init__(self):
#         # super().__init__()
#         # super(Student, self).__init__()
#         Person.__init__(self)
#         self.__money = 500
#
#     def show(self):
#         print('money:', self.__money)
#
#
# s = Student()
# s.show()
# s.show1()


#
# class Person:
#     def __init__(self,a):
#         self.a = a
#
#     def show(self):
#         print(self.a)
#
#
# class Student(Person):
#     def __init__(self,a):
#         super().__init__(a)
#         self.a = 200
#
# s = Student(100)
# s.show()
#
#
#
# class Person:
#     def __init__(self,a):
#         self. a = a
#
#     def show(self):
#         print(self.a)
#
# class Student(Person):
#     def __init__(self,a):
#         self.a = 200
#         super().__init__(a)
#
# s = Student(100)
# s.show()


class A:
    def __new__(self):
        self.__init__(self)
        print("A's __new__() invoked")

    def __init__(self):
        print("A's __init__() invoked")


class B(A):
    def __new__(self):
        print("B's __new__() invoked")

    def __init__(self):
        print("B's __init__() invoked")


def main():
    b = B()
    a = A()


main()