# 加密算法: md5 sha1  sha256
# base64
import hashlib

msg = '于鹏中午一起吃饭去！'
md5 = hashlib.md5(msg.encode('utf-8'))

print(len(md5.hexdigest()))  # b1a0c31ad20f8f982923f61f8003d8a9   32

sha1 = hashlib.sha1(msg.encode('utf-8'))
print(len(sha1.hexdigest()))  # 40

sha256 = hashlib.sha256(msg.encode('utf-8'))
print(len(sha256.hexdigest()))  # 64


password ='123456'

list1 = []

sha256 = hashlib.sha256(password.encode('utf-8'))
list1.append(sha256.hexdigest())

pwd = input('输入密码:')
sha256 = hashlib.sha256(pwd.encode('utf-8'))
pwd = sha256.hexdigest()
print(pwd)
print(list1)
for i in list1:
    if pwd == i:
        print('登录成功！')

