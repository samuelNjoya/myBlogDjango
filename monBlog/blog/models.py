from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class post(models.Model):

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
    publish = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="posted")

    #  pourpersonnaliser l'affichage dans admin 
    def __str__(self):
        return self.title
    
    
