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
