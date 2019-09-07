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

