from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from registration.models import Profile
class SineUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email' ]
        labels = {'email' : 'Email'}
    
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']




