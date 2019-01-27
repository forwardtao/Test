from selenium import webdriver
url = 'https://beijing.anjuke.com/sale/'

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values':
             {

                 'images': 2,
                 'javascript': 2
             }
        }
options.add_experimental_option('prefs', prefs)

browser = webdriver.Chrome(chrome_options=options)
browser.get(url)
house_list = browser.find_elements_by_css_selector('div.house-details')
for eachhouse in house_list:
    address=eachhouse.find_element_by_css_selector('span.comm-address')
    address=address.text
    roomdetails=eachhouse.find_elements_by_css_selector('')



    print(address)
