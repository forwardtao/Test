import requests
from pyquery import PyQuery as pq
from pymongo import MongoClient
client=MongoClient()
db=client['weibo']
collection=db['weibo']



base_url='https://m.weibo.cn/api/container/getIndex?'
headers={
'Referer':'https://m.weibo.cn/u/2830678474',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
'X-Requested-With':'XMLHttpRequest',
}


def get_page(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page':page
    }
    try:
        response=requests.get(base_url,headers=headers,params=params)
        if response.status_code==200:
            js_data=response.json()
            return js_data
    except:
        print('error is existing!')
def parse_page(js):
    if js:
        items=js.get('data').get('cards')
        print(type(items))
        for item in items:
            item=item.get('mblog')
            print(type(item))

            if item == None:
                continue
            content = {}
            content['data'] = item.get('created_at')  # 日期
            content['text'] = pq(item.get('text')).text()  # 借助pyquery将正文中的HTML标签去掉了
            content['source'] = item.get('source')  # 用什么发表
            content['user'] = item.get('user').get('screen_name')
            yield content
def save_mongo(weibo):
    if collection.insert(weibo):
        print('save to mongodb!')
if __name__ == '__main__':
    for i in range(1,10):
        js=get_page(i)
        weibos=parse_page(js)
        for weibo in weibos:
            print(weibo)
            save_mongo(weibo)

