from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from app_login.models import UserProfile


class signupForm(UserCreationForm):
     email = forms.EmailField(label="Email Address",required= True)
     class Meta:
         model = User
         fields = ('username','first_name','last_name','email','password1','password2')

class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')
class Profilepic(forms.ModelForm):
     class Meta:
         model = UserProfile
         fields = ['profile_pic']
