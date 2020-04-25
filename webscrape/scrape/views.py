# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import ShoppingList, Item
from .forms import CreateNewList
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import time # for time.sleep(#seconds)


def index(request, id):
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--headless")
    ls = ShoppingList.objects.get(id=id) #the id starts at 2, 1 doesn't work
    if ls in request.user.shoppingList.all():
        #{"save": ["save"], "c1":["clicked"]}
        #dict = name, value
        if request.method == "POST":
            if request.POST.get("save"): #save == name of the button
                for item in ls.item_set.all():
                    if request.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
                    return render(request, "scrape/view.html",{})
            elif request.POST.get("newItem"):
                txt = request.POST.get("new")
                if len(txt) > 2:
                  ls.item_set.create(text = txt, complete=False)
                	#Open Browser
                  browser = webdriver.Chrome(options=chrome_options,executable_path='/Users/gabbypinto/Documents/CPSC_Courses/CPSC_353/web-scraping/webscrape/scrape/chromedriver')
                  browser.minimize_window()
                	#handles alert and popup boxes
                  if NoAlertPresentException:
                     pass
                  elif UnexpectedAlertPresentException:
                     alert_obj = browser.switch_to.alert
                     alert_obj.dismiss()
                	# #User Inputs the link
                  browser.get(txt)
                  print('hola')
                	# # grabs the title of the product, which is usually tagged with a h1
                  productTitle = browser.find_element_by_tag_name('h1').text  #works for almost all websites
                  print(productTitle)
                  browser.close()
                else:
                    print("invalid")
            elif request.POST.get("delete"):
                for item in ls.item_set.all():
                    if request.POST.get("c" + str(item.id)) == "clicked":
                        item.delete()
            elif request.POST.get("deleteList"):
                print("delete list")
                ls.delete()
                return render(request,"scrape/view.html",{})
        return render(request, "scrape/list.html",{"ls":ls})
    return render(request, "scrape/view.html",{})

def home(request):
    return render(request, "scrape/home.html",{})

def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ShoppingList(name=n)
            t.save()
            request.user.shoppingList.add(t)
        return HttpResponseRedirect("/%i" %t.id) #id refers to the todo list we want to go to
    else:
        form = CreateNewList()

    return render(request, "scrape/create.html", {"form":form})

#POST for 'secret information' aka passwords
#GET for modifying the database

#the view function is for viewing a list
def view(request):
    return render(request, "scrape/view.html")

#def renameItem(request):
