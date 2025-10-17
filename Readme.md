
username tom:tom12345 sam:azerty123

monenv\Scripts\activate

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

python manage.py startapp accounts

python manage.py createsuperuser

pip install psycopg2-binary //pour que l'import de django marche

# Créer un dump de toutes les données
python manage.py dumpdata --indent=2 > alldata.json

# Ou exporter app par app (plus propre)
python manage.py dumpdata auth --indent=2 > auth.json
python manage.py dumpdata blog --indent=2 > blog.json
python manage.py dumpdata accounts --indent=2 > accounts.json

# super 
python manage.py dumpdata blog --output=blog/fixtures/blog.json --indent=2
python manage.py dumpdata auth --output=accounts/fixtures/accounts.json --indent=2   //python manage.py loaddata accounts.json
python manage.py dumpdata blog --indent=2 > blog.json  //python manage.py loaddata blog.json

vector permet de faire des recherches sur plusieurs champs de la bd

fitre avancer 
ajouter des pub a parti du blog
associer un utilisateur a un commentaire
Système de commentaires en temps réel

# Prochaines améliorations possibles :
    Upload d'images pour les articles
    Système de tags
    Recherche avancée
    Éditeur WYSIWYG
    Système de likes/partages

<!-- Au lieu de : -->
<a href="{% url 'post_detail' post.slug %}">{{ post.title }}</a>

<!-- Vous pouvez faire : -->
<a href="{{ post.get_absolute_url }}">{{ post.title }}</a>