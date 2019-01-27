import requests
''''
url = "https://movie.douban.com"
#rsp = requests.get(url)
rsp = requests.request("get",url)
print(rsp.text)
'''
url = 'https://www.baidu.com/s?'
kw = {
    'wd':'大熊猫'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36'

}
rsp =requests.get(url,params=kw,headers=headers)
print(rsp.text)
print(rsp.content)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code)

