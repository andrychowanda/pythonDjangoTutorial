from django.contrib import admin
from django.urls import path
from italicApp import views

urlpatterns = [
    path('', views.index , name='italic'),
]
