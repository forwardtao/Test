from urllib import request,parse
if __name__=="__main__":
    url="https://www.baidu.com/s?"
    wd= input("input your keywrd:")
    qs = {
        "wd":wd
    }
    qs=parse.urlencode(qs)
    print(qs)
    fullurl =url +qs
    print(fullurl)
    rsp = request.urlopen(fullurl)
    print('url:{0}'.format(rsp.geturl()))
    print("info:{0}".format(rsp.info()))
    print("code:{0}".format(rsp.getcode()))
    html = rsp.read()
    html=html.decode()
    print(html)