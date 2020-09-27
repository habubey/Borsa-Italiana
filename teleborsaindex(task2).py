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

# "B" harfindeki stock indexlerin içine girip 46. satırındaki xpathi almam gerekiyor ama sayfanın neresine girersem giriyim aşağıdaki gibi bir sonuç alıyorm
# kolaylık olsun diye sadece 46 ve 47 deki satırı run etmek yeterli olacaktır. loopu eksik yapamadm
# <selenium.webdriver.remote.webelement.WebElement (session="5638d091139f41ed4fee9022ee0c1873", element="a64d3e25-201e-41c4-864f-3ba1e886fa2c")>


option = webdriver.ChromeOptions()

browser = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=option)
browser.set_window_size(444,444)

arr_urls = []

browser.get("https://www.teleborsa.it/Quotazioni/Azioni-Italia/B")
currentitem = 2

while currentitem < 46:
    url = browser.find_element_by_xpath('//*[@id="ctl00_phContents_ctlListing_gvGrid"]/tbody/tr[' + str(currentitem) + ']/td[1]/a').get_attribute('href')
    print(url)
    currentitem += 2

for x in arr_urls:  # urlleri dolaş

    browser.get(x)
    print("\n\npageURL: " + x)

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

# çalışıyor csv yapılacak

option = webdriver.ChromeOptions()

browser = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=option)
browser.set_window_size(444,444)

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
    print(browser.find_element_by_xpath("//*[@id='ctl00_phContents_ctlHeader_pnlHeaderTop']/h1").text)
    print(browser.find_element_by_xpath("//*[@id=\"ctl00_phContents_ctlHeader_pnlHeaderMarketInfo\"]").text)





#browser.get("https://www.teleborsa.it/azioni/buzzi-unicem-rnc-bzur-it0001369427-SVQwMDAxMzY5NDI3")
#print(browser.find_elements_by_xpath('//*[@id="ctl00_phContents_ctlHeader_pnlHeaderMarketInfo"]'))
