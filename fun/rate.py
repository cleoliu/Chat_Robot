'''
匯率爬蟲
'''
# encoding: utf-8
import pandas

def get_rate():                 #--拿台銀匯率--
    dfs = pandas.read_html("http://rate.bot.com.tw/xrt?Lang=zh-TW")
    # 1.取dsf的list資料
    currency = dfs[0]
    # 2.只取前五欄
    currency = currency.ix[:,0:5]
    # 3.加上header欄位名稱
    currency.columns = ['幣別','現金買入','現金賣出','即期買入','即期賣出']
    # 4.幣別值有重複字,利用正規式取英文代號
    currency['幣別'] = currency['幣別'].str.extract('\((\w+)\)')
    return currency

def countryList():              #--各國貨幣簡稱list--
    currency = get_rate()
    country_list = currency['幣別'].values.tolist()
    return country_list

def save(currency):             #--輸出到excel--
    currency.to_excel('currency.xlsx')

def fliter(currency, money):    #--單國匯率查詢,輸入:USD匯率--
    fliter = (currency['幣別'] == money)
    country_result = currency[fliter]
    country_money = country_result.T #將行列顛倒
    return country_money

def exchange(country):          #--出國時參考"現金賣出"價:回傳匯率(ex:4.503)--
    currency = get_rate()
    fliter = (currency['幣別'] == country)
    country_result = currency[fliter]
    return country_result.iloc[0,2]



if __name__ == '__main__':
    #全國匯率
    currency = get_rate()
    #單國匯率
    fliter(currency, 'CNY')
    #金額換匯
    exchange('CNY')
