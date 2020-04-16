from django.urls import path

from . import views
from django.conf.urls import url
from django.contrib import admin

# from .views import pagelogout

#different views we have in this file
urlpatterns = [
    path("<int:id>", views.index, name='index'),
    path("",views.home, name="home"), #home page
    path("create/",views.create,name="create"),
    path("view/",views.view,name="view"),


    # path(r'^signup$', signup, name='signup'),
    # path(r'^login', pagelogin, name='login'),

    #path("home/",views.home,name="home"),
]
