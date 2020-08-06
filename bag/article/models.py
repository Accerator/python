class Article:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def show(self):
        print('发表文章名字:{}的作者是:{}'.format(self.name, self.author))


class Tag:
    def __init__(self, name):
        self.name = name
# article = Article('个人总结', '家伟')