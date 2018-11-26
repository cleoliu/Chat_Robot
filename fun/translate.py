'''
翻譯
'''
#-*- coding: utf-8 -*-　
import json
import requests


def En_Trans_Ch(word): #-- 英中互轉 --#
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null' # api
    # data, "i" is translated word 
    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    # POST
    response = requests.post(url, data=key)
    # response
    if response.status_code == 200: #success
        return response.text
    else:
        print("有道詞典調用失敗") #failure
        return None

def Zhcn_Trans_Zhtw(word): #-- 簡轉繁 --#
    import zhconv
    return zhconv.convert(word, 'zh-tw')


def get_reuslt(trans_result): #-- JSON>str --#
    result = json.loads(trans_result)
    #print ("輸入的詞為：%s" % result['translateResult'][0][0]['src'])
    #print ("翻譯結果為：%s" % result['translateResult'][0][0]['tgt'])
    return (result['translateResult'][0][0]['tgt'])

def Translator(word, trans_type):
    if trans_type == 'en_ch':
        response_text = En_Trans_Ch(word)      # 英中互轉
        #print(response_text)
        trans_result = get_reuslt(response_text)
    elif trans_type == 'cn_tw':
        trans_result = Zhcn_Trans_Zhtw(word)  # 簡繁中互轉
    return trans_result

if __name__ == '__main__':
    print (Translator("翻譯字", 'en_ch'))
    print (Translator("黑卡纸涂鸦珠光笔", 'cn_tw'))
