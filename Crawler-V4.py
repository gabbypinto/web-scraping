from selenium import webdriver

import time

#User Input
inLink = input("Enter The Amazon Link to the Product: ")

#Open Browser
browser = webdriver.Chrome(executable_path='/Users/gabbypinto/Documents/CPSC_Courses/CPSC_353/web-scraping/chromedriver')
browser.get(inLink)
time.sleep(1)

#search---with find_element_by_xpath
# browser.find_element_by_xpath("").click()
# time.sleep(1)

#search---with find_element_by_name method
productTitle = browser.find_element_by_id('productTitle').text
print(productTitle)

productPrice = browser.find_element_by_id('priceblock_ourprice').text
print(productPrice)

#if price is not found, that means we have to use googleShopsAPI to find the cheapest one
# use try block or something bc of NoSuchElementException
