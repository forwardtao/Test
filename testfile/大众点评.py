from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time


options=webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values':
             {
                 'images': 2,
                 'javascript': 2
             }
        }
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=options)



with open('restaurant_list.csv', encoding='utf-8') as f:
    csv_file = csv.reader(f)
    link_list = [[row[1], row[2]] for row in csv_file]

for eachone in link_list:
    name = eachone[0]
    link = eachone[1]
    output_list = []
    driver.get(link)
    locator = (By.CLASS_NAME, 'content')
    WebDriverWait(driver, 20, 0.5).until(
        EC.presence_of_element_located(locator))

    soup = BeautifulSoup(driver.page_source, "lxml")

    dishes_list = []
    for eachone in soup.find(class_="recommend-name"):
        try:
            dishes = eachone['title'].strip() + eachone.em.text
            dishes_list.append(dishes)
        except:
            pass

    comment_list = []
    for eachone in soup.find(class_="content"):
        try:
            comment_tag = eachone.a.text
            comment_list.append(comment_tag)
        except:
            pass

    output_list.append(
        [name, link, '|'.join(dishes_list), '|'.join(comment_list)])
    with open('restuarant_detail.csv', 'a+', newline='',
              encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, dialect='excel')
        writer.writerows(output_list)
    time.sleep(2)






