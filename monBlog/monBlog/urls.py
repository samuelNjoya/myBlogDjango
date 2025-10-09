from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # appel de l'url de notre application blog

    path('accounts/', include('accounts.urls')),  # URLs de l'app accounts
    # URLs d'authentification intégrées de Django
    path('accounts/', include('django.contrib.auth.urls')), #peut être pour l'authentification intégré de django
]
