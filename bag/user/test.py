'''
  article
     |--models.py
     |--__init__.py
     |-- ....
  user
     |-- models.py
          |-- User
     |--__init__.py
     |-- test.py
'''

# 用户发表文章
# 创建用户对象

# from user.models import User
import sys

from user.models import User
from article.models import Article
# from .models import User  # 当前目录下的models里面的User类

user = User('admin', '123456')  # ----》user就是通过导入User类创建的

# 发表文章，文章对象
article = Article('个人总结', '家伟')

user.publish_article(article)

list1 = [1, 3, 5, 6, 7]

from calculate import add

result = add(*list1)
print(result)

MAX = 1000

print(sys.path)