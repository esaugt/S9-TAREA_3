from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import AutorForm
from .models import Autor
# Create your views here.

def Home(request):
    return render(request, 'index.html')

def crearAutor(request):
    if request.method == 'POST':
        print(request.POST)
        autor_form = AutorForm (request.POST)
        if autor_form .is_valid():
            autor_form.save()
            return redirect('index')
    else:
        autor_form = AutorForm()
    return render (request,'libro/crear_autor.html',{'autor_form':autor_form})
