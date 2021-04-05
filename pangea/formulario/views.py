from django.shortcuts import render, HttpResponse, redirect
from cap2.models import Modulo,Fase,Etapa
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import * 
import pandas as pd 
from .forms import FormLocalizacionC

class LocalizacionListView(ListView):
    model = FormLocalizacionC

class LocalizacionDetailView(DetailView):
    model = FormLocalizacionC

class LocalizacionCreate(CreateView):
    model = ImagenLocalizacionC
    form_class = FormLocalizacionC
    

def regresa_instancia_id(key,modelo):
    objetos = modelo.objects.all()

    for i in objetos:
        if i.id == int(key):
            return i

def regresa(key,objetos):

    for i in objetos:
        if i.id == key:
            return i


def page(request,componente,fase,etapa):

    agrega_form = ImagenLocalizacionC(
    title = "Prueba con fidel en código",
    componente= regresa_instancia_id(componente,Modulo),
    fase= regresa_instancia_id(fase,Fase),
    etapa= regresa_instancia_id(etapa,Etapa),
    )
    agrega_form.save()
    #return HttpResponse(LocalizacionCreate.as_view())
    return HttpResponse("estructura creada"+componente+", "+fase+", "+str(etapa))

def agregar_estructura(request):
    
    estructura = pd.read_csv("C:/Dropbox (LANCIS)/CARPETAS_TRABAJO/vhernandez/repositorios_git/cap2/pangea/estructura_arbol_form.txt", delimiter='\t',encoding='utf-8')
    estructura.sort_values(by='nombre',ascending=False)
    l_componentes  = Modulo.objects.all()
    l_etapas = Etapa.objects.all()
    l_fases = Fase.objects.all()
    dicc_fases ={}

    
    for componente_i in l_componentes:
        for etapa_i in l_etapas:
            for index, row in estructura.iterrows():
                
                if row['tipo_c']== 1 and componente_i.t_base == True: #and componente_i.t_aprov_edificable == False and componente_i.t_obras == False and componente_i.t_areas_verdes == False and componente_i.t_aprov_lineal == False:
                    nombre_f = row['nombre'] #0
                    tipo_f = str(row['tipo']) #1
                    tipoc_f = str(row['tipo_c']) #2
                    componente_f =componente_i  #3
                    fase_f =regresa(row['fase'],l_fases) #4
                    etapa_f = etapa_i  # 5
                    existe_form = CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f)
                    print (len(existe_form))
                    if len(existe_form)==0:

                        agrega_form = CatForm(
                            title = nombre_f,
                            tipo = tipo_f,
                            tipo_c = tipoc_f,
                            componente = componente_f,
                            fase = fase_f,
                            etapa =etapa_f,
                                            )
                        agrega_form.save()
                
                elif row['tipo_c']== 2 and componente_i.t_base == True and componente_i.t_aprov_edificable == True:  
                    nombre_f = row['nombre'] #0
                    tipo_f = str(row['tipo']) #1
                    tipoc_f = str(row['tipo_c']) #2
                    componente_f =componente_i  #3
                    fase_f =regresa(row['fase'],l_fases) #4
                    etapa_f = etapa_i  # 5
                    existe_form = CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f)
                    print (len(existe_form))
                    if len(existe_form)==0:

                        agrega_form = CatForm(
                            title = nombre_f,
                            tipo = tipo_f,
                            tipo_c = tipoc_f,
                            componente = componente_f,
                            fase = fase_f,
                            etapa =etapa_f,
                                            )
                        agrega_form.save()

                elif row['tipo_c']== 3 and componente_i.t_base == True and componente_i.t_obras == True:  
                    nombre_f = row['nombre'] #0
                    tipo_f = str(row['tipo']) #1
                    tipoc_f = str(row['tipo_c']) #2
                    componente_f =componente_i  #3
                    fase_f =regresa(row['fase'],l_fases) #4
                    etapa_f = etapa_i  # 5
                    existe_form = CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f)
                    print (len(existe_form))
                    if len(existe_form)==0:

                        agrega_form = CatForm(
                            title = nombre_f,
                            tipo = tipo_f,
                            tipo_c = tipoc_f,
                            componente = componente_f,
                            fase = fase_f,
                            etapa =etapa_f,
                                            )
                        agrega_form.save()

                elif row['tipo_c']== 4 and componente_i.t_base == True and componente_i.t_areas_verdes == True:  
                    nombre_f = row['nombre'] #0
                    tipo_f = str(row['tipo']) #1
                    tipoc_f = str(row['tipo_c']) #2
                    componente_f =componente_i  #3
                    fase_f =regresa(row['fase'],l_fases) #4
                    etapa_f = etapa_i  # 5
                    existe_form = CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f)
                    print (len(existe_form))
                    if len(existe_form)==0:

                        agrega_form = CatForm(
                            title = nombre_f,
                            tipo = tipo_f,
                            tipo_c = tipoc_f,
                            componente = componente_f,
                            fase = fase_f,
                            etapa =etapa_f,
                                            )
                        agrega_form.save()

                elif row['tipo_c']== 5 and componente_i.t_base == True and componente_i.t_aprov_lineal == True:  
                    nombre_f = row['nombre'] #0
                    tipo_f = str(row['tipo']) #1
                    tipoc_f = str(row['tipo_c']) #2
                    componente_f =componente_i  #3
                    fase_f =regresa(row['fase'],l_fases) #4
                    etapa_f = etapa_i  # 5
                    existe_form = CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f)
                    print (len(existe_form))
                    if len(existe_form)==0:

                        agrega_form = CatForm(
                            title = nombre_f,
                            tipo = tipo_f,
                            tipo_c = tipoc_f,
                            componente = componente_f,
                            fase = fase_f,
                            etapa =etapa_f,
                                            )
                        agrega_form.save()
            
            
    return HttpResponse("estructura creada")

# Create your views here.


