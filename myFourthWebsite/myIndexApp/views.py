from django.shortcuts import render
from myIndexApp.models import User

def index(request):
    mydata = User.objects.all()
    userDataDict = {'usersData':mydata}
    return render(request, 'index.html', context=userDataDict)

