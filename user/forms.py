from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.forms import ModelForm

class UserAuthenticated(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-unput'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

class UserRegistration(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-unput'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label='Repeat the password',widget=forms.PasswordInput(attrs={'class':'form-input'}))


    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name','password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'First Name',
            'last_name': 'Last Name'
        }
        widgets = {
            'email': forms.TextInput(attrs={ 'class': 'form-unput'}),
            'first_name': forms.TextInput(attrs={ 'class': 'form-unput'}),
            'last_name': forms.TextInput(attrs={ 'class': 'form-unput'}),
        }
    #
    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError('passwords do not match')
    #     return cd['password']

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if get_user_model().objects.filter(email=email).exists():
    #         raise forms.ValidationError('there is no such email')
    #     return email




