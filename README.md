# web-scraping

* running instructions:
  * mkdir -p .pip_cache
  * docker build -t django-markdown-editor .

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
    * https://docs.docker.com/compose/django/
    * https://docs.docker.com/engine/reference/builder/
    * https://www.caktusgroup.com/blog/2017/03/14/production-ready-dockerfile-your-python-django-app/
  * pip install django?
    * https://docs.djangoproject.com/en/3.0/topics/install/
