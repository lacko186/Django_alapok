from django.shortcuts import render
from .forms import FelhasznaloForm
from .models import Felhasznalok

def index(request):
    if request.method == 'POST':
        form = FelhasznaloForm(request.POST)
        if form.is_valid():
            form.save()
            form = FelhasznaloForm()  
    else:
        form = FelhasznaloForm()
    
    felhasznalok = Felhasznalok.objects.all()
    return render(request, 'index.html', {'form': form, 'felhasznalok': felhasznalok})

