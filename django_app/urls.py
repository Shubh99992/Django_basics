from django.contrib import admin
from django.urls import include, path
from django_app import views
urlpatterns = [
    path("",views.index),
    path("team/<int:s>/",views.cls)

]

