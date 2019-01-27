
import re
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

#连接到数据库
from goodsdb import *
import pymongo
client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]

#使用Chrome无头浏览器，即仅在后台使用
chrome_options=Options()
chrome_options.add_argument('--headless')
browser=webdriver.Chrome(chrome_options=chrome_options)
wait=WebDriverWait(browser,10)
#搜索页面
def search():
    try:
        browser.get('https://www.taobao.com')
        #等待元素id为XXX的出现，10秒后若是还不出现，则报错
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
        )
        submit=wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button'))
        )
        input.send_keys('dell笔记本')
        submit.click()
        #等待最下面的总页数加载出来（意味着前面产品已经全部加载出来了）
        total=wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total'))
        )
        #等该页面加载完后，输出一个个产品信息
        get_product()
        return total.text
    except TimeoutException:
        return search()

#跳转到下一页
def next_page(page_number):
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input'))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit'))
        )
        input.clear()
        input.send_keys(page_number)
        submit.click()
        #判断已经跳转成功，由于此时所处页面高亮，所以css_selector不同
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page_number))
        )
        #获取商品
        get_product()
    except TimeoutException:
        next_page(page_number)

#解析宝贝内容
def get_product():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item')))
    html=browser.page_source
    #通过PyQuery解析HTML
    doc=pq(html)
    items=doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product={
            'image':item.find('.pic .img').attr('src'),
            'price':item.find('.price').text().replace('\n',''),
            'deal':item.find('.deal-cnt').text()[:-3].replace('\n',''), #去掉"人付款"三个字
            'title':item.find('.title').text().replace('\n',''),
            'shop':item.find('.shop').text().replace('\n',''),
            'location':item.find('.location').text().replace('\n','')
        }
        save_to_mongo(product)

#参数为一个个产品形成的字典
def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print('存储成功',result)
    except Exception:
        print('存储错误',result)

def main():
    total_String=search()
    total_Number=int(re.compile('(\d+)').search(total_String).group(1))
    for i in range(2,total_Number+1):
        next_page(i)
    browser.close()

if __name__=='__main__':
    main()
