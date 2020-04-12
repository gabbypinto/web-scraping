from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import time # for time.sleep(#seconds)

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("--disable-notifications")
# chrome_options.add_argument('--headless') <--research but not too important atm
#Open Browser
browser = webdriver.Chrome(options=chrome_options,executable_path='/Users/gabbypinto/Documents/CPSC_Courses/CPSC_353/web-scraping/chromedriver')
browser.minimize_window()
#handles alert and popup boxes
if NoAlertPresentException:
    pass
elif UnexpectedAlertPresentException:
    alert_obj = browser.switch_to.alert
    alert_obj.dismiss()
#User Inputs the link
inLink = input("Enter product link: ")
browser.get(inLink)

# grabs the title of the product, which is usually tagged with a h1
productTitle = browser.find_element_by_tag_name('h1').text  #works for almost all websites
print(productTitle)


try:
    price = browser.find_element_by_css_selector("span[class*='price']") #don't change this, this works for most websites
    print(price.text)
except NoSuchElementException:
    pass

try:
    price = browser.find_element_by_css_selector("span[class*='Price']")
    print(price.text)
except NoSuchElementException:
    pass

try:
    price = browser.find_element_by_css_selector("span[id*='price']")
    print(price.text)
except NoSuchElementException:
    pass

try:
    price = browser.find_element_by_css_selector("div[class*='price']")
    print(price.text)
except NoSuchElementException:
    pass

try:
    price = browser.find_element_by_css_selector("div[id*='price']")
    print(price.text)
except NoSuchElementException:
    pass

try:
    price = browser.find_element_by_css_selector("div[id*='ItemPrice']")
    print(price.text)
except NoSuchElementException:
    pass

browser.close()

# print(price.text)
# print(price.size)
