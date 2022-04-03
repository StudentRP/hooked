""" form created to modify the standard django form requiring the user to be registered to enter an email"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyUserRegisterForm(UserCreationForm):
    email = forms.EmailField() # adds email field

    class Meta:
        """ nested namespace for configs. Specifies the model the form is to interact with"""
        model = User # any changes are to save to this model
        fields = ['username', 'email', 'password1', 'password2'] # field to be shown and in the given order on the form