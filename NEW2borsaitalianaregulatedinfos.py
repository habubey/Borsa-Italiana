import pandas as pd
from selenium import webdriver
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
from selenium.webdriver import ActionChains
import pickle
import selenium.webdriver


option = webdriver.ChromeOptions()
browser = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=option)
browser.set_window_size(444,444)
arr_urls = []
arr_comps = []
arr_titles = []
arr_dates = []
arr_pdf_urls = []

currentpage = 1
while currentpage < 6:
    browser.get("https://www.borsaitaliana.it/borsa/notizie/price-sensitive/risultati.html?lang=en&startingDate=20200901&endingDate=20200925&page=" + str(currentpage))
    time.sleep(3)
    items = browser.find_elements_by_xpath("//*[@id=\"relases\"]/*")
    items_size = len(items)
    cur = 1

    currentpage += 1
    while cur < items_size:
        title = browser.find_element_by_xpath("//*[@id=\"relases\"]/a[" + str(cur) + "]/div[2]/h3").text
        date = browser.find_element_by_xpath("//*[@id=\"relases\"]/a[" + str(cur) + "]/div[2]/div/span[1]").text
        comp = browser.find_element_by_xpath("//*[@id=\"relases\"]/a[" + str(cur) + "]/div[2]/div/span[2]").text
        link = browser.find_element_by_xpath("//*[@id=\"relases\"]/a[" + str(cur) + "]").get_attribute("href")
        arr_urls.append(str(link))
        arr_titles.append(str(title))
        arr_dates.append(str(date))
        arr_comps.append(str(comp))

        print("Link: " + link)
        print("*")
        print("Company Name: " + comp)
        print("*")
        print("Title: " + title)
        print("*")
        print("Date: " + date)


        cur += 1

urls_size = len(arr_urls)

cur = 0
while cur < urls_size:
    browser.get(str(arr_urls[cur]))
    time.sleep(6)
    pdf_urls = browser.find_element_by_xpath("//*[@id=\"fullcontainer\"]/main/section/div[3]/div[1]/span/a").get_attribute("href")
    arr_pdf_urls.append(str(pdf_urls))
    cur+=1


print(pdf_urls)
print(arr_pdf_urls)


my_df = {'Link': arr_urls,
         'Company Name': arr_comps,
         'Title': arr_titles,
         'Date': arr_dates,
         'PDF Urls': arr_pdf_urls}


df = pd.DataFrame(my_df)
print('DataFrame:\n', df)
borsaitalianareg_csv_data = df.to_csv('borsaitalianareg_csv_data', index = False, encoding=   'utf-8')
print('\nCSV String:\n', borsaitalianareg_csv_data)

print (df)
