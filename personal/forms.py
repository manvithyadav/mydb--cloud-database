from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm) :

    name = forms.CharField(max_length=50, required=True)

    class Meta :
        model = User
        fields = ('name', 'username', 'password1', 'password2')