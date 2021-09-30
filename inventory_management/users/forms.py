from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# User Registration Form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    # Save the data from the form into the fields in User model
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

# Profile Update Form
class UserProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']