import pandas as pd
from selenium import webdriver
import selenium
import time
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

arr_stocknames = []
arr_isin_codes = []
arr_urls = []
arr_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
a = 0

while a < len(arr_letters):
    browser.get("https://www.teleborsa.it/Quotazioni/Azioni-Italia/" + str(arr_letters[a]))
    length_of_table = len(browser.find_elements_by_xpath("//*[@id=\"ctl00_phContents_ctlListing_gvGrid\"]/tbody/*"))
    print(length_of_table)
    time.sleep(5)
    cur = 2
    while cur < (length_of_table + 1):

        name = browser.find_element_by_xpath("//*[@id=\"ctl00_phContents_ctlListing_gvGrid\"]/tbody/tr["+ str(cur)+ "]/td[1]/a").get_attribute("href")
        print(name)
        cur += 1
        arr_urls.append(name)

    a += 1

current_url_index = 1
for x in arr_urls:
    browser.get(x)
    time.sleep(6)
    print("\n\npageURL: " + x)
    names = (browser.find_element_by_xpath("//*[@id='ctl00_phContents_ctlHeader_pnlHeaderTop']/h1").text)
    print(names)
    arr_stocknames.append(str(names))

    isin = (browser.find_element_by_xpath("//*[@id=\"ctl00_phContents_ctlHeader_pnlHeaderMarketInfo\"]").text)
    arr_isin_codes.append(str(isin))

    print(isin)


my_df = {'Stock Names': arr_stocknames,
         'Isin Code': arr_isin_codes,
         'Url': arr_urls}

df = pd.DataFrame(my_df)
print('DataFrame:\n', df)
teleborsaindexs_csv_data = df.to_csv('teleborsaindexs_csv_data', index = False, encoding=   'utf-8')
print('\nCSV String:\n', teleborsaindexs_csv_data)

print (df)

