import re

# 分组
# 匹配数字0-100数字
n = '100'
'''
| 或者  
() 分组 （163|126|qq）  一组
'''
# 改进版
result = re.match(r'[1-9]?\d?$|100$', n)
print(result)

# (word|word|word)  区别   [163] 表示的是一个字母而不是一个单词
# 验证输入的邮箱 163  126  qq
email = '73877884@163.com'
result = re.match(r'\w{5,20}@(163|126|qq)\.(com|cn)$', email)
print(result)

# 不是以4、7结尾的手机号码(11位)

phone = '15901018869'
result = re.match(r'1\d{9}[0-35-689]$', phone)
print(result.group())

# 爬虫
phone = '010-12345678'

result = re.match(r'(\d{3}|\d{4})-(\d{8})$', phone)
print(result)

# 分别提取
print(result.group())
# () 表示分组  group(1) 表示提取到第一组的内容   group(2)表示第二组的内容
print(result.group(1))
print(result.group(2))

#
msg = '<html><h1>abc</h1>'
msg1 = '<h1>hello</h1>'

result = re.match(r'<[0-9a-zA-Z]+>(.+)</[0-9a-zA-Z]+>', msg)
print(result)
print(result.group(1))

# number
result = re.match(r'<([0-9a-zA-Z]+)>(.+)</\1>$', msg1)
print(result)
print(result.group(1))
print(result.group(2))

#
msg = '<html><h1>abc</h1></html>'

result = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$',msg)
print(result)

print(result.group(1))
print(result.group(2))
print(result.group(3))