from selenium import webdriver

import time

#User Input
inLink = input("Enter any Link to the Product: ")

#Open Browser
browser = webdriver.Chrome(executable_path='/Users/gabbypinto/Documents/CPSC_Courses/CPSC_353/web-scraping/chromedriver')
browser.get(inLink)
time.sleep(1)


bestBuyTitle = browser.find_element_by_tag_name('h1').text  #works for most websites
print(bestBuyTitle)

#NEED A SERIES OF IF ELSE STATEMENTS HERE....

# price = browser.find_element_by_css_selector("span[class*='price']").text #works but prints twice for some reason, this is for matching substring= "price"
# print(price)

#if the above doesn't work then do...
# price = browser.find_element_by_css_selector("span[id*='price']").text #works but prints twice for some reason
# print(price)

# also do for div id
#also do for div class

browser.close()



#if price is not found, that means we have to use googleShopsAPI to find the cheapest one
# use try block or something bc of NoSuchElementException



#don't use this, this is just for reference...

#search---with find_element_by_name method
# productTitle = browser.find_element_by_id('productTitle').text
# print(productTitle)
#
# productPrice = browser.find_element_by_id('priceblock_ourprice').text
# print(productPrice)

#bestBuyPrice = browser.find_element_by_class_name('price').text
#price = browser.find_element_by_partial_class_name('price').text
