'''
翻譯, 預設轉繁中
'''
#-*- coding: utf-8 -*-　
from googletrans import Translator

def TranslateText(word, dest=None):
    translator = Translator()
    # 1.如果沒有帶預轉語言
    if dest == None:
        autoFromType = translator.translate(word).src
        # 1-1.中轉英
        if autoFromType == 'zh-CN':
            return translator.translate(word).text
        # 1-2.自動轉中
        return translator.translate(word, 'zh-tw').text

    # 2.轉指定語言
    return translator.translate(word, dest).text

if __name__ == '__main__':
    print (TranslateText("翻譯字", 'en'))
    print (TranslateText("黑卡纸涂鸦珠光笔", 'zh-tw'))
