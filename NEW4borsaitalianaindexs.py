import pandas as pd
from selenium import webdriver
import time
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import urllib3
import zipfile
import csv



option = webdriver.ChromeOptions()

browser = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=option)
browser.set_window_size(444,444)



arr_urls = []
arr_stocknames = []
arr_stock_indexs = []
arr_isin_codes = []
arr_markets = []
arr_sectors = []
arr_ftses = []

currentitem = 3
currentpage = 1
arr_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"



cur_char = 0
cur_pagination = 1

while cur_char < len(arr_letters):
    time.sleep(3)
    #ilk harfi yükle
    browser.get("https://www.borsaitaliana.it/borsa/azioni/listino-a-z.html?initial=" + str(
        arr_letters[cur_char]) + "&lang=en&page=" + str(cur_pagination))
    #harfte 1den fazla sayfa var mı bak
    pages_len = len(
        browser.find_elements_by_xpath(
            "//*[@id=\"fullcontainer\"]/main/section/div[3]/article[1]/div[2]/div[2]/div/ul/*")) - 1
    print("Pages Length:" + str(pages_len))
    # şu anda zaten ilk sayfada

    total_urls = len(browser.find_elements_by_xpath(
        "//*[@id=\"fullcontainer\"]/main/section/div[3]/article[1]/div[2]/div[1]/div[2]/table/tbody/*")) - 2
    print("Total URLS: " + str(total_urls))
    current_row = 1
    while current_row <= total_urls:
        stock_url = browser.find_element_by_xpath(
            "//*[@id=\"fullcontainer\"]/main/section/div[3]/article[1]/div[2]/div[1]/div[2]/table/tbody/tr[" + str(
                current_row + 2) + "]/td[1]/article/div[1]/a").get_attribute('href')
        arr_urls.append(stock_url)
        print("Stock URL: " + stock_url)
        current_row += 1

    if pages_len <= -1:
        pages_len = 1

    a = 0
    #1den fazla sayfa varsa diğerlerini dolaş
    while a < pages_len - 1:

        time.sleep(3)
        #1. sayfayı bir daha yüklemesini engelle
        if (cur_pagination < pages_len):
            cur_pagination += 1
        browser.get("https://www.borsaitaliana.it/borsa/azioni/listino-a-z.html?initial=" + str(
            arr_letters[cur_char]) + "&lang=en&page=" + str(cur_pagination))

        a += 1
        total_urls = len(browser.find_elements_by_xpath("//*[@id=\"fullcontainer\"]/main/section/div[3]/article[1]/div[2]/div[1]/div[2]/table/tbody/*")) - 2
        print("Total URLS: " + str(total_urls))

        current_row = 1
        while current_row <= total_urls:
            stock_url = browser.find_element_by_xpath("//*[@id=\"fullcontainer\"]/main/section/div[3]/article[1]/div[2]/div[1]/div[2]/table/tbody/tr["+ str(current_row + 2) +"]/td[1]/article/div[1]/a").get_attribute('href')
            arr_urls.append(stock_url)
            print("Stock URL: " + stock_url)
            current_row += 1

    #1 ise alta yeni kod ekle

    #sayfa kısmını sıfırla
    cur_pagination = 1
    #diğer harflerden devam et
    cur_char += 1

print("ALL URLS SIZE: " + str(len(arr_urls)))


for x in arr_urls:
    browser.get(x)
    time.sleep(6)


    Name = browser.find_element_by_xpath('//*[@id="fullcontainer"]/main/section/div[3]/article/div/div/div[1]/h1/a').text
    arr_stocknames.append(str(Name))
    print("Stock Name: " + Name)
    print("*")

    Stock = browser.find_element_by_xpath('//*[@id="fullcontainer"]/main/section/div[6]/article/div/div[3]/div[2]/table/tbody/tr[5]/td[2]/span').text
    arr_stock_indexs.append(str(Stock))
    print("Stock Index: " + Stock)
    print("*")

    Isin = browser.find_element_by_xpath('//*[@id="fullcontainer"]/main/section/div[6]/article/div/div[3]/div[2]/table/tbody/tr[4]/td[2]/span').text
    arr_isin_codes.append(str(Isin))
    print("Isin code: " + Isin)
    print("*")

    try:
        Market = browser.find_element_by_xpath('//*[@id="fullcontainer"]/main/section/div[6]/article/div/div[3]/div[1]/table/tbody/tr[6]/td[2]').text
        arr_markets.append(str(Market))
        print("Market/Segment: " + Market)
        print("*")
    except:
        arr_markets.append("")
        print("No Market Found")
        print("*")

    try:
        Sector = browser.find_element_by_xpath('//*[@id="fullcontainer"]/main/section/div[6]/article/div/div[3]/div[2]/table/tbody/tr[6]/td[2]').text
        arr_sectors.append(str(Sector))
        print("Sector: " + Sector)
    except:
        arr_sectors.append("")
        print("No Sector Found")
        print("*")

    try:
        ftse = browser.find_element_by_xpath('//*[@id="fullcontainer"]/main/section/div[6]/article/div/div[3]/div[3]/table/tbody/tr/td[2]/span').text
        arr_ftses.append(str(ftse))
        print("Ftse Indices: " + ftse)
        print("*")
    except:
        arr_ftses.append("")
        print("No FTSE Indices Found")
        print("*")


my_df = {'Stock URL' : arr_urls,
         'Stock Name': arr_stocknames,
         'Stock Index': arr_stock_indexs,
         'Isin Code': arr_isin_codes,
         'Market/Segment': arr_markets,
         'Sector': arr_sectors,
         'Ftse Indices': arr_ftses}

df = pd.DataFrame(my_df)
print('DataFrame:\n', df)
new4borsaitalianaindexs1_csv_data = df.to_csv('new4borsaitalianaindexs1_csv_data', index = False)
print('\nCSV String:\n', new4borsaitalianaindexs1_csv_data)

print (df)
