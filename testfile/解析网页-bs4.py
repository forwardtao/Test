import requests
from bs4 import BeautifulSoup

url = 'http://www.santostang.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
r = requests.get(url,headers=headers)

soup = BeautifulSoup(r.text,"html.parser")
first_title = soup.find('h1',attrs={'class':'post-title'}).a.text.strip()
print('第一个标题是: ',first_title)

title_list = soup.find_all('h1',attrs={'class':'post-title'})

list1=[]
for i in range(len(title_list)):
    title = title_list[i].a.text.strip()
    list1.append(title)
    print('第{}章的标题是: {}'.format(i+1,list1[i]))

