from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<i> This is the Italic App! </i>")