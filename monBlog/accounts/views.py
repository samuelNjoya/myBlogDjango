from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        #TAPE 2 : Créer le formulaire avec les données envoyées
        form = UserCreationForm(request.POST)
         # ÉTAPE 3 : Valider le formulaire
        if form.is_valid():
            user = form.save()
          #  login(request, user)  # Connecte automatiquement l'utilisateur 
            messages.success(request, 'Inscription réussie !')
            #return redirect('post_list') #route pour les posts
            return redirect('login')
    else:
         # Créer un formulaire vide pour l'affichage initial
        form = UserCreationForm()
    # ÉTAPE 8 : Afficher le template d'inscription avec le formulaire
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')