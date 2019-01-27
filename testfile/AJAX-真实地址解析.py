import requests
import json

#link="https://api-zero.livere.com/v1/comments/list?callback=jQuery11240530620327073595_1532015979691&limit=10&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1532015979693"
def single_page_comment(link):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36'}
    r = requests.get(link, headers= headers)
    print(r.text)
        # 获取 json 的 string
    json_string = r.text
    json_string = json_string[json_string.find('{'):-2]
    json_data = json.loads(json_string)
    comment_list = json_data['results']['parents']
    for eachone in comment_list:
        message = [eachone['replySeq'],eachone['content']]
        print(message)
#url = https://api-zero.livere.com/v1/comments/list?callback=jQuery11240530620327073595_1532015979691&limit=10&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1532015979693
''' 
   for page in range(1,4):
        link1 = "https://api-zero.livere.com/v1/comments/list?callback=jQuery11240530620327073595_1532015979691&limit=10"
        link2 = "&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1532015979693"
        page_str = str(page)
        link = link1 + page_str + link2
        print(link)
        single_page_comment(link)
'''
for page in range(1,4):
    link1 = "https://api-zero.livere.com/v1/comments/list?callback=jQuery11240530620327073595_1532015979691&limit=10"
    link2 = "&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1532015979693"
    page_str = str(page)
    link = link1 + page_str + link2
    print (link,end='')
    single_page_comment(link)