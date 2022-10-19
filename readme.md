# Pour lancer ce projet

### Creer un environement virtuel et l'activer
- Pour Mac:
```bash
python3 -m venv venv 
source venv/bin/activate
```

- Pour windows:
```bash
py -m venv venv
Set-ExecutionPolicy Unrestricted -Scope Process
venv/scripts/activate
```

### Installer django

```bash
pip install django
OU
pip install -r requirements.txt
```

### Effectuer les migrations et creer la base de donnees

```bash
python manage.py migrate
```

### Remplir la base de donnees avec les donnees du fichier CSV 

```bash
python manage.py populate
```

### Creer un super-utilisateur

```bash
python manage.py createsuperuser
```

### Lancer le serveur de dev

```bash
python manage.py runserver
```

# Commandes utils 

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


## Modèles avec relations 1-n

On prend comme exemple le modèle suivant :
- Destination (id, ville).
- Voyage (id, destination_id, prix) en relation n-1 avec Destination.
- Voyageur (id, nom) en relation n-n avec Voyage à travers Participation (voyageur_id, voyage_id, nombre_valises).

### Relation 1-n :

On utilise un champ avec le type ForeignKey et la classe en argument.
exemple en reprenant les tables ci-dessus :

``` python 
from django.db.models import Model

class Destination(models.Model):
    ville = models.CharField(max_length = 10)
class Voyage(Model):
    destination = models.ForeignKey(Destination)
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

### Workflow

Lorsqu'une qu'une requête est effectuée sur le browser celle-ci est transformée en objet Python. Django cherche ensuite dans les ``settings`` du projet la variable `ROOT_URLCONF` et le chamin vers l'emplacement des urls.

Si ce chemin est renseigné (la configuration de base est ``nom_du_projet.urls``) django va vérifier s'il existe une variable `urlpatterns` (liste) dans ce fichier.

(Si vous avez utilisé la méthode `include()`, partez du principe que la variable `urlpatterns` du fichier inclu étend la variable urlpatterns initial)

Au sein de cette variablem, Django parcourt chaque motif d’URL dans l’ordre et s’arrête dès la première correspondance de `path_info` (le premier paramètre, string) avec l’URL demandée.

Une fois qu’un des motifs d’URL correspond, Django importe et appel la vue correspondante, qui est une fonction Python (le second parametre de l'objet `path`). La fonction est appelée et Django lui passe l'argument `request`.

#### Example: 

```python
from django.urls import path

from .views import home

urlpatterns = [
    path('', home)
]
```

Si nous raffraichissons la homepage de notre application (page cotnenant uniquement le nom de domaine). Django va voir que le premier élément de de urlpatterns match avec la requete. De là il va appeller la fonction `home` et lui passer le paramètre `request`.


Il est egalement possible de faire passer d'autres paramètres nommés.

#### Example:

```python
from django.urls import include, path

urlpatterns = [ 
    path('detail/<int:pk>/', detail),
]
```

Ici, la fonction `detail` sera appelée avec le paramètre `request`. De plus, un paramètre `pk` sera envoyé à la vue. `pk` devra être un integer.

### Les types de paramètre pouvant être passés à la vue:

- str - correspond à n’importe quelle chaîne non vide, à l’exception du séparateur de chemin, '/'. C’est ce qui est utilisé par défaut si aucun convertisseur n’est indiqué dans l’expression.

- int - correspond à zéro ou un autre nombre entier positif. Renvoie le type int.
slug - correspond à toute chaîne composée de lettres ou chiffres ASCII, du trait d’union ou du caractère soulignement. Par exemple, construire-votre-1er-site-django.

- uuid - correspond à un identifiant UUID. Pour empêcher plusieurs URL de correspondre à une même page, les tirets doivent être inclus et les lettres doivent être en minuscules. Par exemple, 075194d3-6885-417e-a8a8-6c931e272f00. Renvoie une instance UUID.

- path - correspond à n’importe quelle chaîne non vide, y compris le séparateur de chemin, '/'. Cela permet de correspondre à un chemin d’URL complet au lieu d’un segment de chemin d’URL comme avec str.

# Les Vues 

[POUR EN APPRENDRE PLUS](https://docs.djangoproject.com/fr/4.1/topics/http/views/)

Une fonction de vue, ou vue pour faire simple, est une fonction Python acceptant une requête web et renvoyant une réponse web. Cette réponse peut contenir le contenu HTML d’une page web, une redirection, une erreur 404, un document XML, une image… ou vraiment n’importe quoi d’autre. La vue elle-même contient la logique nécessaire pour renvoyer une réponse. Ce code peut se trouver à l’emplacement de votre choix, pour autant qu’il soit dans le chemin Python. Il n’y a pas d’autres exigences, pas de « magie » comme on dit. Mais comme il faut bien mettre ce code quelque part, la convention est de placer les vues dans un fichier nommé views.py se trouvant dans un projet ou un répertoire d’application.

```python
from django.http import HttpResponse 
import datetime 

def current_datetime(request): 
    now = datetime.datetime.now() 
    html = "<html><body>It is now %s.</body></html>" % now 
    return HttpResponse(html)
```

### Quelques méthodes utiles pour les vues:

#### render()

`render(request, template_name, context=None, content_type=None, status=None, using=None)`

Combine un gabarit donné avec un dictionnaire contexte donné et renvoie un objet HttpResponse avec le texte résultant.

Paramètres obligatoires

- request
L’objet requête utilisé pour générer la réponse.
template_name
Le nom complet d’un gabarit à utiliser ou une liste de noms de gabarits. Si une liste est donnée, le premier gabarit de la liste qui est trouvé sera utilisé. Consultez la documentation du chargement de gabarits pour plus d’informations sur la façon dont les gabarits sont recherchés.

- Paramètres facultatifs

context
Un dictionnaire de valeurs à ajouter un contexte du gabarit. Par défaut, ce dictionnaire est vide. Si une des valeurs du dictionnaire est exécutable, la vue l’appellera immédiatement avant de faire le rendu du gabarit.

#### Exemple:

```python
from django.shortcuts import render

def home(request):
    cars = Vehicle.objects.all()
    context = {'cars': cars}
    return render(request, 'home.html', context)
```

#### redirect()

`redirect()`

Renvoie une réponse HttpResponseRedirect à l’URL correspondant aux paramètres transmis.

```python
from django.shortcuts import redirect

def detail(request, pk):
    return redirect('home')
```

# Les formulaires

[POUR EN APPRENDRE PLUS 1](https://docs.djangoproject.com/fr/4.1/topics/forms/)
[POUR EN APPRENDRE PLUS 2](https://docs.djangoproject.com/fr/4.1/topics/forms/modelforms/)

### Les formulaires standards

```python
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
```

Cela définit une classe Form comportant un seul champ (your_name). Nous avons attribué une étiquette conviviale à ce champ ; celle-ci apparaîtra dans la balise `<label>` au moment de l’affichage (bien que dans ce cas, le contenu indiqué dans label est en réalité identique à celui qui aurait été généré automatiquement si nous n’avions rien fait).


La longueur maximale du champ est définie par max_length. Cela fait deux choses : la balise HTML `<input>  `reçoit l’attribut `maxlength="100"` (afin que le navigateur empêche lui-même la saisie d’un plus grand nombre de caractères), et ultérieurement lorsque Django reçoit en retour les données de formulaire, il valide que les données respectent cette longueur.

Une instance de Form possède une méthode `is_valid()` qui procède aux routines de validation pour tous ses champs. Lorsque la méthode est appelée et que tous les champs contiennent des données valables, celle-ci :

- renvoie True;
- insère les données du formulaire dans l’attribut cleaned_data.

Le formulaire complet, lorsqu’il est affiché pour la première fois, ressemble à ceci :

```html
<label for="your_name">Your name: </label> 
<input id="your_name" type="text" name="your_name" maxlength="100" required>
```

Notez qu’il n’inclut pas les balises `<form>` ni de bouton d’envoi. Ces éléments doivent être ajoutés par celui qui rédige le gabarit.

### Les formulaires basées sur un modèle

Si vous construisez une application basée sur une base de données, il y a des chances pour que vos formulaires correspondent étroitement avec les modèles Django. Par exemple, vous pourriez avoir un modèle BlogComment et vouloir créer un formulaire permettant d’envoyer des commentaires. Dans ce cas, il serait redondant de devoir définir les types de champs du formulaire, car vous avez déjà défini des champs au niveau du modèle.

C’est pour cette raison que Django fournit une classe utilitaire permettant de créer une classe de formulaire Form à partir d’un modèle Django.

#### Exemple :

```python
from django import forms

from .models import Vehicle, Comment
    
class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
```

Notez l'héritage de classe. La classe VehicleForm hérite de `forms.ModelForms` et non de `froms.Form`.

Dans cette exemple nous générons automatiquement les champs de formulaire pour l'ensemble des attributs du modèle Vehicle.

Le paramètre fields permet de définir les attributs du modèle que nous voulons utiliser. Dans cet exemple `'__all__'` indique que nous voulons intégrer tous les champs.


### Validation du formulaire dans la vue

#### Exemple:

```python
def create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VehicleForm()

    context = {'title': 'Create', 'form': form}
    return render(request, 'create.html', context)

```

Dans cet exemple nous avons une vue qui gère la création d'un objet `Vehicle`. La vue prévoit deux cas de figure.

- Dans le premier cas, la requête est une méthode HTML `POST` (l'utilisateur a remplis un formulaire et l'a envoyé au serveur). Les données envoyées par la requête `POST` sont dans un permier temps passées dans l'objet `VehicleForm` ce qui permet d'instancier un objet `Vehicle`. Si toutes les données correspondent aux attributs du modèle `Vehicle` le formulaire est considéré comme valide et est enregistré en base de donnée. 

- Le second cas correspond à l'envoi d'une requête `GET` par l'utilisateur. Ici, nous allons simplement passer une instance de l'objet VehicleForm dans le context.

# Les templates

[POUR EN APPRENDRE PLUS 1](https://docs.djangoproject.com/fr/4.1/topics/templates/)

Par sa nature liée au Web, Django a besoin d’un procédé agile de génération dynamique de HTML. L’approche la plus couramment utilisée est de se baser sur des gabarits. Un gabarit contient la partie statique du résultat HTML souhaité ainsi qu’une certaine syntaxe particulière définissant comment insérer le contenu dynamique.

Un gabarit Django est un document texte ou un chaîne Python, balisés à l’aide du langage de gabarit de Django. Certaines structures sont reconnues et interprétées par le moteur de gabarit. Les principales sont les variables et les balises.

Un gabarit est produit avec un contexte. Le processus de production remplace les variables par leurs valeurs qui sont cherchées dans le contexte, et il exécute les balises. Tout le reste est affiché tel quel.

La syntaxe du langage de gabarit de Django implique quatre structures.

### Variables

Une variable affiche une valeur à partir du contexte, qui est un objet de type dictionnaire faisant correspondre des clés à des valeurs.

Les variables sont entourées par ``{{`` et `}}` comme ceci :

```html
<p>My first name is {{ first_name }}. My last name is {{ last_name }}.</p>
```
Avec un contexte `{'first_name': 'John', 'last_name': 'Doe'}`, ce gabarit produit :

*My first name is John. My last name is Doe.*

La consultation de dictionnaire, d’attribut et d’indice de liste est implémentée par une notation pointée :

{{ my_dict.key }} {{ my_object.attribute }} {{ my_list.0 }}

Si le contenu d’une variable s’avère être un objet exécutable, le système de gabarit l’appelle sans paramètre et utilise son résultat à la place de l’objet exécutable.

### Balises

Les balises permettent d’appliquer une logique arbitraire dans le processus de rendu.

Cette définition est volontairement vague. Par exemple, une balise peut produire du contenu, servir de structure de contrôle telle qu’une instruction « if » ou une boucle « for », extraire du contenu d’une base de données ou même de donner accès à d’autres balises de gabarit.

Les balises sont entourées par `{%` et `%}`, comme ceci :

`{% csrf_token %}`

La plupart des balises acceptent des paramètres :

`{% url 'home' %}`

### Filtres

Les filtres transforment les valeurs de variables et les paramètres de balises.

Ils ressemblent à ceci :

`{{ django|title }}`

Avec un contexte {'django': 'the web framework for perfectionists with deadlines'}, ce gabarit produit le résultat suivant :

The Web Framework For Perfectionists With Deadlines

(Notez la capitalisation!!)

Certains filtres acceptent un paramètre :

`{{ my_date|date:"Y-m-d" }}`

Une référence des filtres intégrés est disponible tout comme des instructions pour écrire des filtres personnalisés.

### Commentaires

Les commentaires ressemblent à ceci :

`{# this won't be rendered #}`

Une balise `{% comment %} `autorise des commentaires sur plusieurs lignes.

#### Example d'une page HTML générée avec le moteur de gabarits.

```html
<div class="cars">
    <ol>
        {% for car in cars %}
        <li>
            <h3>
                <a href="{% url 'detail' car.pk %}">
                    {{ car.car_name }}</a>
            </h3>
            <p>{{ car.description }}</p>
            <a href="{% url 'delete' car.pk %}">Delete this car</a>
        </li>
        {% endfor %}
    </ol>
</div>
```