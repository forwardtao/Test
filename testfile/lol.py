import requests
import json
import re


def getLOLImages():
    # 获取源代码
    url_js = "http://lol.qq.com/biz/hero/champion.js"
    html_js = requests.get(url_js).text
    # 200 请求成功
    # print(html_js)
    # pass
    # 正则表达式
    req = '"keys":(.*?),"data"'
    list_js = re.findall(req, html_js)
    # print(list_js[0])
    dict_js = json.loads(list_js[0])
    # 拼接路径
    pic_list = []
    for hero_id in dict_js:
        print(hero_id)
        for i in range(20):
            num = str(i)
            if len(num) == 1:
                hero_num = "00" + num
            elif len(num) == 2:
                hero_num = "0" + num
            print(hero_num)
            numstr = hero_id + hero_num
            url = 'http://ossweb-img.qq.com/images/lol/web201310/skin/big1' + numstr + '.jpg'
            pic_list.append(url)

    list_filepath = []
    path = "D:\图片\lol"

    for name in dict_js.values():
        print(name)
        for i in range(20):
            file_path = path + name + str(i) + ".jpg"
            list_filepath.append(file_path)

    # 下载图片
    n = 0
    for picurl in pic_list:
        # print(picurl)
        res = requests.get(picurl)
        # print(res)
        n = n + 1
        if res.status_code == 200:
            print("正在下载%s:" % list_filepath[n])
            # f=open(list_filepath[n],"wb")
            # f.write(res.content)
            # f.close()
            with open(list_filepath[n], "wb") as f:
                f.write(res.content)


getLOLImages()
