from selenium import webdriver
import requests

url = 'http://www.santostang.com/2018/07/04/hello-world/'
browser = webdriver.Chrome()
browser.get(url)
browser.switch_to.frame(browser.find_element_by_css_selector("iframe[title='livere']"))
comments = browser.find_elements_by_css_selector('div.reply-content')

for eachcomment in comments:
    content = eachcomment.find_element_by_tag_name('p')
    print (content.text)