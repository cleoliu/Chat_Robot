import requests
import itchat
from Common.Services import RateService, ShopService, TranslateService, WorkbookService
import os
import re

def Trans(text):                                #--英中翻譯--
    # 1.排除'翻譯'字眼
    translateWord = text.replace('翻譯', '')                   
    # 2.翻譯 api
    translateReuslt = TranslateService.TranslateText(translateWord)      
    return translateReuslt

def Shop(text, userId, userName):                           #--商品爬蟲--
    itchat.send('處理中...', userId)
    # 1.get short url
    head = text.find('https://')
    shortUrl = text[head:head+25]
    # 2.crawler
    url, title, price, options, image = ShopService.Page(object).Get_platform(shortUrl)
    # 3.write excel
    if text[2:] == '00':
        title = '◍二手◍' + title
    WorkbookService.InserFile('product_%s.xls' %userName, url, title, price, options, image)
    WorkbookService.UpFile('upload_%s.xls' %userName, userName, title, price, options, image)
    # 4.whchat reply file
    SendFile('product_%s.xls' %userName, userId)
    SendFile('upload_%s.xls' %userName, userId)
    return ('Creat：%s' %title)

def SendFile(filename, toUserName=None):        #--回傳檔案--
    if os.path.isfile(filename) == False:
        return ('%s：檔案不存在' %filename)
    else:
        return itchat.send_file(filename, toUserName)

def DeleFile(text):                             #--刪除檔案--
    filename = text.replace('刪除', '')
    if os.path.isfile(filename) == False:
        return ('%s：檔案不存在' %filename)
    else:
        WorkbookService.DeleFile(filename)
        return ('Delete file done：%s' %filename)

def Rate(text, userId):                           #--匯率查詢--
    currency = RateService.GetRate()
    money = text.replace('匯率', '')
    # 1-1.如果有字眼在國家清單裡,單國匯率查詢
    if money in currency['幣別'].values.tolist():
        result = RateService.Fliter(currency, money).to_csv(sep='：')
    # 1-2.如果沒有國家字眼就回傳全球匯率之excle檔
    else:
        RateService.Save(currency)
        SendFile('currency.xlsx', userId)
        result = '已建檔'
    return result

def ExchangeRate(text):                         #--出國時參考"現金賣出"價:回傳(金額*匯率)--
    # 1.排除非數字的字眼,為計算金額
    price = "".join(re.findall(r"\d+\.?\d*",text))
    # 2.抓出國家字眼
    country = "".join([country for country in RateService.CountryList() if country in text])
    # 3.單國的'現金賣出'價
    exchange = RateService.Exchange(country)
    # 4.換算台幣(四捨五入) = 計算金額(上1)*單國的現金賣出價(上3)
    twd = round(float(price)*float(exchange))
    return ('匯率：%s，換算台幣：NT$%s' %(exchange, twd))

def Tuling(text):                               #--圖靈 api--
    url = 'http://www.tuling123.com/openapi/api'
    data = {
            'key': '6dd6b115f9484ba2a4aed7063ce54466',      # apiKey
            'info': text,                                   # 訊息發給圖靈
            'userid': 'wechat-robot',
            }
    # POST
    response = requests.post(url, data=data).json()
    return response["text"]



if __name__ == '__main__':
    Shop("https://m.tb.cn/h.3mNFpaV")
