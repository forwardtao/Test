from bs4 import BeautifulSoup
import csv
import time
from selenium import webdriver
options=webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values':
             {
                 'images': 2,
                 'javascript': 2
             }
        }
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=options)


def outputOneCommentResult(page_id, soup, output_list):
    for item in soup.find(id='shop-all-list'):
        try:
            title = item.find(class_='tit').a.text.strip()
        except:
            title = ''
        try:
            link = "http://www.dianping.com" + item.find(class_='tit').a['href']
        except:
            link = ''
        try:
            star = item.find(class_='comment').span['title']
        except:
            star = ''
        try:
            comment_link = "http://www.dianping.com" + item.find(class_='review-num')['href']
        except:
            comment_link = ''
        try:
            comment = item.find(class_='review-num').b.text.strip()
        except:
            comment = ''
        try:
            price = item.find(class_='mean-price').b.text.strip()
        except:
            price = ''
        try:
            tag = item.find(class_='tag').text.strip()
        except:
            tag = ''
        try:
            addr = item.find(class_='addr').text.strip()
        except:
            addr = ''
        try:
            commentlist = item.find(class_='comment-list').text.strip()
            commentlist = commentlist.replace("\n","|")
        except:
            commentlist = ''

        if title != "":
            output_list.append([str(page_id), title, link, star ,comment_link, comment, price, tag, addr, commentlist])
    return output_list
for i in range(1, 51):
    link = "https://www.dianping.com/search/category/7/10/p" + str(i)
    driver.get(link)
    soup = BeautifulSoup(driver.page_source, "lxml")

    output_list = []
    output_list = outputOneCommentResult(i, soup, output_list)

with open('restaurant_list.csv', 'a+', newline='',
          encoding='utf-8') as csvfile:
    spamwriter = csv.writer(csvfile, dialect='excel')
    spamwriter.writerows(output_list)
time.sleep(2)