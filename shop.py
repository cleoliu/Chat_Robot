#-*- coding: utf-8 -*-　
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep,time

def shop_find():
    #head = word.find("https://") #word[head:head+25]
    driver = webdriver.Chrome(r"C:\chromedriver.exe")
    driver.implicitly_wait(30)
    driver.get("https://m.tb.cn/h.3m60CGL")
    sleep(3)
    pageSource = driver.page_source
    print(pageSource)

shop_find()