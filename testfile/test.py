import requests
import json
r=requests.get("https://feed.sina.com.cn/api/roll/get?pageid=121&lid=1356&num=20&versionNumber=1.2.4&page=1&encode=utf-8&callback=feedCardJsonpCallback&_=1539222744271")
print(r.text.lstrip("try{feedCardJsonpCallback(").rstrip(");}catch(e){};"))
j=json.loads(r.text.lstrip("try{feedCardJsonpCallback(").rstrip(");}catch(e){};"))
j
