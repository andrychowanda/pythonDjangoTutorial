from django.shortcuts import render
from myFormApp import forms
from myFormApp.forms import newUserForm
from myFormApp.models import User

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

