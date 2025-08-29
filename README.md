# Django_alapok

```bash

python -m venv venv

venv\Scripts\activate

pip install django 

```

<br>


```bash

django-admin startproject elso

cd elso 

python manage.py runserver

```


```bash 

eredmény: 
August 29, 2025 - 08:53:09
Django version 5.2.5, using settings 'elso.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

```

<img src="localhost.PNG" alt="localhost">

<h3> Migrálás </h3>

```bash

python manage.py migrate

```

http://127.0.0.1/admin: 

<img src="admin_vegpont.PNG" alt="admin végpont">

<h3>createsuperuser az admin felülethez</h3>

```bash

python manage.py createsuperuser

```

utána felhasználónév, email jelszó megadása

```bash

Username (leave blank to use '...'): 
Email address: 
Password: 
Password (again):

```


```bash

python manage.py runserver

```

<img src="belepes.PNG" alt="belepes">

<b>Ha jól dolgoztunk:</b>

<img src="admin_page.PNG" alt="admin oldal">


```bash

 python manage.py startapp elsoapp

```

belelépek az elsoapp mappába és itt a models.py-ban megírom az első modelt

<img src="elso_model.PNG" alt="első model">

```python

from django.db import models

class Felhasznalok(models.Model):
    felhasznalonev = models.CharField(max_length=100, unique=True, verbose_name="Felhasználónév")
    emailcim = models.EmailField(unique=True, verbose_name="Email cím")
    jelszo = models.CharField(unique=True, verbose_name="Jelszó", max_length=100)
    keszult = models.DateTimeField(auto_now_add=True, verbose_name="Készült")

    def __str__(self):
        return self.felhasznalonev
    

```
migráláshoz elsoapp hozzáadás settings.py-ban:

<img src="hozzaad.PNG" alt="hozzáadás">

admin.py-ban hozzáadjuk a felhasználók modelt:

<img scr="adminhozzaad.PNG" alt="felhasználók hozzáadása">


```python

from .models import Felhasznalok

admin.site.register(Felhasznalok)

```

Migrálás: 

```bash

python manage.py makemigrations elsoapp

python manage.py migrate elsoapp

python manage.py runserver


```

<h3>Ha jól dolgoztunk:</h3>

<img src="fhozzaad.PNG" alt="felhasznalok hozzaadasa admin panel">
<img src="ujfelhasznalo.PNG" alt="új felhasználó">
<b>mentés után</b>
<img src="sikeres.PNG" alt="sikeres regisztráció">
<b>Rákattintva tudjuk szerkeszteni</b>
<img src="edit.PNG" alt="szerkesztes">