'''
访问一个网址，更改自己的useragent 进行伪装
'''
from urllib import request,error
if __name__=='__main__':
    url='http://baidu.com'
    try:
        #方法一
        #使用head方法伪装UA
        #headers = {}
        #headers['User-Agent']= 'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5'
        #req=request.Request(url,headers=headers)
        #rsp=request.urlopen(req)
        #html=rsp.read().decode()
        #print(html)
    #方法二
        #使用add_header
    # 正常访问
        req=request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36')

        rsp=request.urlopen(req)

        html=rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print('HTTPError:{0}'.format(e.reason))
        print('HTTPError:{0}'.format(e))
    except error.URLError as e:
        print('URLError:{0}'.format(e.reason))
        print('URLError:{0}'.format(e))
    except Exception as e:
        print(e)