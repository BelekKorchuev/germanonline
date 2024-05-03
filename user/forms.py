from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserAuthenticated(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-unput'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class UserRegistration(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-unput'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Repeat the password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'First Name',
            'last_name': 'Last Name'
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-unput'}),
            'first_name': forms.TextInput(attrs={'class': 'form-unput'}),
            'last_name': forms.TextInput(attrs={'class': 'form-unput'}),
        }
