#!/usr/bin/python
#-*- coding: utf-8 -*-　
import itchat
import time
import requests
import json
from translate import translator
#from shop import shop_find


def post_tulin_robot(text): #-- POST --#
    print("用戶說："+ text)
    if "翻譯" in text:    # 如果用戶發來的訊息有"翻譯"字樣,就 call translate api
        translate_word = text.replace('翻譯', '')
        translate_reuslt = translator(translate_word)
        return translate_reuslt
    #if "淘♂寳" in text:
        #shop_find(text)
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

# --自動回覆好友--
# @itchat.msg_register('Text')    #-- itchat裝飾器 --#
# def text_reply(msg):    #-- 接收wechat用戶發來的訊息(排除自己發的) --#
#     repa = post_tulin_robot(msg['Text'])
#     return  u"[我是機器人]{}".format(repa) # 回覆給微信好友

# 回覆給指定對象
@itchat.msg_register(itchat.content.TEXT)
def auto_reply(msg):
    # 搜尋微信好友
    readFriend=itchat.search_friends(name='Cleo')
    readFriendsName=readFriend[0]['UserName'] #@03243591003c97d1f11f4db3b80b8dc779f51b0db57a1ada9c1a488dc3c5b10c
    # 列印好友回覆的資訊
    print("message:%s"%msg['Text'])
    reply=post_tulin_robot(msg['Text'])
    if msg['FromUserName']==readFriendsName and msg['ToUserName']==readFriendsName:
        itchat.send(reply,toUserName=readFriendsName)

if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=1, hotReload=True)# Login QRcode
    #itchat.send('測試發送內容', toUserName='filehelper')
    itchat.run(debug=True)    
