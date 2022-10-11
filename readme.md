# Initialisation 

### Créer et accéder au projet
```bash
mkdir project_name
cd project_name
```

### Créer un environnement virtuel 
```bash
python3 -m venv venv
```

### Activer l'environnement virtuel
```bash
source venv/bin/activate
```

### Désactiver l'environnement virtuel
```bash
deactivate
```

### Installer la dernière version de Django
```bash
pip install django
```

### Créer un nouveau projet Django
```bash
django-admin startproject <nom> .
```

### Créer une app Django dans un projet
```bash
python manage.py startapp <nom>
```

### Lancer le serveur de développement
```bash
python manage.py runserver
```

### Accéder au shell Django
```bash
python manage.py shell
```

### Créer le code SQL pour effectuer des migrations
```bash
python manage.py makemigrations
```

### Exécuter le code SQL pour effectuer des migrations
```bash
python manage.py migrate
```

### Créer un super-utilisateur
```bash
python manage.py createsuperuser
```


# Les modeles #

[POUR EN APPRENDRE PLUS](https://docs.djangoproject.com/fr/4.1/topics/db/models/)

## Les différents champs de modèles Django ##

- AutoField              → incrémente automatiquement sa valeur
- BinaryField            → stocke des données binaires brutes en octets (bytes)
- BooleanField           → un champ True / False
- CharField              → un champ pour une chaine de caractères assez courte
- TextField              → pour du texte long
- CommaSeparatedIntegerField → entiers séparés par un virgule
- EmailField             → vérifie une valeur d'adresse valide
- SlugField              → format slug (alphanumérique + tirets)
- URLField               → format URL
- DateField              → une date, instance de datetime.date en python
- DateTimeField          → une date et une heure, instance python de datetime.datetime
- DecimalField           → un nombre décimal de taille fixe, instance python de Decimal
- FileField              → un champ de fichier à téléverser (paramètre upload_to est obligatoire)
- ImageField             → idem que FileField mais vérifie qu'il s'agit d'une image
- FilePathField          → un path de fichier (paramètre path est obligatoire)
- FloatField             → une instance de float en python
- GenericIPAddressField  → une adresse ip valide IPV4 / IPV6
- IPAddressField         → une adresse ip textuel type 192.168.0.1
- IntegerField           → valeurs comprises entre -2147483648 à 2147483647 
- BigIntegerField        → Un entier 64 bits
- PositiveIntegerField   → valeurs comprises entre 0 et 2147483647 
- PositiveSmallIntegerField → valeurs comprises entre 0 et 32767
- SmallIntegerField      → valeurs comprises entre -32768 et 32767 
- NullBooleanField       → un champ booléen qui accepte le Null
- TimeField              → format heure instance de datetime.time

## Les differents champs de modeles --- avec relations ---

- ForeignKey       → relation plusieurs-à-un
- ManyToManyField  → relation plusieurs-à-plusieurs 
- OneToOneField    → relation un-à-un 

## Differents paramètres des champs de modeles

- db_column         → nom de la colonne dans la base de données
- db_index          → créer un index pour la colonne
- default           → la valeur par défaut du champ
- editable          → Si False le champ n'est pas éditable dans admin
- help_text         → texte d'aide affiché dans le formulaire
- primary_key       → si True devient la clé primaire
- unique            → si True impossible d'avoir des doublons de valeur
- verbose_name      → un nom plus explicite
- validators        → une liste de validateurs à exécuter


- primary_key       → renseigner la clé primaire
- blank             → autoriser la soumission d'un champ vide
- null              → autoriser d'enregistrer en base une valeur nulle 
- unique_for_date   → unique pour une date 
- unique_for_month  → unique pour un mois 
- unique_for_year   → unique pour un an 
- choices           → choix possibles 


## Quelques méthodes du manager (non exhaustif) 

#### Chercher un objet spécifique
    .get()

#### Chercher de multiples objets
    .filter()

#### Chercher de multiples objets en excluant une catégorie
    .exclude()

#### Exécuter sa propre query SQL
    .raw()


## Quelques méthodes pour QuerySet

#### Longueur du QuerySet
    .count()

#### Inverse le QuerySet
    .reverse()

#### Transformer les valeurs du QuerySet en dictionnaire
    .values()

#### Transformer les valeurs du QuerySet en liste
    .values_list()

#### Trier le QuerySet
    .order_by() 


## Méthodes de recherche ##

Toujours précédé de __ (ex: name__contains="James")
Les méthodes ixxx font abstraction des majuscules/minuscules

- exact  		→ Recherche correspond exactement
- iexact
- contains  		→ Recherche contiens
- icontains
- gt  		→ > que (greater)
- gte  		→ >=
- lt  		→ < a   (less)
- lte  		→ <= a
- startswith  	→ Commence par
- istartswith
- endswith  		→ Fini par
- iendswith
- range  		→ check if x < query < x
- isnull  		→ check if True/False
- regex  		→ ex: Entry.objects.get(title__regex=r'^(An?|The) +')
- iregex

# Les URLS 

[POUR EN APPRENDRE PLUS](https://docs.djangoproject.com/fr/4.1/topics/http/urls/)

# Les Vues 

[POUR EN APPRENDRE PLUS](https://docs.djangoproject.com/fr/4.1/topics/http/views/)
