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

browser.get("https://www.borsaitaliana.it/borsa/notizie/price-sensitive/home.html?lang=en")
time.sleep(10)
# COOKIE GELİYOR Çok önemli değil timesleep sayesinde kendim kapabiliyorm lakin aynı sıkıntı vurda da devam ediyour
# print ettiğimde bu sorun karşıma çıkıyor ve linkteki sayfada bir sonraki sayfaya geçmem gerekecek kodla html değişmiyor çünkü
# SORUN [<selenium.webdriver.remote.webelement.WebElement (session="754ebace6a2f7d57ab2bf1d1b9a85a07", element="c7af9b70-0877-44ba-ae31-494d5f521d6d")>]

dateandname = browser.find_elements_by_xpath('//*[@id="relases"]/a[1]/div[2]/h3')

print(dateandname)
