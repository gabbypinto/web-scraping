#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import ShoppingList, Item

def index(request, id):
    ls = ShoppingList.objects.get(id=id)
    #the id starts at 2, 1 doesn't work
    return render(request, "scrape/list.html",{"ls":ls})

def home(request):
    return render(request, "scrape/home.html",{})
