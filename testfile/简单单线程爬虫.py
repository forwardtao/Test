import requests
import time

with open('C:/Users/小仙女/Desktop/Python 网络爬虫-从入门到实践代码/Cha 7 -'
          '提升爬虫的速度/alexa.txt','r') as file:
    file_list=file.readlines()
    link_list=[]
    for eachone in file_list:
        link=eachone.split()[1]
        link=link.replace('\n','')
        link_list.append(link)
    print(link_list)
start=time.time()

for eachone in link_list:
    try:
        r=requests.get(eachone)
        print(r.status_code,eachone)
    except Exception as e:
        print('error',e)
end =time.time()
print('串行总时间为：',end-start)