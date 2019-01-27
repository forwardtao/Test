from selenium import webdriver
url='http://www.santostang.com/2018/07/04/hello-world/'
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values':
             {
                 'stylesheet':2,
                 'images': 2,
                 'javascript': 2
             }
        }
options.add_experimental_option('prefs', prefs)

browser = webdriver.Chrome(chrome_options=options)
browser.get(url)
