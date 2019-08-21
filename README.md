# Wechat ItChat

1. 翻譯
    - 包含關鍵字『翻譯』，範例輸入：『**翻譯 Try the following in this order**』。
2. 商品爬蟲
    - 使用分享鏈接，包含關鍵字『m.tb.cn』，爬蟲內容會寫進 **upload.xls** 和 **product.xls** 並回傳。
    - 刪除檔案，包含關鍵字『刪除』，範例輸入：『**刪除upload.xls**』或『**刪除product.xls**』。
    - 再次傳送檔案，包含關鍵字『回傳』，範例輸入：『**回傳upload.xls**』或『**回傳product.xls**』。
3. 匯率查詢
    - 全球匯率，匯出 excel 報表，輸入：『**匯率**』，回傳 **currency.xlsx**。
    - 單國匯率，回傳單國（幣別/現金買入/現金賣出/即期買入/即期賣出）文字訊息，範例輸入：『**SDG匯率**』（不分大小寫），回傳『幣別：SGD/現金買入：22.07/現金賣出：22.98/即期買入：22.56/即期賣出：22.74』。
    - 匯率計算機，範例輸入：『**SDG 28**』（不分大小寫），回傳範例『**匯率：22.98，換算台幣：643.44**』。
4. 圖靈回覆

# EXE

```
$ cd Chat_Robot
$ python Robot.py
```

***

# Requirements
* python 3


# Install 
### ItChat
```
$ pip install itchat
```

### 簡繁翻譯

```
$ pip install zhconv
```

### crawler

```
$ pip install requests
```

- selenium

```
$ pip install selenium
```

- chromedriver

```
$ wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
$ sudo apt install unzip
$ unzip chromedriver_linux64.zip
$ sudo mv chromedriver /usr/bin/chromedriver
$ sudo chown root:root /usr/bin/chromedriver
$ sudo chmod +x /usr/bin/chromedriver
$ chromedriver #安裝成功檢查
```

- chromium

```
$ sudo apt-get update
$ sudo apt-get install chromium-browser
```



### excel

```
$ pip install xlwt
$ pip install xlrd
$ pip install lxml
$ pip install xlutils
$ pip install pandas
```

