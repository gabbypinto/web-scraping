from django.urls import path

from . import views
rom django.conf.urls import url
from django.contrib import admin
from .views import signup, pagelogin, pagelogout

#different views we have in this file
urlpatterns = [
    path("<int:id>", views.index, name='index'),
    path("",views.home, name="home"), #home page
    path("home/",views.home,name="home"),
    path("create/",views.create,name="create"),
    path("view/",views.view,name="view"),
    path(r'^signup$', signup, name='signup'),
    path(r'^login', pagelogin, name='login'),
    path(r'^logout', pagelogout, name='logout'),
]
