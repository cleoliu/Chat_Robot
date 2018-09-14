'''
翻譯：外文-->中文｜中文-->英文
'''
#-*- coding: utf-8 -*-　
import json
import requests


def post_word(word): #-- POST --#
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

def get_reuslt(repsonse): #-- GET --#
    result = json.loads(repsonse)
    print ("輸入的詞為：%s" % result['translateResult'][0][0]['src'])
    print ("翻譯結果為：%s" % result['translateResult'][0][0]['tgt'])
    return (result['translateResult'][0][0]['tgt'])

def translator(word):
    list_trans = post_word(word)
    translate_reuslt = get_reuslt(list_trans)
    return translate_reuslt

if __name__ == '__main__':
    print (translator("翻譯字"))
