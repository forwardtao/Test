from urllib import request

import ssl
#使用非认证上下文黄金替换认证的向下文环境
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.12306.cn/mormhweb/'
rsp =request.urlopen(url)
html = rsp.read().decode()
print(html)
