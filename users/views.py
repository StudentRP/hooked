"""
logic created for handling user login and creation with django pre-made forms.
"""
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # old: standard user form for creation of new users (no email)
from django.contrib import messages # used for the 1 time flash messages
from .forms import MyUserRegisterForm
from django.contrib.auth.decorators import login_required # login required to see requests


def register(request):
    """if form submitted it returns here on a post request method specified in the html form. """
    if request.method == 'POST':
        form = MyUserRegisterForm(request.POST) # populated form
        if form.is_valid(): # django UserCreationForm does all checks to see if form is valid
            form.save() # saves to django's user model db
            username = form.cleaned_data.get('username') # gets username from the cleaned data dict
            messages.success(request, f'Account created for {username}. You can now login.') # creates a success message
            return redirect('login') # redirects the user to the home screen
    else:
        form = MyUserRegisterForm() # blank form
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')

