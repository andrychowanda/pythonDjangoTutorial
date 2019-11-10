from django.contrib import admin
from django.urls import path
from myIndexApp import views

urlpatterns = [
    path('', views.index),   
]
