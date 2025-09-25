from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # appel de l'url de notre application blog
]
