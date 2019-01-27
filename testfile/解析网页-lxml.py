import requests
from lxml import etree

link = "http://www.santostang.com/"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(link, headers= headers)

html = etree.HTML(r.text)
print(html)
title_list = html.xpath('//h1[@class="post-title"]/a/text()')
list1=[]
for i in range(len(title_list)):
    title = title_list[i].strip()
    list1.append(title)
    print('第{}章的标题是: {}'.format(i+1,list1[i]))