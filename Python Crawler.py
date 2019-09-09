'''
Create by: Jacon Hunt
'''
import urllib.request

response = urllib.request.urlopen('https://www.python.org')

print(response.read().decode('utf-8'))

import urllib.request

response = urllib.request.urlopen('https://www.python.org')

print(type(response))

import urllib.request

response = urllib.request.urlopen('https://www.python.org')

print(response.status)
print(response.getheaders())
print(response.getheader('Server'))


import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'world': 'hello'}), encoding = 'utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', data = data)
print(response.read())

import urllib.request

response = urllib.request.urlopen('http://httpbin.org/get', timeout = 0.2 ) #timeout 修改为0.2, 1 可以正常输出
print(response.read())

import socket
import urllib.request

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout = 0.2 ) #timeout 修改为0.2, 1 可以正常输出
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

import urllib.request

request = urllib.request.Request('http://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}

dict = {
    'name': 'Germey'
}

data = bytes(parse.urlencode(dict), encoding = 'utf-8')
req = request.Request(url= url, data = data,  method = 'POST')
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
response = request.urlopen(req)
print(response.read().decode('utf-8'))

from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import  URLError

username = 'username'
password = 'password'
url = 'http://localhost:5000/'

p= HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)

from urllib.request import ProxyHandler, build_opener
from urllib.error import  URLError

proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1:9743'
})

opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+"="+item.value)

import http.cookiejar, urllib.request

filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard = True, ignore_expires = True)

import http.cookiejar, urllib.request


cookie = http.cookiejar.LWPCookieJar()
cookie.load(r'C:\Users\Administrator\PycharmProjects\test01\cookie.txt', ignore_discard = True, ignore_expires = True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))

#此段代码有问题, 需要在load后加r
#https://stackoverflow.com/questions/37400974/unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-trunca

from urllib import request, error

try:
    response = request.urlopen('http://cuiqingcai.com/index.htm')
except error.URLError as e:
    print(e.reason)

from  urllib import request, error
try:
    response = request.urlopen('http://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, seq= '\n')
# 上面代码有误,应该去除seq = '\n'
# 'seq' is an invalid keyword argument for this function

from  urllib import request, error

try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers)
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')

import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://www.baidu.com' , timeout= 0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
#会报错，也会输出

from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.htm; user?id=5#comment')
print(type(result), result)

from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.htm; user?id=5#comment', scheme = 'https')
print(result)

from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments= False)
print(result)

from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments= False)
print(result.scheme, result[0], result.netloc, result[1])

from urllib.parse import urlunparse

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a = 6', 'comment']  #长度为6
print(urlunparse(data))


from urllib.parse import urlsplit
from urllib.parse import urlunsplit

result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)

data = ['http', 'www.baidu.com', 'index.html',  'a = 6', 'comment']
print(result.scheme, result[0])
print(urlunsplit(data))

from urllib.parse import urlencode

params = {
    'name': 'germey',
    'age': 22
}

base_url = 'http://www.baidu.com?'
url = base_url +urlencode(params)
print(url)

from urllib.parse import parse_qs

query = 'name=germey&age=22'
print(parse_qs(query))

from urllib.parse import parse_qsl

query = 'name=germey&age=22'
print(parse_qsl(query))

from urllib.parse import quote

keyword = '壁纸'
url = 'https://www.baidu.com/s?wd='+quote(keyword)
print(url)

from urllib.parse import unquote

url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))

from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()

print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', "http://wwww.jianshu.com/search?q=python&page=1&type=collections"))

from urllib.robotparser import RobotFileParser
from urllib.request import urlopen

rp = RobotFileParser()
rp.parse(urlopen('http://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n'))
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', "http://wwww.jianshu.com/search?q=python&page=1&type=collections"))
# HTTPError: HTTP Error 403: Forbidden 会报错

import requests

r = requests.get('http://www.baidu.com/')

print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)

import requests

r = requests.get('http://httpbin.org/get')
print(r.text)

data = {
    'name': 'germey',
    'age': 22
}

r = requests.get('http://httpbin.org/get', params= data)
print(r.text)

import requests

r= requests.get("http://httpbin.org/get")
print(type(r.text))
print(r.json())
print(type(r.json()))

import requests
import re

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36\
            (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get('https://www.zhihu.com/explore', headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)
#无结果，知乎限制

import requests

r = requests.get("https://github.com/favicon.ico")
print(r.text)
print(r.content)

import requests

r = requests.get("https://github.com/favicon.ico")
with open('favicon.ico', 'wb') as f:
    f.write(r.content)

    import requests

data = {'name':'germey','age': '22'}
r = requests.post("http://httpbin.org/post", data =data)
print(r.text)

import requests

r = requests.get('http://www.jianshu.com')

print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)

import requests
r = requests.get('http://www.jianshu.com')
exit() if not r.status code == requests.codes.ok else print('Request Successfully')
#以上代码报错

import requests
files = {'file': open ('favicon.ico','rb')}
r = requests.post ("http://httpbin.org/post", files=files)
print(r.text)

import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group())
print(result.span())
#正则表达式

import re

content = 'Hello 1234567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s(\d+)\sWorld',content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())

#通用匹配
import re

content = 'Hello 1234567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello.*Demo$',content)
print(result)
print(result.group())
print(result.span())

#贪婪与非贪婪
import re

content = 'Hello 1234567 World_This is a Regex Demo'
print(len(content))
result = re.match('^He.*(\d+).*Demo$',content)
print(result)
print(result.group(1))  #贪婪匹配

import re

content = 'Hello 1234567 World_This is a Regex Demo'
print(len(content))
result = re.match('^He.*?(\d+).*Demo$',content)
print(result)
print(result.group(1)) #非贪婪匹配

import re

content = 'http://weibo.com/comment/kEraCN'
result1 = re.match('^http.*?comment/(.*?)',content)
result2 = re.match('^http.*?comment/(.*)',content)
print('result1', result1.group(1))
print('result2', result2.group(1)) #注意末尾匹配情况

#修饰符
import re

content = '''Hello 1234567 World_This
is a Regex Demo'''
result = re.match('^He.*?(\d+).*?Demo$',content, re.S)
print(result.group(1))

#转义匹配，此处括号和点均转义
import re

content = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com', content)
print(result)

#search(）实例1
import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result =re.search('Hello.*?(\d+).*?Demo', content)
print(result)

#search(）实例2
import re

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''

result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result.group(1),result.group(2))

result = re.search('<li.*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result.group(1),result.group(2))

result = re.search('<li.*?singer="(.*?)">(.*?)</a>',html) #不匹配换行符
print(result.group(1),result.group(2))

results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
print(results)
print(type(results))
for result in results:
    print(result)
    print(result[0], result[1], result[2])

results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)
for result in results:
    print(result[1])

html = re.sub('<a.*?>|</a>', '', html)
print(html)
results = re.findall('<li.*?>(.*?)</li>', html, re.S)
for result in results:
    print(result.strip()) #sub实例2

#sub()
import re

content =  '54aK54yr5oiR54ix5L2g'
content = re.sub('\d+', '', content)
print(content)

#compile()
import re

content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-22 13:21'

pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)

#lxml实例引入
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
     </ul>
 </div>
'''

html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))
#待补充其他lxml用法

#BeautifulSoup
from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>Hello</p>', 'lxml')
print(soup.p.string)

#第5章 数据存储
import requests
from pyquery import PyQuery as pq

url = "https://www.zhihu.com/explore"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)\
                  Chrome/58.0.3029.110 Safari/537.36'
}
html = requests.get(url, headers=headers).text  # 获取网页源代码文本
doc = pq(html)
items = doc('.explore-tab .feed-item').items()  # 结果是列表形式
file = open('explore.txt', 'a', encoding="utf-8")
for item in items:
    question = item.find('h2').text()   # 获取每个标题
    author = item.find('.author-link-line').text()      # 获取每个标题的作者
    answer = pq(item.find('.content').html()).text()    # 先找到html文本，再转换为pyquery对象，再获取文本
    file.write('\n'.join([question, author, answer]))   # 将标题、作者、回答放在一起
    file.write('\n' + '=' * 50 + '\n')
file.close()
#此种方式无法得到内容，可能被反爬虫

#读取json
import json

str = '''
[{
"name": "Bob",
"Gender": "male",
"Birthday": "1992-10-18"
},{"name": "Selina",
"Gender": "female",
"Birthday": "1995-10-18"
}
]
'''
print(type(str))
data = json.loads(str)
print(data)
print(type(data))
print(data[0]['name'])
print(data[0].get('name'))
print(data[0].get('age'))
print(data[0].get('age', 25))
#https://stackoverflow.com/questions/39491420/python-jsonexpecting-property-name-enclosed-in-double-quotes

#json文本读取
import json

with open('data.json','r') as file:
    str = file.read()
    data = json.loads(str)
    print(data)
    
#输出json
import json

data = [{
"name": "王伟",
"Gender": "男",
"Birthday": "1992-10-18"
},{"name": "Selina",
"Gender": "female",
"Birthday": "1995-10-18"
}
]
with open ('data.json', 'w', encoding = 'utf-8') as file:
    file.write(json.dumps(data, indent =2, ensure_ascii = False))
 
#CSV文件存储
import csv

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])
    
#字典写入
import csv

with open('data.csv', 'w') as csvfile:
    fieldnames= ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow({'id':'10001','name': 'Mike','age':20})
    writer.writerow({'id':'10002','name': 'Bob','age': 22})
    writer.writerow({'id':'10003', 'name':'Jordan','age': 21})
    writer.writerow({'id': '10004', 'name': 'Durant', 'age': 22})
 
#中文写入
import csv

with open('data.csv', 'a', encoding = 'utf-8') as csvfile:
    fieldnames= ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writerow({'id': '10005', 'name': '王伟', 'age': 22})
    
#读取CSV
import csv

with open('data.csv', 'r', encoding ='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

import pandas as pd

df = pd.read_csv('data.csv')
print(df)

#连接数据库MySQL
import pymysql

db = pymysql.connect(host = 'localhost', user = 'root', password = 'czq123xyz', port = 3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)
cursor.execute("CREATE DATABASE spiders1 DEFAULT CHARACTER SET utf8MB4")
db.close()

#创建表
import pymysql

db = pymysql.connect(host = 'localhost', user = 'root', password = 'czq123xyz', port = 3306, db = 'spiders1')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT  NULL, name VARCHAR(255) NOT NULL ,age INT NOT NULL ,PRIMARY KEY(id))'
cursor.execute(sql)
db.close()

#插入数据
import pymysql

id = '2010001'
user = 'Bob'
age = 20

db = pymysql.connect(host = 'localhost', user = 'root', password = 'czq123xyz', port = 3306, db = 'spiders1')
cursor = db.cursor()
sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()
except:
    db.rollback()
db.close()

#动态表
import pymysql

db = pymysql.connect(host = 'localhost', user = 'root', password = 'czq123xyz', port = 3306, db = 'spiders1')
cursor = db.cursor()
data = {
    'id':  '2010001',
    'name':  'Bob',
    'age': 20
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table =table, keys =keys, values = values)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()

#更新数据
import pymysql

db = pymysql.connect(host = 'localhost', user = 'root', password = 'czq123xyz', port = 3306, db = 'spiders1')
cursor = db.cursor()
sql = 'UPDATE students SET age = %s WHERE name = %s'
try:
    cursor.execute(sql, (25, 'Bob'))
    db.commit()
except:
    db.rollback()
db.close()

#去除重复值
import pymysql

db = pymysql.connect(host = 'localhost', user = 'root', password = 'czq123xyz', port = 3306, db = 'spiders1')
cursor = db.cursor()
data = {
    'id':  '2010001',
    'name':  'Bob',
    'age': 21
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table =table, keys =keys, values = values)
update = ','.join(["{key} = %s".format(key =key ) for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()

#删除数据
import pymysql

db = pymysql.connect(host = 'localhost', user = 'root', password = 'czq123xyz', port = 3306, db = 'spiders1')
cursor = db.cursor()
table = 'students'
condition = 'age > 20'

sql = 'DELETE FROM {table} WHERE {condition}'.format(table = table, condition = condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()

#查询数据
import pymysql

db = pymysql.connect(host = 'localhost', user = 'root', password = 'czq123xyz', port = 3306, db = 'spiders1')
cursor = db.cursor()
table = 'students'

sql = 'SELECT * FROM students WHERE  age >= 20'

try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone()
    print('One:', one)
    results = cursor.fetchall()
    print('Results:', results)
    print('Results Type:', type(results))
    for row in results:
        print(row)
except:
    print('Error')
#共用指针, cursor

#While循环遍历数据
import pymysql

db = pymysql.connect(host = 'localhost', user = 'root', password = 'czq123xyz', port = 3306, db = 'spiders1')
cursor = db.cursor()
table = 'students'

sql = 'SELECT * FROM students WHERE  age >= 20'

try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')
