# encoding: utf-8
import pandas

def get_rate():     #--拿台銀匯率--
    dfs = pandas.read_html("http://rate.bot.com.tw/xrt?Lang=zh-TW")
    # 取dsf的list 資料
    currency = dfs[0]
    #只取前五欄
    currency = currency.ix[:,0:5]
    #print (currency)
    # 重新命名欄位名稱 u-utf
    currency.columns = ['幣別','現金買入','現金賣出','即期買入','即期賣出']
    # 幣別值有重複字 利用正規式取英文代號
    currency['幣別'] = currency['幣別'].str.extract('\((\w+)\)')
    #print (currency)
    return currency

def save(currency): #--輸出到excel--
    currency.to_excel('currency.xlsx')

def fliter(currency, money):    #--幣別搜尋--
    fliter = (currency['幣別'] == money)
    country_result = currency[fliter]
    country_money = country_result.T #行列顛倒
    print(country_money)
    #return country_money

if __name__ == '__main__':
    currency = get_rate()
    fliter(currency, 'CNY')
