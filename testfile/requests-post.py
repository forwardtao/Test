'''
利用parse 模块模拟post请求
分析百度词典
分析步骤
1.打开F2
2.尝试输入单词girl，发现每敲一个字母都有请求
3.请求地址是是https://fanyi.baidu.com/sug
4.利用network—all——hearders查看发现formdata的值是kw：girl
5.检查返回内容的格式，发现返回的是json格式内容==》需要用到json包
'''
from urllib import request,parse
import requests
import json
'''
d大致流程：
1.利用data构造内容，然后urlopen打开
2.返回一个json格式的结果
3.结果应该是girl的释义
'''
baseurl = 'https://fanyi.baidu.com/sug'
data = {
    'kw':'girl'
}
#需要使用parse模块对data进行编码
#data = parse.urlencode(data).encode("utf-8")
#需要构造请求头，请求头部应该至少包含传入的数据长度
#request需求传入的数据是dict格式
headers ={
'Content-Length':str(len(data))

}
#构造一个Request的实例
#req=request.Request(url=baseurl,data=data,headers=headers)
#有了data,url,headers,就可以尝试发出请求了，因为已经构造了一个Request的请求实例，
# 则所有的请求信息都可以封装在Request实例中
rsp = requests.post(url=baseurl,data=data,headers=headers)
print(rsp.text)
print(rsp.json())
'''
json_data =rsp.read().decode()
print(json_data)
#把json字符串转换成字典
json_data =json.loads(json_data)
print(json_data)
for item in json_data['data']:
    print(item['k'],'--',item['v'])
'''
