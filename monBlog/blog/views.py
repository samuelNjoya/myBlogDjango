from django.shortcuts import render,get_object_or_404,redirect
from .models import Comment,post,Category
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views import generic
from .forms import commentform  # Import the comment form
from django.contrib import messages

# def post_list(request):
#     posts = post.objects.all()
#     # print(posts)
#     return render(request, 'blog/post/list.html' ,{'posts':posts}) #ajouter un dictionnaire facultatif , {} apres le name

def post_list(request,category=None):
    posts = post.published.all().order_by('-created')  #objects a été remplacer par published provenant du model
    categories = Category.objects.all()
    if category:
        category = get_object_or_404(Category, slug=category)
        posts = posts.filter(category=category)
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

    context = {
            'posts': posts_paginated,
            'page': page,
            'categories': categories,
            'category': category
        }

    return render(request, 'blog/post/list.html', context)

def post_detail(request, slug:str):
    # try:
    #     post_dt  = post.objects.get(slug=slug)
    # except post.DoesNotExist:
    #     raise('this post doesn\'t exist' )
    post_dt = get_object_or_404(post, slug=slug)
    comments = Comment.objects.filter(post=post_dt).order_by('created') #pour filtrer les commentaires par post
    new_comment = None
    if request.method == 'POST':
        comment_form = commentform(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False) # on enregistre pas encore
            new_comment.post = post_dt #on assossie le commentaire au post 'comment_form': comment_form,
            new_comment.save() #on enregistre
            messages.success(request, 'Your comment has been added.')
            return redirect('post_detail', slug=slug) #rediriger pour eviter la soumission lors de l'actualisation
    else:
        comment_form = commentform()
        
    return render(request, 'blog/post/detail.html',{
                                                    'post':post_dt, 
                                                    'comments': comments, 
                                                   # 'new_comment': new_comment,
                                                    'comment_form':comment_form
                                                    })
    return render(request, 'blog/post/detail.html',{'post':post_dt})