from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile,Business
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email' ,'password1', 'password2']

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','neighbourhood']

class AddBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name','description','email']