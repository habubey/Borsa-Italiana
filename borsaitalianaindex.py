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
