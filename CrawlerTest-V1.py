from selenium import webdriver

import time

browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
browser.get('https://wcca.wicourts.gov/case.html')
time.sleep(3)

#First Name
a = browser.find_element_by_xpath("//input[@id ='lastName']")
a.send_Keys("Smith")
#Last Name
b = browser.find_element_by_xpath("//input[@id ='firstName']")
b.send_Keys("John")

browser.find_element_by_xpath("//a[@id ='search']").click() 