from django.shortcuts import render, get_object_or_404
from myApp import forms
from myApp.forms import newUserForm
from myApp.models import User

def index(request):
    myUserData = User.objects.all()
    myUserDataDict = {'usersData':myUserData}
    return render(request, 'index.html', context=myUserDataDict)


def formUserView(request):
    form = forms.formUser()
    if request.method == 'POST':
        form = forms.formUser(request.POST)
        if form.is_valid():
            print("Validation Success!")

    return render(request, 'form.html',{'form':form})

def formInputUserView(request):
    form = forms.newUserForm()
    if request.method == 'POST':
        form = forms.newUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Validation Error!")
    return render(request, 'form.html',{'form':form})

def viewDetailView(request, key):
    #userDetail = get_object_or_404(User, userName=key)
    userDetail = User.objects.get(userName__exact=key)
    return render(request, 'viewDetail.html', {'usersData':userDetail})


def deleteUserView(request, key):
    userDelete = User.objects.get(userName__exact=key)
    if request.method == 'POST':
        userDelete.delete()
        return index(request)
    return render(request, 'delete.html', {'usersData':userDelete})

def updateUserView(request, key):
    userUpdate = User.objects.get(userName__exact=key)
    form = forms.newUserForm(instance=userUpdate)
    if request.method == 'POST':
        form = forms.newUserForm(request.POST, instance=userUpdate)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Validation Error!")
    return render(request, 'form.html',{'form':form})

