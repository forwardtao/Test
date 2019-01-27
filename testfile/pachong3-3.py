import requests
from bs4 import BeautifulSoup
def get_movies():
    headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                 '(KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36',
    'Host':'movie.douban.com'
    }
    movie_list=[]
    for i in range(0,10):
        link = "http://movie.douban.com/top250?start=' + str(i * 25)"
        r = requests.get(link,headers=headers,timeout= 10)
        print(str(i+1),"页响应状态码：",r.status_code)
        soup = BeautifulSoup(r.text,"html.parser")
        div_list = soup.find_all('div',attrs={'class':'hd'})
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)9
    return movie_list
    print(r.text)
movies=get_movies()
print(movies)


