from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from .models import CrearFicha
from cap2.models import Modulo,Fase,Etapa
from formulario.models import CatForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="login")
def fichascap2(request):

    fichas = CrearFicha.objects.all()
    componentes = Modulo.objects.all()
    fases = Fase.objects.all()
    etapas = Etapa.objects.all().order_by('id')
    avances = CatForm.objects.all().order_by('title')
    total_formularios = len(CatForm.objects.values_list('title',))
    total_confirmados = len(CatForm.objects.filter(completo=True))
    porcentaje = str(int(((total_confirmados/total_formularios)*100)))

    return render(request,"cap2/fichas.html",{
                'title':'Fichas',
                'fichas':fichas,
                'componentes':componentes,
                'fases':fases,
                'etapas':etapas,
                'avances':avances,
                'completados': total_confirmados,
                'totales':total_formularios,
                'porcentaje':porcentaje,
    })