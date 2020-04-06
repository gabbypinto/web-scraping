from django.urls import path

from . import views

#different views we have in this file
urlpatterns = [
    path("<str:name>", views.index, name='index'),
]
