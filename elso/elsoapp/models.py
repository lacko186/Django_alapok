from django.db import models

class Felhasznalok(models.Model):
    felhasznalonev = models.CharField(max_length=100, unique=True, verbose_name="Felhasználónév")
    emailcim = models.EmailField(unique=True, verbose_name="Email cím")
    jelszo = models.CharField(unique=True, verbose_name="Jelszó", max_length=100)
    keszult = models.DateTimeField(auto_now_add=True, verbose_name="Készült")

    def __str__(self):
        return self.felhasznalonev
    
