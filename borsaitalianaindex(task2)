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


option = webdriver.ChromeOptions()

browser = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=option)
browser.set_window_size(444,444)


#İÇERİKleri ben aldım ama asıl index sayfasının loopunu alamadım https://www.borsaitaliana.it/borsa/azioni/listino-a-z.html?initial=A&lang=en bu sayfanın hem page numberlı hem
#hem a dan z ye gidiyor teleborsaindextask2 dosyasıyla benzer page var bunda bir tek
# arr_urls = []
# arr_stocknames = []
# arr_stock_indexs = []
# arr_isin_codes = []
# arr_markets = []
# arr_sectors = []
# arr_ftse_indices = []



browser.get("https://www.borsaitaliana.it/borsa/azioni/scheda/IT0005395071.html?lang=en")

Name = browser.find_element_by_xpath('//*[@id="fullcontainer"]/main/section/div[3]/article/div/div/div[1]/h1/a').text
print("Stock Name: " + Name)
print("*")
Stock = browser.find_element_by_xpath('//*[@id="fullcontainer"]/main/section/div[6]/article/div/div[3]/div[2]/table/tbody/tr[5]/td[2]/span').text
print("Stock Index: " + Stock)
print("*")
Isin = browser.find_element_by_xpath('//*[@id="fullcontainer"]/main/section/div[6]/article/div/div[3]/div[2]/table/tbody/tr[4]/td[2]/span').text
print("Isin code: " + Isin)
print("*")
Market = browser.find_element_by_xpath('//*[@id="fullcontainer"]/main/section/div[6]/article/div/div[3]/div[1]/table/tbody/tr[6]/td[2]').text
print("Market/Segment: " + Market)
print("*")
try:
    Sector = browser.find_element_by_xpath('//*[@id="fullcontainer"]/main/section/div[6]/article/div/div[3]/div[2]/table/tbody/tr[6]/td[2]').text
    print("Sector: " + Sector)
except:
    print("No Sector Found")

print("*")
try:
    Ftse = browser.find_element_by_xpath('//*[@id="fullcontainer"]/main/section/div[6]/article/div/div[3]/div[3]/table/tbody/tr/td[2]/span').text
    print("Ftse Indices: " + Ftse)
except:
    print("No FTSE Indices Found")

# arr_stocknames.append(str(Name))
# arr_stock_indexs.append(str(Stock))
# arr_isin_codes.append(str(Isin))
# arr_markets.append(str(Market))
# arr_sectors.append(str(Sector))
# arr_ftse_indices.append(str(Ftse))
#
#
#
# my_df = {'URL': arr_urls,
#          'Stock Name': arr_stocknames,
#          'Stock Index': arr_stock_indexs,
#          'Isin Code': arr_isin_codes,
#          'Market/Segment': arr_markets,
#          'Sector': arr_sectors,
#          'Ftse Indices': arr_ftse_indices}
#
# df = pd.DataFrame(my_df)
# print('DataFrame:\n', df)
# borsaitaliana12_csv_data = df.to_csv('borsaitaliana12_csv_data', index = False)
# print('\nCSV String:\n', borsaitaliana12_csv_data)
#
# print (df)
