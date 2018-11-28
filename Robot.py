#-*- coding: utf-8 -*-　
import itchat
from fun import features


def Job(text): #-- POST --#
    if '翻譯' in text:
        response = features.Trans(text)
    elif '淘♂寳' in text:
        response = features.Shop(text)
    elif '刪除' in text:
        response = features.DeleFile(text)
    elif '回傳' in text:
        response = features.SendFile(text.replace('回傳', ''))
    elif '匯率' in text:
        response = features.Rate(text)
    else :
        response = features.Tuling(text)

    return response


# --回覆給指定對象--
@itchat.msg_register(itchat.content.TEXT)
def auto_reply(msg):
    # search wechat friends
    readFriend=itchat.search_friends(name='Cleo')
    readFriendsName=readFriend[0]['UserName']
    # friend say
    print('message：%s' %msg['Text'])
    # Job
    reply = Job(msg['Text'])
    # reply
    if msg['FromUserName']==readFriendsName and msg['ToUserName']==readFriendsName:
        itchat.send(reply,toUserName=readFriendsName)


if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=1, hotReload=True) #--Login QRcode-- (enableCmdQR=1) 
    #itchat.send('測試發送內容', toUserName='filehelper')
    itchat.run(debug=True)


'''
msg['ToUserName']=='@03243591003c97d1f11f4db3b80b8dc779f51b0db57a1ada9c1a488dc3c5b10c'
'''