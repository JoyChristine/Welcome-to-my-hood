from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile,Business,Neighbourhood,Post
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email' ,'password1', 'password2']

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic','bio','neighbourhood']

class CreateNeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['image','name','location','about','health_dept','police_dept']

class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('image','title','context')
        
class AddBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['image','name','description','email']

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image','title','context']