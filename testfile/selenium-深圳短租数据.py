from selenium import webdriver

url = 'https://zh.airbnb.com/s/Shenzhen--China?page=1'
browser = webdriver.Chrome()
browser.get(url)
for i in range(20):
    #browser.get("https://zh.airbnb.com/s/Shenzhen-China/homes?refinement_paths%5B%5D=%2Fhomes&allow_override%5B%5D=&s_tag=_45KiJet§ion_offset="+str(i))
    rent_list = browser.find_elements_by_css_selector("div._v72lrv")
    for eachhouse in rent_list:
        try:
            comment = eachhouse.find_element_by_css_selector("div._190019zr")
            comment = comment.text
        except:
            comment = 0
        price = eachhouse.find_element_by_tag_name("span")
        price = price.text[4:]
        fangxin = eachhouse.find_element_by_tag_name('span')
        fangxin = fangxin.text
        evaluate = eachhouse.find_element_by_css_selector("div._1hc6xcl")
        evaluate = evaluate.text
        print("评论"+evaluate+"，价格"+price,fangxin,comment+"\n")


