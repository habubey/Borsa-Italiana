import pandas as pd
from selenium import webdriver
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




option = webdriver.ChromeOptions()
browser = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=option)
browser.get("https://www.teleborsa.it/News/Home.aspx?k=news_italia")
print(browser.find_elements_by_xpath('//*[@id="ctl00_phContents_GridView1_ctl03_lblTesto"]')[0].text)

elements = browser.find_elements_by_css_selector(".text")
for element in elements:
    print("*************************************************************")
    print(element.text)

url = "https://www.teleborsa.it/News/Home.aspx?k=news_italia&p=2"
tmp = list(url)
p = 2

elements = browser.find_elements_by_css_selector(".text")

while p < 5:
    tmp = list(url)
    tmp[-1] = str(p)
    url = ''.join(tmp)

    browser.get(url)
    print(url.title())

    elements = browser.find_elements_by_css_selector(".text")
    for element in elements:
        print("*************************************************************")
        print(element.text)

    p += 1
