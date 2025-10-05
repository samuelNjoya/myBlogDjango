from django.contrib import admin
from .models import post, Comment

# importer mon model pour que ça s'affiche dans admin de django
# admin.site.register(post)

@admin.register(post) #permet d'ajouter dans le site d'admin de django
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','body','author','status','created','publish')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('title','body')
    ordering = ('title','author')
    list_filter = ('title','author','publish')

@admin.register(Comment)  #permet d'ajouter dans le site d'admin de django
class Comments(admin.ModelAdmin):
    list_display = ['username','email','created']