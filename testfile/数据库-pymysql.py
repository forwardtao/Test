import pymysql.cursors
from bs4 import BeautifulSoup
import requests
#链接数据库
connection = pymysql.connect(host='localhost',user='root',passwd='123456',db='scraping')
#获取游标
cursor = connection.cursor()

url = 'http://www.santostang.com/'
headers= {
    'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

}
r = requests.get(url,headers=headers)
soup = BeautifulSoup(r.text,'lxml')
title_list = soup.find_all('h1',attrs={'class':'post-title'})
for eachtitle in title_list:
    url=eachtitle.a['href']
    title = eachtitle.a.text.strip()
    cursor.execute("INSERT INTO urls (url, content) VALUES (%s, %s)", (url, title))


connection.commit()

cursor.close()
connection.close()
