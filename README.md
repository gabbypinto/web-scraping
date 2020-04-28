# web-scraping

* running instructions:
  * mkdir -p .pip_cache
  * docker build -t scraper .
  * docker run -it -p 8020:8020 \
     -e DJANGO_SUPERUSER_USERNAME=admin \
     -e DJANGO_SUPERUSER_PASSWORD=sekret1 \
     -e DJANGO_SUPERUSER_EMAIL=admin@example.com \
     scraper

* if docker doesn't work  
  * cd webscrape
  * python3 manage.py runserver

* references:
  * markdown: https://guides.github.com/features/mastering-markdown/
  * scraping with selenium:
    * https://selenium-python.readthedocs.io/locating-elements.html
    * https://stackoverflow.com/questions/51496232/how-to-extract-product-informationtitle-price-review-asin-from-all-amazon-p
    * https://www.techbeamers.com/locate-elements-selenium-python/#locate-element-by-id
    * https://saucelabs.com/resources/articles/selenium-tips-css-selectors
  * alert popups
    * http://allselenium.info/python-selenium-handle-alerts-prompts-confirmation-popups/
  * dockerfile:
    * https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application
