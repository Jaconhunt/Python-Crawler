import requests
from bs4 import BeautifulSoup
import pandas as pd

def GetMovieList(link):
    res=requests.get(link)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text)
    movies=[]
    for movie in soup.select('a em'):
        movies.append(str(movie.text))
    dates=[]
    for date in soup.select('span[class="date"]'):
         dates.append(str(date.text))
    tags=[]
    for tag in soup.select('span[class="tags"]'):
         tags.append(str(tag.text))
    results={}
    results['movie']=movies
    results['date']=dates
    results['tag']=tags
    return results

start_link = 'https://movie.douban.com/people/104233544//collect?start='#请自行更改为自己的主页域名
depth = 8#你的页数
lists={'MOVIE':[],'DATE':[],'TAG':[]}
for i in range(depth):
    link= start_link + str(15*i)
    list=GetMovieList(link)
    lists['MOVIE'].extend(list['movie'])
    lists['DATE'].extend(list['date'])
    lists['TAG'].extend(list['tag'])

pd.set_option('display.max_rows', None)#显示所有行
df_movie = pd.DataFrame.from_dict(lists, orient='index')
df_movie