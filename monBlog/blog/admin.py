from django.contrib import admin
from .models import Post, Comment, Category

# importer mon model pour que ça s'affiche dans admin de django
# admin.site.register(post)

admin.site.register(Category)

@admin.register(Post) #permet d'ajouter dans le site d'admin de django
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','body','author','status','created','publish')
    prepopulated_fields = {'slug':('title',)} # pour que le slog se remplis automatiquement en fonction du titre
    search_fields = ('title','body')
    ordering = ('title','author')
    list_filter = ('title','author','publish')

@admin.register(Comment)  #permet d'ajouter dans le site d'admin de django
class Comments(admin.ModelAdmin):
    list_display = ['created'] # information de la table Comments(class)