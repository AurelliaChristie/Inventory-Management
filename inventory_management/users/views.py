from django.shortcuts import redirect, render
from django.contrib import messages
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