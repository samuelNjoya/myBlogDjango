from django import forms
from django.forms import Textarea,TextInput,EmailInput
from .models import Comment,Post

class commentform(forms.ModelForm):
      # username = forms.CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}))
      # email = forms.EmailField( widget=forms.EmailInput(attrs={'class': 'form-control'}))
      body = forms.CharField( widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
      class Meta:
            model = Comment
            fields = ['body']


class PostForm(forms.ModelForm):
    """
    Formulaire pour créer et modifier les articles
    Utilise tous les champs du modèle Post sauf l'auteur qui est défini automatiquement
    """
    class Meta:
        model = Post
        fields = ['title', 'slug', 'category', 'body', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Titre de votre article'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'titre-en-minuscules-sans-espaces'
            }),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 15,
                'placeholder': 'Contenu de votre article...'
            }),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
        help_texts = {
            'slug': 'Version URL-friendly du titre (minuscules, tirets)',
            'status': '"Brouillon" pour sauvegarder, "Publié" pour rendre visible',
        }