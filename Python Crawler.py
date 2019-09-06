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

response = urllib.request.urlopen('http://httpbin.org/get', timeout = 0.2 ) #timeout �޸�Ϊ0.2, 1 �����������
print(response.read())

import socket
import urllib.request

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout = 0.2 ) #timeout �޸�Ϊ0.2, 1 �����������
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

#�˶δ���������, ��Ҫ��load���r
#https://stackoverflow.com/questions/37400974/unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-trunca

from urllib import request, error

try:
    response = request.urlopen('http://cuiqingcai.com/index.htm')
except error.URLError as e:
    print(e.reason)