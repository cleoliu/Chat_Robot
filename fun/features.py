import requests
import itchat
from fun.translate import Translator
from fun.shop import Page
from fun.workbook import Inser_file, Dele_file


def Trans(text):        #--英中翻譯--
    # 排除字眼
    translate_word = text.replace('翻譯', '')
    # api
    translate_reuslt = Translator(translate_word, 'en_ch')

    return translate_reuslt

def Shop(text):         #--商品爬蟲--
    # get short url
    head = text.find("https://")
    short_url = text[head:head+25]
    # crawler
    url, Title, Price, Options, Image = Page(object).Get_platform(short_url)
    # write excel
    Inser_file('product.xls', url, Title, Price, Options, Image)
    # whchat reply file
    SendFile('product.xls')

    return ("已建檔完成：%s" %Title)

def SendFile(filename):         #--回傳檔案--
    itchat.send_file(filename)

def DeleFile(text):     #--刪除檔案--
    Dele_file(text)

def Rate(text):         #--匯率查詢--
    from fun import rate
    currency = rate.get_rate()
    money = text.replace('匯率', '')
    if money in currency['幣別'].values.tolist():     #如果有字眼在國家清單裡,單國匯率查詢
        result = rate.fliter(currency, money).to_csv(sep='：')
    else:   #沒有就回傳excle檔
        rate.save(currency)
        SendFile('currency.xlsx')
        result = '已建檔'

    return result

def Tuling(text):       #--圖靈 api--
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
