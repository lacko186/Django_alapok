# Django_alapok

```terminal

python -m venv venv

venv\Scripts\activate

pip install django 

```

<br>


```
django-admin startproject elso

cd elso 

python manage.py runserver

```


```
eredmény: 
August 29, 2025 - 08:53:09
Django version 5.2.5, using settings 'elso.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

<img src="localhost.PNG" alt="localhost">

### migrálás
```

python manage.py migrate

```

http://127.0.0.1/admin: 

<img src="admin_vegpont.PNG" alt="admin végpont">
### createsuperuser az admin felülethez
```

python manage.py createsuperuser

```

utána felhasználónév, email jelszó megadása
```terminal

Username (leave blank to use '...'): 
Email address: 
Password: 
Password (again):

```


```
python manage.py runserver

```

<img src="belepes.PNG" alt="belepes">

<b>ha jól dolgoztunk:</b>

<img src="admin_page.PNG" alt="admin oldal">