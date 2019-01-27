from urllib import request,parse
def youdao(key):
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {
    'i': 'girl',
    'from':'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '1531495012395',
    'sign': '9fc09c1df25976e6b419fc993c7a49e2',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTIME',
    'typoResult': 'false'
    }
    #参数data需要是byte格式
    data = parse.urlencode(data).encode()
    headers ={
    "Accept": "application/json,text/javascript,*/*;q = 0.01",
    #"Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Content-Length": "203",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Cookie": "OUTFOX_SEARCH_USER_ID=665110509@10.169.0.83;OUTFOX_SEARCH_USER_ID_NCOO = 1536988257.3093104;fanyi - ad - id = 46607;fanyi - ad - closed = 1;_ntes_nnid = 72c5927dcf15f366d72995bfa5e9259e, 1531065745714;JSESSIONID = aaaWfy_9i33tt8THOnusw;___rl__test__cookies = 1531495012384",
    "Host": "fanyi.youdao.com",
    "Origin": "http://fanyi.youdao.com",
    "Referer": "http://fanyi.youdao.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest"
    }
    req =request.Request(url=url,data=data,headers=headers)
    rsp = request.urlopen(req)
    html =rsp.read().decode()
    print(html)
if __name__ == '__main__':
    youdao("fruit")
