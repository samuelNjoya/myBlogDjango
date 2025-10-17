from django.urls import path
from . import views

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    # path('category/<slug:category>/', views.post_list, name='category_post_list'),
    # path('<slug>/', views.post_detail, name='post_detail'),

    #  # NOUVELLES URLs
    # path('post/new/', views.post_create, name='post_create'),
    # path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    # path('drafts/', views.post_draft_list, name='post_draft_list'),

      # URLs existantes
    path('', views.post_list, name='post_list'),
    path('category/<slug:category>/', views.post_list, name='category_post_list'),
    # NOUVELLES URLs - Spécifiques en premier
    path('post/new/', views.post_create, name='post_create'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    # URL générique en dernier
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
