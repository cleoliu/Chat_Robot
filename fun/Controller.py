import requests
import itchat
from fun.translate import Translator
from fun.shop import Page
from fun.workbook import Inser_file, Dele_file, Up_file
from fun import rate
import os
import re

def Trans(text):                    #--英中翻譯--
    # 1.排除'翻譯'字眼
    translate_word = text.replace('翻譯', '')                   
    # 2.翻譯 api
    translate_reuslt = Translator(translate_word, 'en_ch')      
    return translate_reuslt

def Shop(text):                     #--商品爬蟲--
    itchat.send('處理中...')
    # 1.get short url
    head = text.find('https://')
    short_url = text[head:head+25]
    # 2.crawler
    url, Title, Price, Options, Image = Page(object).Get_platform(short_url)
    # 3.write excel
    if text[2:] == '00':
        Title = '◍二手◍' + Title
    Inser_file('product.xls', url, Title, Price, Options, Image)
    Up_file('upload.xls', Title, Price, Options, Image)
    # 4.whchat reply file
    SendFile('product.xls')
    SendFile('upload.xls')
    return ('Creat：%s' %Title)

def SendFile(filename):             #--回傳檔案--
    if os.path.isfile(filename) == False:
        return ('%s：檔案不存在' %filename)
    else:
        return itchat.send_file(filename)

def DeleFile(text):                 #--刪除檔案--
    filename = text.replace('刪除', '')
    if os.path.isfile(filename) == False:
        return ('%s：檔案不存在' %filename)
    else:
        Dele_file(filename)
        return ('Delete file done：%s' %filename)

def Rate(text):                     #--匯率查詢--
    currency = rate.get_rate()
    money = text.replace('匯率', '')
    # 1-1.如果有字眼在國家清單裡,單國匯率查詢
    if money in currency['幣別'].values.tolist():
        result = rate.fliter(currency, money).to_csv(sep='：')
    # 1-2.如果沒有國家字眼就回傳全球匯率之excle檔
    else:
        rate.save(currency)
        SendFile('currency.xlsx')
        result = '已建檔'
    return result

def ExchangeRate(text):             #--出國時參考"現金賣出"價:回傳(金額*匯率)--
    # 1.排除非數字的字眼,為計算金額
    price = "".join(re.findall(r"\d+\.?\d*",text))
    # 2.抓出國家字眼
    country = "".join([country for country in rate.countryList() if country in text])
    # 3.單國的'現金賣出'價
    exchange = rate.exchange(country)
    # 4.換算台幣(四捨五入) = 計算金額(上1)*單國的現金賣出價(上3)
    twd = round(float(price)*float(exchange))
    return ('匯率：%s，換算台幣：NT$%s' %(exchange, twd))

def Tuling(text):                   #--圖靈 api--
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
