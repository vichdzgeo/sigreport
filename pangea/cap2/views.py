from django.shortcuts import render
from django.views.generic import ListView
from cap2.models import Imagen

# Create your views here.

def index(request):
    return render(request,"cap2/index.html")



class ImagenList(ListView):
    model = Imagen
