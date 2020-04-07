#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ShoppingList, Item
from .forms import CreateNewList

def index(request, id):
    ls = ShoppingList.objects.get(id=id)
    #the id starts at 2, 1 doesn't work
    return render(request, "scrape/list.html",{"ls":ls})

def home(request):
    return render(request, "scrape/home.html",{})

def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ShoppingList(name=n)
            t.save()
        return HttpResponseRedirect("/%i" %t.id) #id refers to the todo list we want to go to
    else:
        form = CreateNewList()

    return render(request, "scrape/create.html", {"form":form})

#POST for 'secret information' aka passwords
#GET for modifying the database
