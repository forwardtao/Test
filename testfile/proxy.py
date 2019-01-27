'''
使用代理访问百度网站
'''
from urllib import request,error

if __name__=="__main__":
    url='http://www.baidu.com'
    #使用代理步骤：
    #1.设置代理地址
    proxy = {'http':'60.205.205.48'}
    #2.创建proxyhandler
    proxy_handler = request.ProxyHandler(proxy)
    #3.创建 opener
    opener = request.build_opener(proxy_handler)
    #4.安装
    request.install_opener(opener)

    #如果现在访问url，则使用代理服务器
    try:
        rsp=request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)