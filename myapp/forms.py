from django import forms
from .models import *
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
