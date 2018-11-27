#-*- coding: utf-8 -*-　
from lxml import etree
from selenium import webdriver
from fun.translate import Zhcn_Trans_Zhtw

class Page:
    def __init__(self, driver):
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.add_argument('--headless')                   #無頭chrome
        chrome_options.add_argument('--disable-gpu')                #不用gpu
        chrome_options.add_argument('--log-level=3')                #過濾一些輸出error
        chrome_options.add_argument('--proxy-server="direct://"')   #windows無頭設定
        chrome_options.add_argument('--proxy-bypass-list=*')        #windows無頭設定
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def is_element_exist(self, xpath):
        s = self.driver.find_elements_by_xpath(xpath)
        if len(s) == 0:
            #print ("元素未找到:%s"%xpath)
            return False
        elif len(s) >= 1:
            return True

    def Get_platform(self, short_url):
        self.driver.get(short_url)

        # 等待短網址跳轉
        while self.driver.current_url != short_url:
            break

        # 判斷網域
        if "detail.tmall.com" in self.driver.current_url:
            from fun.resource import tmall as RES
            Title, Price, Options, Image = Page.crawler(self, RES)
        elif "item.taobao.com" in self.driver.current_url:
            from fun.resource import taobao as RES
            Title, Price, Options, Image = Page.crawler(self, RES)
        else:
            return "網址錯誤"

        return self.driver.current_url, Title, Price, Options, Image

    def crawler(self, RES):
        # 取得網頁原始碼
        html = self.driver.page_source  
        selector = etree.HTML(html)

        # 標題
        title = selector.xpath(RES.TITLE)[0].text.strip()
        Title = Zhcn_Trans_Zhtw(title)
        #print (Title)

        # 價格
        J_price = Page.is_element_exist(self, RES.PRICE)
        if J_price == False:   #如果沒有顯示價格,就不爬
            Price = '需登入取Price'
            #print ('需登入取Price')
        elif J_price == True:
            Price = selector.xpath(RES.PRICE)[0].text
            #print (Price)
            
        # 顏色分類,數量
        Options = []
        J_isku = Page.is_element_exist(self, RES.ISKU)
        if J_isku == True:     #如果有多顏多尺,就爬選項
            J_TSaleProp = selector.xpath(RES.OPTION)
            for i in J_TSaleProp:
                small_pic = i.xpath("./a//span")[0].text
                Options.append(Zhcn_Trans_Zhtw(small_pic))
        #print(Options)
        
        # 商品主圖
        Image = []
        J_ULThumb = selector.xpath(RES.IMAGE)
        for li in J_ULThumb:
            if len(li.xpath(RES.IMAGE_SUB)) < 1:
                continue
            small_pic = li.xpath(RES.IMAGE_SUB)[0]
            common_pic = 'https:' + small_pic.replace('50x50', '400x400')   #替換圖片50*50至400*400
            Image.append(common_pic)
        #print (Image)

        # 詳細頁所有圖片
        all_img = selector.xpath(RES.DESCIMAGE)
        for img in all_img:
            imglink = img
            if img.startswith('http') is True:
                imglink = img
            else:
                imglink = 'https:' + img
            Image.append(imglink)
        #print(Image)

        return Title, Price, Options, Image


if __name__ == '__main__':
    Page(webdriver).Get_platform(short_url="https://m.tb.cn/h.3NdhkXb")
        #short_url = "https://m.tb.cn/h.3mNFpaV" #淘寶
        #short_url = "https://m.tb.cn/h.3mipeHt" #淘寶多顏
        #short_url = "https://m.tb.cn/h.3NdhkXb" #天貓多顏