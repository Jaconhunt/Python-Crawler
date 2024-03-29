import requests
import json
from requests.exceptions import RequestException
import time
import re

def get_one_page(url):
    try:
        headers = {
        'User-Agent': 'Mozilla/5.0(Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36(KHTML, like Gecko) \
        Chrome/65.0.3325.162 Safari/537.36'
    }
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?title="(.*?)".*?img data-src="(.*?)".*?<p class="star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i><i class="fraction">(\d+).*?</dd>',re.S
    )
    items = re.findall(pattern, html)
    for item in items:
        yield{
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score':item[5]+item[6]
        }
    print(items)

def write_to_file(content):
    with open('result.text', 'a', encoding = 'utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii = False)+'\n')

def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)
#代码来源于崔庆才《Python3 网络爬虫开发实战》
'''
可以学习的地方有如下：
1. Request用法
2. Try Except异常处理
3. yield 生成器
4. json用法
'''
