#-*- coding: utf-8 -*-　
import itchat
from Common import Controller
from Common.Services import RateService

def Job(text, userId, userName): #-- 觸發各種事件 --#
    # 1.翻譯
    if '翻譯' in text:
        response = Controller.Trans(text)

    # 2.商品爬蟲
    elif 'm.tb.cn' in text:
        response = Controller.Shop(text, userId, userName)
    elif '刪除' in text:
        response = Controller.DeleFile(text)
    elif '回傳' in text:
        response = Controller.SendFile(text.replace('回傳', ''))

    # 3.匯率查詢
    elif '匯率' in text:
        response = Controller.Rate(text.upper(), userId)
    elif "".join([country for country in RateService.CountryList() if country in text.upper()]):
        response = Controller.ExchangeRate(text.upper())
    
    # 4.圖靈回覆
    else :
        response = Controller.Tuling(text)

    return response


# --回覆給指定對象--
@itchat.msg_register(itchat.content.TEXT)
def auto_reply(msg):
    # friend say
    print('message：%s' %msg['Text'])
    
    ## 傳給自己:second903商店
    friendCleoId = itchat.search_friends(name='Cleo')[0]['UserName']
    if msg['ToUserName']==friendCleoId:
        print(msg['ToUserName'], friendCleoId)
        itchat.send(Job(msg['Text'], friendCleoId, 'Cleo'), toUserName=friendCleoId)

    ## 傳給Kini:Kini商店
    friendKiniId = itchat.search_friends(name='Kini')[0]['UserName']
    if msg['ToUserName']==friendKiniId:
        print(msg['ToUserName'], friendKiniId)
        itchat.send(Job(msg['Text'], friendKiniId, 'Kini'), toUserName=friendKiniId)


if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=1, hotReload=True) #--Login QRcode-- (enableCmdQR=1) 
    #itchat.send('測試發送內容', toUserName='filehelper')
    itchat.run(debug=True)

'''
msg['ToUserName']=='@03243591003c97d1f11f4db3b80b8dc779f51b0db57a1ada9c1a488dc3c5b10c'
'''