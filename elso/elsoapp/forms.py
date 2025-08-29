from django import forms
from .models import Felhasznalok

class FelhasznaloForm(forms.ModelForm):
    class Meta:
        model = Felhasznalok
        fields = '__all__'
