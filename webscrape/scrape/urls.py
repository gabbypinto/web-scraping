from django.urls import path

from . import views

#different views we have in this file
urlpatterns = [
    path("<int:id>", views.index, name='index'),
    path("",views.home, name="home") #home page
]
