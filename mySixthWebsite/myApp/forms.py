from django import forms
from myApp.models import User 

class formUser(forms.Form):
    userName = forms.CharField()
    firstName = forms.CharField()
    lastName = forms.CharField()
    address = forms.CharField(widget=forms.Textarea)
    dob = forms.DateField(widget=forms.SelectDateWidget)
    phoneNumber = forms.CharField()

class newUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'


