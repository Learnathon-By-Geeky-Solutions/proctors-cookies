from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='FirstName')
    last_name = forms.CharField(max_length=30, required=True, label='LastName')
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'username', 'password1', 'password2']