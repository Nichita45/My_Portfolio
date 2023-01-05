from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Post

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "John",
        }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Doe"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "JohnDoe26"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "someone@domain.com"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "********"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "********"}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    class Meta:
        model = User
        fields = ['username', 'password']

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'An inspiring title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your article goes here!'}))
    class Meta:
        model = Post
        fields = ['title', 'content', 'thumbnail', 'tag']
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']