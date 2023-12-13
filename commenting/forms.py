# comments/forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'text']
        labels = {
            'name': 'Username',
            'email': 'E-mail',
            'text': 'Text',
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-unput'}),
            'name': forms.TextInput(attrs={'class': 'form-unput'}),
            'text': forms.TextInput(attrs={'class': 'form-unput'}),
        }

