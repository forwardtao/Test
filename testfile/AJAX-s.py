from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# 可能需要手动添加路径
browser = webdriver.Chrome()
browser.get("https://www.baidu.com/")

text = browser.find_element_by_id('wrapper').text
print(text)
print(browser.title)
#得到页面的快照
browser.save_screenshot('index.png')
#id= ‘kw’是百度的输入框，我们得到输入框的ui元素后直接输入大熊猫
browser.find_element_by_id('kw').send_keys(u'大熊猫')
#id=
#获取当前页面的cookie'su,是百度搜索的按钮，click模拟点击
browser.find_element_by_id('su').click()
time.sleep(5)
browser.save_screenshot('daxiongmao.png')
print(browser.get_cookies())
#模拟输入两个按键crtl+a
browser.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
#ctrl +_x
browser.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')

browser.find_element_by_id('kw').send_keys(u'航空母舰')
browser.save_screenshot('hangmu.png')
browser.find_element_by_id('su').send_keys(Keys.RETURN)
time.sleep(5)
browser.save_screenshot('hangmu2.png')

#清空输入框clear
browser.find_element_by_id('kw').clear()

#退出浏览器
browser.quit()