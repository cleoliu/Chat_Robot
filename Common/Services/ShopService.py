#-*- coding: utf-8 -*-　
from lxml import etree
from selenium import webdriver
from Common.Services.TranslateService import TranslateText


class Page:
    def __init__(self, driver):                 #--設定chromedriver--
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.add_argument('--headless')                   #無頭chrome
        chrome_options.add_argument('--disable-gpu')                #不用gpu
        chrome_options.add_argument('--log-level=3')                #過濾一些輸出error
        chrome_options.add_argument('--proxy-server="direct://"')   #windows無頭設定
        chrome_options.add_argument('--proxy-bypass-list=*')        #windows無頭設定
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def __IsElementExist(self, xpath):          #--尋找元素--
        s = self.driver.find_elements_by_xpath(xpath)
        if len(s) == 0:
            #print ("元素未找到:%s"%xpath)
            return False
        elif len(s) >= 1:
            return True

    def __GetPlatform(self, shortUrl):          #--判斷來自哪個購物網站,配對元素--
        self.driver.get(shortUrl)

        # 等待短網址跳轉
        while self.driver.current_url != shortUrl:
            break

        # 判斷網域
        if 'detail.tmall.com' in self.driver.current_url:
            from Common.Defines.Resource import Tmall as RES
            title, price, options, image = Page.__Crawler(self, RES)
        elif 'item.taobao.com' in self.driver.current_url:
            from Common.Defines.Resource import Taobao as RES
            title, price, options, image = Page.__Crawler(self, RES)
        # elif '1688.com' in self.driver.current_url:
        #     PcUrl = self.driver.current_url.replace('https://m.1688.com', 'https://detail.1688.com')
        #     self.driver.get(PcUrl)
        #     from Common.Defines.Resource import Qr1688 as RES
        #     title, price, options, image = Page.crawler(self, RES)
        else:
            return '這個網址不支援爬蟲!'

        return self.driver.current_url, title, price, options, image

    def __Crawler(self, RES):                   #--爬蟲工作--
        # html sourcecode
        html = self.driver.page_source  
        selector = etree.HTML(html)

        # 1.標題
        title = selector.xpath(RES.TITLE)[0].text.strip()
        title = TranslateText(title, 'zh-tw')

        # 2.價格
        jPrice = Page.__IsElementExist(self, RES.PRICE)
        if jPrice == False:   #如果沒有顯示價格,就不爬
            price = '需登入取Price'
        elif jPrice == True:
            price = selector.xpath(RES.PRICE)[0].text
            
        # 3.顏色分類
        options = []
        jIsku = Page.__IsElementExist(self, RES.ISKU)
        if jIsku == True:     #如果有多顏多尺,就爬選項
            jTSaleProp = selector.xpath(RES.OPTION)
            for i in jTSaleProp:
                smallPic = i.xpath(RES.OPTION_TEXT)[0].text
                options.append(TranslateText(smallPic, 'zh-tw'))
        
        # 4-1.商品主圖
        image = []
        jULThumb = selector.xpath(RES.IMAGE)
        for li in jULThumb:
            if len(li.xpath(RES.IMAGE_SUB)) < 1:
                continue
            smallPic = li.xpath(RES.IMAGE_SUB)[0]
            if smallPic.startswith('http') is True: #是以http字符串開頭
                imglink = smallPic
            else:
                imglink = 'https:' + smallPic
            commonPic = imglink.replace(RES.IMG_SIZE, '400x400')   #替換圖片50*50至400*400
            image.append(commonPic)

        # 4-2.詳細頁所有圖片
        allImg = selector.xpath(RES.DESCIMAGE)
        for img in allImg:
            if img.startswith('http') is True: #是以http字符串開頭
                imglink = img
            else:
                imglink = 'https:' + img
            image.append(imglink)

        return title, price, options, image


if __name__ == '__main__':
    Page(webdriver).__GetPlatform(short_url="https://m.tb.cn/h.3NdhkXb")
        #short_url = "https://m.tb.cn/h.3mNFpaV" #淘寶
        #short_url = "https://m.tb.cn/h.3mipeHt" #淘寶多顏
        #short_url = "https://m.tb.cn/h.3NdhkXb" #天貓多顏
        #short_url = "https://qr.1688.com/share.html?secret=Og3sppfM" #阿里
        #short_url = "https://qr.1688.com/share.html?secret=2waeAxnn" #阿里
