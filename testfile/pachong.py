import requests
from bs4 import BeautifulSoup
link="http://www.santostang.com/"
headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
"(KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36"}
r =requests.get(link,headers=headers)
print(r.text)
soup = BeautifulSoup(r.text,"html.parser")
title = soup.find("h1",class_="post-title").a.text.strip()
print(title)

with open("title.txt","a+") as f:
    f.write(title)
    f.close()

