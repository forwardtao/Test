'''
#未使用cookie登录，返回登录界面
from urllib import request
if __name__ == '__main__':
    url = 'http://www.renren.com/966904280'
    rsp = request.urlopen(url)
    html=rsp.read().decode()
    with open('rsp.html','w') as f:
        f.write(html)
'''
from urllib import request
if __name__ == '__main__':
    url = 'http://www.renren.com/966904280'
    headers = {'Cookie':'anonymid=jjipbjr4so2ys; depovince=SH; _r01_=1; JSESSIONID=abcSZQbMifk0jdkKwfpsw; ick_login=60abdfc7-2f1f-4c2e-853f-b1956b428ab5; t=11be91c86b323144e4e48018b3bc80e70; societyguester=11be91c86b323144e4e48018b3bc80e70; id=966904280; xnsid=70e1b4e2; jebecookies=7b727485-690e-4b95-942d-7ce8d3cbb60e|||||; ver=7.0; loginfrom=null; wp_fold=0'}
    req = request.Request(url,headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    with open('rsp.html', 'w') as f:
        f.write(html)  
