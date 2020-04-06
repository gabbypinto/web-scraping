#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import ShoppingList, Item
def index(request, name):
    ls = ShoppingList.objects.get(name=name)
    item  = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" % (ls.name,item.text))
                                        #or str(item.text) inside the ()
