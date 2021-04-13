# -*- coding: utf-8 -*-
from django.views.generic.edit import CreateView,UpdateView,DeleteView, FormMixin
from django.contrib.admin.views.decorators import staff_member_required 
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from cap2.models import Modulo,Fase,Etapa
from .forms import FormLocalizacionC
from django.urls import reverse_lazy
from django import forms 
from .models import * 
import pandas as pd 


def regresa(key,modelo):
    for i in objetos:
        if i.title == key:
            return i.id
        


def regresa_instancia_id(key,modelo):
    objetos = modelo.objects.all()

    for i in objetos:
        if i.id == int(key):
            return i


@method_decorator(staff_member_required,name='dispatch')
class LocalizacionCreate(CreateView):
    
    model = ImagenLocalizacionC
    #form_class = FormLocalizacionC
    fields = '__all__'
    success_url = reverse_lazy('forms:fig-loc')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
 
        initial_data = {'componente':"1",'fase':"6","etapa":"6"}
        context['form']=FormLocalizacionC(initial=initial_data)
        return context
    

class LocalizacionCListView(ListView):
    model = ImagenLocalizacionC
    template_name = "formulario/imagenlocalizacionc_list.html"
    #paginate_by = 1
class LocalizacionCUpdate(UpdateView):
    model = ImagenLocalizacionC
    form_class = FormLocalizacionC
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('forms:fig-update',args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required,name='dispatch')
class EstructuraView(TemplateView):
    template_name = "formulario/fichas.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['componentes'] = Modulo.objects.all()
        context['fases'] = Fase.objects.all()
        context['etapas'] = Etapa.objects.all()
        context['avances'] = CatForm.objects.all().order_by('title')
        context['completados'] = len(CatForm.objects.filter(completo=True))
        context['totales'] = len(CatForm.objects.values_list('title',))
        context['porcentaje'] = str((context['completados']/ context['totales'])*100)
        return context

def fichascap2(request):

    componentes = Modulo.objects.all()
    fases = Fase.objects.all()
    etapas = Etapa.objects.all().order_by('id')
    avances = CatForm.objects.all().order_by('title')
    total_formularios = len(CatForm.objects.values_list('title',))
    total_confirmados = len(CatForm.objects.filter(completo=True))
    porcentaje = str(int(((total_confirmados/total_formularios)*100)))

    return render(request,"formulario/fichas.html",{
                'title':'Fichas',
                'componentes':componentes,
                'fases':fases,
                'etapas':etapas,
                'avances':avances,
                'completados': total_confirmados,
                'totales':total_formularios,
                'porcentaje':porcentaje,
    })



def regresa(key,objetos):

    for i in objetos:
        if i.id == key:
            return i



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


# def page(request,componente,fase,etapa):

#     agrega_form = ImagenLocalizacionC(
#     title = "Prueba con fidel en código",
#     componente= regresa_instancia_id(componente,Modulo),
#     fase= regresa_instancia_id(fase,Fase),
#     etapa= regresa_instancia_id(etapa,Etapa),
#     )
#     agrega_form.save()
#     #return HttpResponse(LocalizacionCreate.as_view())
#     return HttpResponse("estructura creada"+componente+", "+fase+", "+str(etapa))
