import requests
import time
import re

exist_url=[]#存储已经爬取的网页
go_writecount=0

start=time.time()
def scarppy(url,depth=1):
    global go_writecount
    try:
        headers={
        'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.3'
                    '6 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        r = requests.get(url="https://en.wikipedia.org/wiki/"+url,headers=headers)
        html=r.text
    except Exception as e:
        print("failed downing and saving",url,e)
        exist_url.append(url)
        return None

    exist_url.append(url)
    link_list=re.findall('<a href="/wiki/([^:#=<>]*?)".*?</a>',html)
    unique_list=list(set(link_list)-set(exist_url))

    for eachone in unique_list:
        go_writecount +=1
        output="No."+str(go_writecount) + "\t Depth:" + str(depth) + "\t" + \
               url+"->"+eachone + "\n"
        print(output)
        with open("wikititle.txt",'a+') as f:
            f.write(output)
            f.close()
        if depth <2:
            scarppy(eachone,depth+1)
scarppy("Wikipedia")
end=time.time()
print("total time:",end-start)

