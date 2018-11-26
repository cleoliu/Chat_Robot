#-*- coding: utf-8 -*-　
#import requests
from lxml import etree
from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from time import sleep,time
#from selenium.webdriver.support import expected_conditions as EC
#from helper import BasePage
#from fun import resource 

class Page:
    def __init__(self, driver):
        self.driver = webdriver

    def is_element_exist(self, xpath):
        s = self.driver.find_elements_by_xpath(xpath)
        if len(s) == 0:
            #print ("元素未找到:%s"%xpath)
            return False
        elif len(s) >= 1:
            return True

    def Get_platform(self):
        #head = word.find("https://") #word[head:head+25]
        self.driver = webdriver.Chrome()
        #short_url = "https://m.tb.cn/h.3mNFpaV"#淘寶
        short_url = "https://m.tb.cn/h.3mipeHt"#淘寶多
        #self.driver.get("https://m.tb.cn/h.3m60CGL")#天貓
        self.driver.get(short_url)#淘寶

        while self.driver.current_url != short_url:
            break

        if "detail.tmall.com" in self.driver.current_url:
            Page.tmall(self)
        elif "item.taobao.com" in self.driver.current_url:
            Title, Price, Options, Image = Page.taobao(self)
        else:
            return "網址錯誤"

    def tmall(self):
        pass

    def taobao(self):
        html = self.driver.page_source  #取得網頁原始碼
        selector = etree.HTML(html)

        # 登入關閉窗
        #self.driver.find_element_by_xpath('//*[@id="sufei-dialog-close"]').click() 

        # 標題
        #title = BasePage.driver_wait_until(self, resource.taobao.Item).text
        #print(title)
        Title = selector.xpath('//*[@id="J_Title"]/h3')[0].text
        print (Title)

        # 價格
        Price = selector.xpath('//*[@id="J_StrPrice"]/em[2]')[0].text
        print (Price)
        #rmb = self.driver.find_element_by_xpath('//*[@id="J_PromoPriceNum"]').text

        # 顏色分類,數量
        Options = []
        J_isku = Page.is_element_exist(self, '//*[@id="J_isku"]/div/dl[1]/dd/ul/li')
        if J_isku == False: #如果不是多言多尺
            pass
        elif J_isku == True: 
            J_TSaleProp = selector.xpath('//*[@class ="J_TSaleProp tb-img tb-clearfix"]/li')
            for i in J_TSaleProp:
                small_pic = i.xpath("./a//span")[0].text
                Options.append(small_pic)
        print(Options)
        
        # 圖片
        Image = []
        J_ULThumb = selector.xpath("//div[@class='tb-gallery']/ul/li")
        for li in J_ULThumb:
            # 替换图片 从50*50 至 400 * 400
            if len(li.xpath("./div/a/img/@data-src")) < 1:
                continue
            small_pic = li.xpath("./div/a/img/@data-src")[0]
            common_pic = 'https:' + small_pic.replace('50x50', '400x400')
            Image.append(common_pic)
        print (Image)
            # self.saveImg(img_dir_path, common_pic, thumb_title.decode('utf-8'))

        # 爬取里面所有图片
        all_img = selector.xpath("//div[@id='J_DivItemDesc']//descendant::img/@src")
        #print (all_img)
        for img in all_img:
            imglink = img
            if img.startswith('http') is True:
                imglink = img
            else:
                imglink = 'https:' + img
            Image.append(imglink)
        print(Image)

        return Title, Price, Options, Image

    def Main(self):
        Page.Get_platform(self)

if __name__ == '__main__':
    Page(webdriver).Main()