from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Wikipedia'
headers={'UserAgent':'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) App'
                     'leWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
r = requests.get(url=url,headers=headers)
html = r.text
soup = BeautifulSoup(html,'lxml')

for link in soup.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])