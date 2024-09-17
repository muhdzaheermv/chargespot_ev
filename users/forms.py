from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User

class UserRegisterForm(UserCreationForm):
    fullname=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Fullname"}))
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email"}))
    phonenumber=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Phonenumber"}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}))

    class Meta:
        model = User
        fields = ['username','email']