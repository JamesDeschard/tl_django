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

## Création du modèle

Par défaut, Django utilise une base sqlite (mais on peut changer dans DATABASES dans le fichier settings.py).

Le principe est de créer une classe par table de la base de données :
- cette classe est rajoutée dans le fichier models.py.
- cette classe doit dériver de django.db.models.Model et définit tous les champs.

### Modèle en l'absence de relations

Exemple de modèle défini dans models.py :
```python 
from django.db import models
class MyObject(models.Model):
    label = models.CharField('Nom', max_length = 5)
    description = models.CharField('Description', max_length = 100)
```
  
label et description sont les noms des champs qu'on va utiliser dans le code, et aussi les noms des colonnes dans la base. Les champs on un type dérivé de la classe Field (CharField, DateField, etc ...). Nom et Description sont les noms.

Voir la partie migration pour la création des tables dans la base.

Par défaut, chaque modèle définit un champ id qui s'autoincrémente, c'est à dire qu'il définit implicitement un champ : id = models.AutoField(primary_key=True). Si on définit explicitement un champ comme étant une clef primaire (avec l'argument primary_key = True), ce champ id par défaut n'est plus présent.

Types de champs avec arguments (ces arguments s'appliquent souvent à beaucoup types de champs, pas seulement à celui utilisé ici) :
- models.BooleanField() : champ booléen.
- models.IntegerField() : champ entier.
- models.DecimalField(max_digits = 10, decimal_places = 3) : champ décimal indiquant le nombre de chiffres total et après la virgule.
- models.FloatField() : champ float.
- models.CharField(max_length = 10) : champ chaîne de caractères.
- models.DateField() : champ date.
- models.DateTimeField(auto_now_add = True) : champ date + temps rempli à la création (type date de création).
- models.DateTimeField(auto_now = True) : champ date + temps rempli à la création et à chaque mise à jour (type dernière date de modification).
- models.EmailField(help_text = 'Votre mail') : champ de type mail.
- models.BinaryField(null = True) : champ pour stocker des données binaire (type blob).
- models.FileField(null = True) : champ pour stocker un fichier.
- models.FilePathField(null= True) : champ pour stocker le chemin d'un fichier.

Arguments que l'on peut passer en plus :

- en premier argument, on peut donner un nom au champ : myField = models.CharField('Mon nom', max_length = 10).
- db_column = 'monNom' : le nom de la colonne à utiliser dans la base, à la place du nom du champ.
- null = True : le champ peut être nul (par défaut, False).
- blank = True : le champ peut rester non rempli dans le formulaire (par défaut, False).
- default = 0 : valeur par défaut, si le champ n'est pas rempli.
- max_length = 10 : la longueur maximum du champ.
- choices = (('FR', 'France'), ('US', 'Etats-Unis')) : les possibilités de valeurs de ce champ, avec à la fois les valeurs dans la base et les valeurs affichées (comme select html).
- primary_key = True
- unique = True : le champ doit avoir une contrainte d'unicité dans la base.
- db_index = True : créer un index pour ce champ dans la base.
- help_text = 'numero de telephone' : commentaire sur le champ.

## Création d'un objet :

- création de l'objet : myObject = MyObject(); myObject.field1 = 'abc'; myObject.field2 = 123;
- sauvegarde dans la base : myObject.save()

Duplication d'un objet existant : on lève l'objet et on met sa clef primaire à None :

``` python
myObj = MyModel.objects.get(id = 5)
myObj.pk = None
myObj.save()
```
  
attention : par défaut, ça fait un delete cascade !

Méthodes à rajouter aux classes modèles :
rajouter une méthode __str__, si on veut renvoyer une représentation de l'objet, ce qui est quasi-indispensable.


## Modèles avec relations 1-n ou n-n

On prend comme exemple le modèle suivant :
- Destination (id, ville).
- Voyage (id, destination_id, prix) en relation n-1 avec Destination.
- Voyageur (id, nom) en relation n-n avec Voyage à travers Participation (voyageur_id, voyage_id, nombre_valises).

### Relation 1-n :

On utilise un champ avec le type ForeignKey et la classe en argument.
exemple en reprenant les tables ci-dessus :

``` python 
from django.db.models import Model, CharField, FloatField, ForeignKey
class Destination(Model):
    ville = CharField(max_length = 10)
class Voyage(Model):
    destination = ForeignKey(Destination)
    prix = FloatField()
```

pour créer un objet, on peut faire :

```python
dest = Destination.objects.get(ville = 'Paris')
voyage = Voyage(destination = dest, prix = 100)
voyage.save()
```
    
    
### Migrations

Migrations quand on crée ou on change le modèle :

- l'application doit avoir été rajoutée dans le settings.py, dans la liste INSTALLED_APPS : 'myApp.apps.MyAppConfig' (à quoi sert MyAppConfig ?)
- manage.py makemigrations myApp : crée un fichier python de migration dans le directory migrations de l'application : à faire à chaque changement du modèle (ou à sa création)
- manage.py sqlmigrate myApp 0003 : affiche le sql correspondant à la 3ème migration de l'application myApp.
- manage.py migrate myApp : applique toutes les migrations qui ne l'ont pas encore été (suivi dans la table). Django suit les migrations effectuées dans la table django_migrations.

en routine, on utilise donc makemigrations, puis migrate.
les tables sont préfixées par le nom de l'application puis '_'
Pour créer un objet dans la base à la main :

démarrer un shell avec `manage.py shell`
faire dedans : `from myApp.models import *`
puis `obj = MyModel(); obj.prop1 = value1, obj.prop2 = value2; ...`
puis `obj.save()`
on peut aussi faire :` MyModel(prop1 = value1, prop2 = value2, ...).save()`


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
