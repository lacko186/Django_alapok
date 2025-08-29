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