from django.shortcuts import render

def index(request):
    myVar = 30
    myDict = {'my_variable' : 'Value is ' + str(myVar)}
    return render(request, 'index.html', context=myDict)

