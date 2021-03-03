from django.shortcuts import render
from django.views.generic import ListView
from cap2.models import Imagen

# Create your views here.

def index(request):
    return render(request,"cap2/index.html")

def formularios(request):
    return render(request,"cap2/formularios.html")

class ImagenList(ListView):
    model = Imagen

def FigurasList(request):
    figuras = Imagen.objects.all()
    return render(request,"cap2/galeria_list.html",{'figuras':figuras})