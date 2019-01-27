html = """
<body>
<header id="header">
    <h3 id="name">大数据@唐松Santos</h3>
  <div class="sns">
    <a href="http://www.santostang.com/feed/" target="_blank" rel="nofollow" title="RSS"><i class="fa fa-rss" aria-hidden="true"></i></a>
        <a href="http://weibo.com/santostang" target="_blank" rel="nofollow" title="Weibo"><i class="fa fa-weibo" aria-hidden="true"></i></a>
                <a href="https://www.linkedin.com/in/santostang" target="_blank" rel="nofollow" title="Linkedin"><i class="fa fa-linkedin" aria-hidden="true"></i></a>
                <a href="mailto:tangsongsky@gmail.com" target="_blank" rel="nofollow" title="envelope"><i class="fa fa-envelope" aria-hidden="true"></i></i></a>
          </div>
  <div class="nav">
   <ul><li class="current-menu-item"><a href="http://www.santostang.com/">首页</a></li>
<li><a href="http://www.santostang.com/about-me/">关于我</a></li>
<li><a href="http://www.santostang.com/post-search/">文章搜索</a></li>
<li><a href="http://www.santostang.com/wp-login.php">登录</a></li>
</ul>  </div>
</header>
"""
from bs4 import BeautifulSoup
import re
'''
soup = BeautifulSoup(html,'html.parser')
print(soup.prettify())
'''
soup = BeautifulSoup(html,'html.parser')
print(soup.header.h3)
print(soup.header.div.contents)
print(soup.header.div.contents[1])
for child in soup.header.div.children:
    print(child)
for child in soup.header.div.descendants:
    print(child)
a_tag = soup.header.div.a
print(a_tag.parent)
soup.find_all('div', class_='sns')
for tag in soup.find_all(re.compile("^h")):
        print(tag.name)


print (soup.select("header > h3"))
print (soup.select("div > a"))
