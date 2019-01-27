  import requests
import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.blog_database
collection = db.blog

url = 'http://www.santostang.com/'
headers = {
    'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

}
r = requests.get(url,headers=headers)
soup = BeautifulSoup(r.text,'html.parser')
title_list =  soup.find_all('h1',attrs={'class':'post-title'})
for eachtitle in title_list:
    url = eachtitle.a['href']
    title = eachtitle.a.text.strip()
    post = {
        "url":url,
        "title":title,
        "date":datetime.datetime.utcnow()
    }
    collection.insert_one(post)

