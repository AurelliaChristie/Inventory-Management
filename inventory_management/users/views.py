from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import *

# User Registration
def user_register(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} has been created! You are now able to log in.')
            return redirect('users-login')
        else:
            form = UserRegistrationForm()
    
    context = {
        'form': form,
        'title': 'User Registration'
    }
    return render(request, 'users/user_register.html', context)

# User Profile
@login_required()
def user_profile(request):
    form = UserProfileUpdateForm(instance = request.user)
    if request.method == "POST":
        form = UserProfileUpdateForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('users-profile')
        else:
            form = UserProfileUpdateForm(instance = request.user)
        
    context = {'form': form}
    return render(request, 'users/user_profile.html', context)