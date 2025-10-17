from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse  # ← IMPORTANT: Pour générer les URLs


class PublishedManager(models.Manager):  #herite de models.Manager
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published') #dans le but d'autorisé une pub

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_posts")
    STATUS_CHOICE = (
          ('draft','Draft'),
          ('published','Published')   
   )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICE,default='draft',max_length=10)
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="posted")

    objects = models.Manager() #defaut manager
    published = PublishedManager() #custom manager  aller au niveau de la vue remplacer objects par published

    #  pourpersonnaliser l'affichage dans admin 
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        """Retourne l'URL canonique de l'article"""
        return reverse('post_detail', args=[self.slug])
    
class Comment(models.Model):
     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    #  username = models.CharField(max_length=100)
    #  email = models.EmailField(max_length=200)
     author = models.ForeignKey(User, on_delete=models.CASCADE) #l'utilisateur etant deja connecter recupere une fois nom et email
     body = models.TextField()
     created = models.DateTimeField(auto_now_add=True)
     updated = models.DateTimeField(auto_now=True)
    
     def __str__(self):
        return self.post.title 

