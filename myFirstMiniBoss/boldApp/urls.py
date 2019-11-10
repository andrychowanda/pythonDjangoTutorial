from django.contrib import admin
from django.urls import path
from boldApp import views

urlpatterns = [
    path('', views.index , name='bold'),
]
