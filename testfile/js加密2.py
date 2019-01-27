'''
1.计算salt的公式i = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10)),
sign = n.md5("fanyideskweb" + t + i + "ebSeFb%=XZ%T[KZ)c(sy!");
计算MD5一共需要四个参数，第一个和第四个是固定的字符串，第三个是所谓的salt，第二个是输入的要查找的单词
'''
def getSalt():
    import time ,random

    salt = int(time.time()*1000) + random.randint(0,10)

    return salt
def getMDS(v):

    import hashlib
    md5 = hashlib.md5()
    md5.update(v.encode("utf-8"))
    sign = md5.hexdigest()
    return sign
def getSign(key,salt):
    sign = "fanyideskweb" + key + str(salt) + "ebSeFb%=XZ%T[KZ)c(sy!"
    sign = getMDS(sign)
    return sign


from urllib import request,parse
def youdao(key):
    url = "http://fanyi.youdao.com/translate_0?smartresult=dict&smartresult=rule"
    salt = getSalt()
    data = {
    'i': key,
    'from':'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': str(salt),
    'sign': getSign(key,salt),
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
    "Content-Length": "len(data)",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Cookie": "OUTFOX_SEARCH_USER_ID=665110509@10.169.0.83;OUTFOX_SEARCH_USER_ID_NCOO = 1536988257.3093104;fanyi - ad - id = 46607;fanyi - ad - closed = 1;_ntes_nnid = 72c5927dcf15f366d72995bfa5e9259e, 1531065745714;JSESSIONID = aaaWfy_9i33tt8THOnusw;___rl__test__cookies = 1531495012384",
    "Host": "fanyi.youdao.com",
    "Origin": "http://fanyi.youdao.com",
    "Referer": "http://fanyi.youdao.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36",
    }
    print(data)
    print('http:' + url)
    req =request.Request(url=url,data=data,headers=headers)
    rsp = request.urlopen(req)
    html =rsp.read().decode()
    print(html)
if __name__ == '__main__':
    youdao("girl")



