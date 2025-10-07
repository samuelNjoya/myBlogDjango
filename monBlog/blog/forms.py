from django import forms
from django.forms import Textarea,TextInput,EmailInput
from .models import Comment

class commentform(forms.ModelForm):
      username = forms.CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}))
      email = forms.EmailField( widget=forms.EmailInput(attrs={'class': 'form-control'}))
      body = forms.CharField( widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
      class Meta:
            model = Comment
            fields = ['username','email','body']