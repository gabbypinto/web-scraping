# web-scraping

* What is ScrapenSave?
  * Our django-based project is a web application that allows the user to create a
  shopping list and insert the link. In return, the program will return the product's name
  and price. 


* Running instructions:
  1. "git clone" this repo in your terminal/command prompt
  2. Type the following into your terminal in order to make and run your docker container
    * mkdir -p .pip_cache
    * docker build -t NAME .
      * "NAME" can be whatever you want
    * docker run -it -p 8020:8020 \
       -e DJANGO_SUPERUSER_USERNAME=admin \
       -e DJANGO_SUPERUSER_PASSWORD=sekret1 \
       -e DJANGO_SUPERUSER_EMAIL=admin@example.com \
       NAME
       * "NAME" can be whatever you want
  3. Visit: http://localhost:8020


* References:
  * scraping with selenium:
    * https://selenium-python.readthedocs.io/locating-elements.html
    * https://stackoverflow.com/questions/51496232/how-to-extract-product-informationtitle-price-review-asin-from-all-amazon-p
    * https://www.techbeamers.com/locate-elements-selenium-python/#locate-element-by-id
    * https://saucelabs.com/resources/articles/selenium-tips-css-selectors
  * alert popups
    * http://allselenium.info/python-selenium-handle-alerts-prompts-confirmation-popups/
  * dockerfile:
    * https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application
