from django import forms 

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta: #what we want in this form ----
        model = User
        fields = ["username", "email", "password1", "password2"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]

