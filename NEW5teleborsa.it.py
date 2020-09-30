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
import csv
import zipfile
import time
import pandas as pd


option = webdriver.ChromeOptions()

browser = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=option)
browser.set_window_size(444,444)


arr_urls = []
arr_titles = []
arr_dates = []
arr_topics = []
arr_contents = []
arr_stock_names = []
arr_stock_indexes = []
arr_page_nums = []

currentitem = 2

currentpage = 1
while currentpage < 100:
    browser.get("https://www.teleborsa.it/News/Home.aspx?from=2020-09-01&to=2020-09-30&k=news_italia&p=" + str(currentpage))

    while currentitem < 17:
        url = browser.find_element_by_xpath('//*[@id="ctl00_phContents_GridView1"]/tbody/tr[' + str(currentitem) + ']/td/div/div[1]/a').get_attribute('href')
        print(url)
        arr_urls.append(url)
        currentitem += 1

    currentpage += 1
    currentitem = 2

    time.sleep(7)
current_url_index = 1
for x in arr_urls:  # urlleri dolaş

    browser.get(x)
    print("\n\npageURL: " + x)
    currenttopic = 0
    if(str(x).__contains__("-video-") or str(x).__contains__("/Video/")):
        title = ""
        time.sleep(7)
        title = browser.find_element_by_xpath('//*[@id="ctl00_phContents_pnlContainer"]/h1').text
        print("Title: " + title)
        print("*")
        date = browser.find_element_by_xpath('//*[@id="ctl00_phContents_lblDataOra"]').text
        print("Date: " + date)
        print("*")

        try:
            topic = browser.find_elements_by_xpath('//*[@id="ctl00_phContents_pnlNews"]/div[1]/div[2]')
            if type(topic) is list:
                topic = topic[0].text
                topic = topic[0:topic.find('·') - 1]
            else:
                topic = "No topic"
        except:
            topic = "No topic"



        print("Topic: " + topic)
        print("*")
        content = browser.find_element_by_xpath('//*[@id="ctl00_phContents_pnlBody"]').text
        print("Content: " + content)
        print("*")

        stock_name = ""
        stock_index = ""
        try:
            stock_name = browser.find_element_by_xpath('//*[@id="ctl00_phContents_pnlNewsBody"]/a/span').text
            print("Stock Name: " + stock_name)
            print("*")
            src = browser.page_source
            ind = src.find('data-tlb-value')
            ind2 = src.find('\"', ind + 17)
            stock_index = src[ind + 16:ind2]
            print("Stock Index: " + stock_index)
        except:
            print("no stock info found")

        print("*")
        print("Total Page" + " Current News Order: " + str(currentpage) + " : " + str(current_url_index))
        arr_titles.append(str(title))
        arr_dates.append(str(date))
        arr_topics.append(str(topic))
        arr_contents.append(str(content))
        arr_stock_names.append(str(stock_name))
        arr_stock_indexes.append(str(stock_index))
        arr_page_nums.append(str(currentpage))
        current_url_index += 1
    else:
        time.sleep(6)
        title = ""
        try:
            title = browser.find_element_by_xpath('//*[@id="ctl00_phContents_pnlNews"]/h1').text
        except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.TimeoutException:
            
            arr_titles.append("Editore")
            arr_dates.append("Editore")
            arr_topics.append("Editore")
            arr_contents.append("Editore")
            arr_stock_names.append("Editore")
            arr_stock_indexes.append("Editore")
            arr_page_nums.append("Editore")
            continue
        print("Title: " + title)
        print("*")
        date = browser.find_element_by_xpath('//*[@id="ctl00_phContents_lblDataOra"]').text
        print("Date: " + date)
        print("*")
        topic = browser.find_elements_by_xpath('//*[@id="ctl00_phContents_pnlNews"]/div[1]/div[2]')
        if type(topic) is list:
            topic=topic[0].text
            topic = topic[0:topic.find('·') - 1]
        else:
            topic = "No topic"
        print("Topic: " + topic)
        print("*")
        content = browser.find_element_by_xpath('//*[@id="ctl00_phContents_pnlNewsBody"]').text
        print("Content: " + content)
        print("*")

        stock_name = ""
        stock_index = ""
        #burası da doğru
        try:
            stock_name = browser.find_element_by_xpath('//*[@id="ctl00_phContents_pnlNewsBody"]/a/span').text
            print("Stock Name: " + stock_name)
            print("*")
            src = browser.page_source
            ind = src.find('data-tlb-value')
            ind2 = src.find('\"', ind + 17)
            stock_index = src[ind + 16:ind2]
            print("Stock Index: " + stock_index)
        except:
            print("no stock info found")
        print("*")
        print("Total Page" + " Current News Order: " + str(currentpage) +" : " +str(current_url_index))
        arr_titles.append(str(title))
        arr_dates.append(str(date))
        arr_topics.append(str(topic))
        arr_contents.append(str(content))
        arr_stock_names.append(str(stock_name))
        arr_stock_indexes.append(str(stock_index))
        arr_page_nums.append(str(currentpage))
        current_url_index += 1


my_df = {'URL': arr_urls,
         'Title': arr_titles,
         'Date': arr_dates,
         'Topic': arr_topics,
         'Content': arr_contents,
         'Stock Name': arr_stock_names,
         'Stock Index': arr_stock_indexes,
         'Current Page': arr_page_nums}

print("Numbers:")
print(str(len(arr_urls)) + "\n" + str(len(arr_titles)) +"\n" + str(len(arr_dates)) + "\n" + str(len(arr_topics)) + "\n" + str(len(arr_contents)) + "\n" + str(len(arr_stock_names)) + "\n" + str(len(arr_stock_indexes)) + "\n" + str(len(arr_page_nums)))

df = pd.DataFrame(my_df)
print('DataFrame:\n', df)
new5teleborsadeneme1_csv_data = df.to_csv('new5teleborsadeneme1_csv_data', index = False)
print('\nCSV String:\n', new5teleborsadeneme1_csv_data)

print (df)
