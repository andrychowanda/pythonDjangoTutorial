"""myFifthWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.formInputUserView, name='formUser'),
    path('viewDetail/<str:key>', views.viewDetailView, name='viewDetail'),
    path('delete/<str:key>', views.deleteUserView, name='delete'),
    path('update/<str:key>', views.updateUserView, name='update'),
    path('admin/', admin.site.urls),
]

