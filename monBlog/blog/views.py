from django.shortcuts import render,get_object_or_404,redirect
from .models import Comment,Post,Category
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views import generic
from .forms import commentform, PostForm # Import the comment form
from django.db.models import Q  # ← IMPORTANT: Pour les requêtes complexes
from django.contrib import messages
from django.contrib.auth.decorators import login_required  # ← Pour protéger les vues

# def post_list(request):
#     posts = post.objects.all()
#     # print(posts)
#     return render(request, 'blog/post/list.html' ,{'posts':posts}) #ajouter un dictionnaire facultatif , {} apres le name

def post_list(request,category=None):
    posts = Post.published.all().order_by('-created')  #objects a été remplacer par published provenant du model
    categories = Category.objects.all()

     # Gestion de la recherche
    query = request.GET.get('q')  # Récupère le terme de recherche depuis l'URL
    if query:
        # Filtre les articles contenant le terme dans le titre OU le corps
        posts = posts.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
        messages.info(request, f'Résultats pour : "{query}"')

    # filtrage par categorie si specifier
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
            'category': category,
            'search_query': query  # ← Pour pré-remplir la barre de recherche
        }

    return render(request, 'blog/post/list.html', context)

def post_detail(request, slug:str):
    # try:
    #     post_dt  = post.objects.get(slug=slug)
    # except post.DoesNotExist:
    #     raise('this post doesn\'t exist' )
    post_dt = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post_dt).order_by('created') #pour filtrer les commentaires par post
    new_comment = None
    if request.method == 'POST':
        comment_form = commentform(data=request.POST)
        if comment_form.is_valid():
          #  body = comment_form.cleaned_data['body']
            new_comment = comment_form.save(commit=False) # on enregistre pas encore
            new_comment.post = post_dt #on assossie le commentaire au post 'comment_form': comment_form,
            new_comment.author = request.user #info de l'user qui commente (nom et email)
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

@login_required
def post_create(request):
    """
    Vue pour créer un nouvel article
    Nécessite une connexion utilisateur (@login_required)
    """
    if request.method == 'POST':
        # Créer le formulaire avec les données POST
        form = PostForm(request.POST)
        if form.is_valid():
            # Sauvegarder sans commiter pour ajouter l'auteur
            new_post = form.save(commit=False)
            new_post.author = request.user  # L'auteur est l'utilisateur connecté
            new_post.save()
            
            # Message de succès adapté au statut
            if new_post.status == 'published':
                messages.success(request, '✅ Article publié avec succès !')
            else:
                messages.success(request, '📝 Brouillon sauvegardé !')
            
            return redirect(new_post)  # Redirige vers la page de l'article
    else:
        # Afficher un formulaire vide pour les requêtes GET
        form = PostForm()
    
    context = {
        'form': form,
        'title': 'Nouvel article'
    }
    return render(request, 'blog/post/form.html', context)

@login_required
def post_edit(request, slug):
    """
    Vue pour modifier un article existant
    Seul l'auteur peut modifier son article
    """
    # Récupérer l'article ou renvoyer 404
    post_obj = get_object_or_404(post, slug=slug)
    
    # Vérifier que l'utilisateur est l'auteur
    if post_obj.author != request.user:
        messages.error(request, '❌ Vous ne pouvez modifier que vos propres articles.')
        return redirect('post_list')
    
    if request.method == 'POST':
        # Modifier l'article existant avec les nouvelles données
        form = PostForm(request.POST, instance=post_obj)
        if form.is_valid():
            updated_post = form.save()
            
            # Message de succès adapté
            if updated_post.status == 'published':
                messages.success(request, '✅ Article mis à jour et publié !')
            else:
                messages.success(request, '📝 Modifications sauvegardées !')
            
            return redirect(updated_post)
    else:
        # Afficher le formulaire pré-rempli avec les données actuelles
        form = PostForm(instance=post_obj)
    
    context = {
        'form': form,
        'title': 'Modifier l\'article',
        'post': post_obj
    }
    return render(request, 'blog/post/form.html', context)

@login_required
def post_draft_list(request):
    """
    Vue affichant les brouillons de l'utilisateur connecté
    """
    drafts = Post.objects.filter(
        author=request.user, 
        status='draft'
    ).order_by('-created')
    
    context = {
        'posts': drafts,
        'title': 'Mes brouillons'
    }
    return render(request, 'blog/post/list.html', context)