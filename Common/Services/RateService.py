'''
匯率爬蟲
'''
# encoding: utf-8
import pandas

def GetRate():                  #--1.拿台銀全國匯率--
    dfs = pandas.read_html("http://rate.bot.com.tw/xrt?Lang=zh-TW")
    # 1.取dsf的list資料
    currency = dfs[0]
    # 2.只取前五欄
    currency = currency.iloc[:,0:5]
    # 3.加上header欄位名稱
    currency.columns = ['幣別','現金買入','現金賣出','即期買入','即期賣出']
    # 4.幣別值有重複字,利用正規式取英文代號
    currency['幣別'] = currency['幣別'].str.extract('\((\w+)\)')
    return currency

def CountryList():              #--各國貨幣簡稱list--
    currency = GetRate()
    countryList = currency['幣別'].values.tolist()
    return countryList

def Save(currency):             #--輸出到excel--
    currency.to_excel('currency.xlsx')

def Fliter(currency, money):    #--2.單國匯率查詢,輸入:USD匯率--
    fliter = (currency['幣別'] == money)
    countryResult = currency[fliter]
    countryMoney = countryResult.T #(將行列顛倒)
    return countryMoney

def Exchange(country):          #--3.出國時參考"現金賣出"價:回傳匯率(ex:4.503)--
    currency = GetRate()
    fliter = (currency['幣別'] == country)
    countryResult = currency[fliter]
    return countryResult.iloc[0,2]



if __name__ == '__main__':
    # 1.全國匯率
    currency = GetRate()
    # 2.單國匯率
    Fliter(currency, 'CNY')
    # 3.金額換匯
    Exchange('CNY')
