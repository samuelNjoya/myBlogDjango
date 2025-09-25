from django.shortcuts import render,get_object_or_404
from .models import post

def post_list(request):
    posts = post.objects.all()
    # print(posts)
    return render(request, 'blog/post/list.html' ,{'posts':posts}) #ajouter un dictionnaire facultatif , {} apres le name

def post_detail(request, slug:str):
    # try:
    #     post_dt  = post.objects.get(slug=slug)
    # except post.DoesNotExist:
    #     raise('this post doesn\'t exist' )
    post_dt = get_object_or_404(post, slug=slug)
        
    return render(request, 'blog/post/detail.html',{'post':post_dt})