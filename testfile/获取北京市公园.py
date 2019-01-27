import json
from urllib.request import urlopen
import time
from urllib import request

def urls(itemy, loc):
    #baidu_api = "93GskrM3HsaQxKD3wFEkuWzF6lG8m4GZ"
    urls=[]
    for page in range(0,20):
        url = "http://api.map.baidu.com/place/v2/search?query=" + request.quote(itemy) + "&bounds=" + loc
        url = url + "&page_size=20&page_num=" + str(page) + "&output=json&ak=93GskrM3HsaQxKD3wFEkuWzF6lG8m4GZ"
        urls.append(url)

    return urls

def baidu_search(urls):
    try:
        json_sel = []
        for url in urls:
            req = request.Request(url)
            json_obj = urlopen(req)
            data = json.load(json_obj)

            for item in data['results']:
                jname = item["name"]
                jlat = item["location"]["lat"]
                jlng = item["location"]["lng"]
                if "telephone" in item:
                    jtel = item["telephone"].replace(',',' ')
                else:
                    jtel = ''

                js_sel = jname + ',' + str(jlat) + ',' + str(jlng) + ',' + str(jtel)
                json_sel.append(js_sel)
    except:
        pass

    return json_sel

def lat_all(loc_all):
    lat_sw = float(loc_all.split(',')[0])
    lat_ne = float(loc_all.split(',')[2])
    lat_list = []

    for i in range(0, int((lat_ne - lat_sw ) / 0.01)):  # 网格大小，可根据区域内POI数目修改
        lat_list.append(lat_sw + 0.01 * i)
    lat_list.append(lat_ne)

    return lat_list

def lng_all(loc_all):
    lng_sw = float(loc_all.split(',')[1])
    lng_ne = float(loc_all.split(',')[3])
    lng_list = []
    for i in range(0, int((lng_ne - lng_sw ) / 0.01)):
        lng_list.append(lng_sw + 0.01 * i)
    lng_list.append(lng_ne)

    return lng_list

def ls_com(loc_all):
    l1 = lat_all(loc_all)
    l2 = lng_all(loc_all)
    ab_list = []
    for i1 in range(0, len(l1)):
        a = str(l1[i1])
        for i2 in range(0, len(l2)):
            b = str(l2[i2])
            ab = a + ',' + b
            ab_list.append(ab)
    return ab_list

def ls_row(loc_all):
    l1 = lat_all(loc_all)
    l2 = lng_all(loc_all)
    ls_com_v = ls_com(loc_all)
    ls = []
    for n in range(0, len(l1) - 1):
        for i in range(0 + len(l1) * n, len(l2) + (len(l2)) * n - 1):
            a = ls_com_v[i]
            b = ls_com_v[i + len(l2) + 1]
            ab = a + ',' + b
            ab_list = ab.split(',')
            if (ab_list[0] < ab_list[2] and ab_list[1] < ab_list[3]):
                ls.append(ab)


    return ls

if __name__ == '__main__':
    print("开始爬取数据，请稍等...")
    start_time = time.time()
    loc = '23.1121, 113.3408, 23.1475, 113.3902'
    locs_to_use = ls_row(loc)
    i = 0
    num = []
    filepath = 'title3.txt'
    f = open(filepath, 'w',encoding='utf-8')
    for loc_to_use in locs_to_use:
        print(loc_to_use)
        i += 1
        print("正在采集第%d个区域"%i)
        par = urls(u'政府', loc_to_use)
        print(par)
        a = baidu_search(par)
        b = len(a)
        num.append(b)
        print("第%d个区域采集数量为%d"%(i,b))

        for ax in a:
            print('政府,' + ax)
            item = '政府,' + ax
            f.write(item)
            f.write("\n")

    end_time = time.time()
    print("爬取完毕，用时%.2f秒" % (end_time - start_time))