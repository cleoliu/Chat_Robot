#!/usr/bin/python
#coding=utf8
import itchat
import time
import requests
import json
from translate import translator



def post_tulin_robot(text): #-- POST --#
    print("用戶說："+ text)
    if "翻譯" in text:    # 如果用戶發來的訊息有"翻譯"字樣,就 call translate api
        translate_word = text.replace('翻譯', '')
        translate_reuslt = translator(translate_word)
        return translate_reuslt
    else :  # 其他訊息則post圖靈回應
        url = 'http://www.tuling123.com/openapi/api'
        data = {
            'key': '6dd6b115f9484ba2a4aed7063ce54466',      # apiKey
            'info': text,                                   # 訊息發給圖靈
            'userid': 'wechat-robot',
        }
        # POST
        response = requests.post(url, data=data).json()
        return response["text"]


@itchat.msg_register('Text')    #-- itchat裝飾器 --#
def text_reply(msg):    #-- 接收wechat用戶發來的訊息(排除自己發的) --#
    repa = post_tulin_robot(msg['Text'])
    return  u"[我是機器人]{}".format(repa)


if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=2)  # Login QRcode
    #itchat.send('測試發送內容', toUserName='filehelper')
    itchat.run(debug=True)    
