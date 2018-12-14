# Wechat ItChat
ItChat is an open source api for WeChat, a commonly-used Chinese social networking app.

**目前功能：**
- 翻譯
- 匯率查詢
- 圖靈回覆
- 商品爬蟲

# Requirements
* python 3

***

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

***

# EXE

```
$ cd Chat_Robot
$ python Robot.py
```