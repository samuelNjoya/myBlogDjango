from django.shortcuts import render,get_object_or_404
from .models import Comment,post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views import generic
from .forms import commentform  # Import the comment form

# def post_list(request):
#     posts = post.objects.all()
#     # print(posts)
#     return render(request, 'blog/post/list.html' ,{'posts':posts}) #ajouter un dictionnaire facultatif , {} apres le name

def post_list(request):
    posts = post.objects.all().order_by('-created')  # Remplace 'date_publication' par le champ approprié
    paginator = Paginator(posts, 3)  # 3 posts par page, ajuste selon tes besoins

    page = request.GET.get('page')
    try:
        posts_paginated = paginator.page(page)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, afficher la première page
        posts_paginated = paginator.page(1)
    except EmptyPage:
        # Si la page est vide (trop grande), afficher la dernière page
        posts_paginated = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'posts': posts_paginated})

def post_detail(request, slug:str):
    # try:
    #     post_dt  = post.objects.get(slug=slug)
    # except post.DoesNotExist:
    #     raise('this post doesn\'t exist' )
    post_dt = get_object_or_404(post, slug=slug)
    comments = Comment.objects.all( )
    new_comment = None
    if request.method == 'POST':
        comment_form = commentform(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False) # on enregistre pas encore
            new_comment.post = post_dt #on assossie le commentaire au post 'comment_form': comment_form,
            new_comment.save() #on enregistre
    else:
        comment_form = commentform()
        
    return render(request, 'blog/post/detail.html',{'post':post_dt, 'comments': comments,  'new_comment': new_comment})
    return render(request, 'blog/post/detail.html',{'post':post_dt})