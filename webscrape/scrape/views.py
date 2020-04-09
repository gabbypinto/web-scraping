#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ShoppingList, Item
from .forms import CreateNewList

def index(request, id):
    ls = ShoppingList.objects.get(id=id) #the id starts at 2, 1 doesn't work

    #{"save": ["save"], "c1":["clicked"]}
    #dict = name, value
    if request.method == "POST":
        print(request.POST)
        if request.POST.get("save"): #save == name of the button
            for item in ls.item_set.all():
                if request.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif request.POST.get("newItem"):
            txt = request.POST.get("new")
            if len(txt) > 2:
                ls.item_set.create(text = txt, complete=False)
            else:
                print("invalid")
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
            request.user.shoppinglist.add(t)

        return HttpResponseRedirect("/%i" %t.id) #id refers to the todo list we want to go to
    else:
        form = CreateNewList()

    return render(request, "scrape/create.html", {"form":form})
#POST for 'secret information' aka passwords
#GET for modifying the database
def view(request):
    return render(request, "scrape/view.html")
