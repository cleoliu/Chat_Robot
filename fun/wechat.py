import requests
from translate import Translator
from shop import shop_find
from workbook import Inser_file, Dele_file

def Trans(text):        #--英中翻譯--
    # 排除字眼
    translate_word = text.replace('翻譯', '')
    # api
    translate_reuslt = Translator(translate_word, 'en_ch')
    return translate_reuslt

def Shop(text):         #--商品爬蟲--
    # 爬蟲
    NewUrl, Item, Price, Option, Image = shop_find(text)
    # 寫入 excel
    Inser_file('product.xls', NewUrl, Item, Price, Option, Image)
    # whchat 回覆檔案
    SendFile()

def SendFile():         #--回覆檔案--
    itchat.send_file('product.xls', toUserName='Cleo')

def DeleFile(text):     #--刪除檔案--
    Dele_file(text)

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