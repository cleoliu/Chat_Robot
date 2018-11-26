from selenium.webdriver.common.by import By

class tmall:
    Item = (By.XPATH, '//*[@class="tb-detail-hd"]/h1')
    Price = (By.XPATH, '//*[@class="tm-promo-price"]/span')
    Option = (By.CSS_SELECTOR, 'ul.tm-clear.J_TSaleProp.tb-img > li:nth-child('+i+') > a > span')
    Image = (By.XPATH , '//*[@id="J_UlThumb"]/li['+i+']/a') #5個

#.get_attribute('href')

class taobao:
    Item = (By.XPATH, '//*[@id="J_Title"]/h3')
    Price = (By.XPATH, '//*[@id="J_StrPrice"]/em[2]')
    Option = (By.CSS_SELECTOR, 'ul.J_TSaleProp.tb-img.tb-clearfix > li:nth-child(1) > a > span')
    Image = (By.XPATH , '//*[@id="J_UlThumb"]/li['+i+']/div/a/img') #6個
