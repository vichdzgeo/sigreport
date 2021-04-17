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
from .forms import *
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


### Descipcion general 
@method_decorator(staff_member_required,name='dispatch')
class DescripcionGeneralListView(ListView):
    model = DescripcionGeneral
    template_name = "formulario/descripciongeneral_list.html"
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=DescripcionGeneral._meta.verbose_name
        
        return context


class DescripcionGeneralCreate(CreateView):
    
    model = DescripcionGeneral
    #form_class = FormLocalizacionC
    fields = '__all__'
    #success_url = reverse_lazy('forms:actividad-create')
    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=DescripcionGeneral._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=DescripcionGeneralForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        return  reverse_lazy('forms:generales',args=[this_id]) + '?ok'




###### FRECUENCIA DE ACTIVIDADES


    
@method_decorator(staff_member_required,name='dispatch')
class FrecuenciaActividadesCListView(ListView):
    model = FrecuenciaActividadesC
    template_name = "formulario/frecuenciaactividadesc_list.html"
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=FrecuenciaActividadesC._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        
        return context

@method_decorator(staff_member_required,name='dispatch')
class FrecuenciaActividadesCCreate(CreateView):
    
    model = FrecuenciaActividadesC
    #form_class = FormLocalizacionC
    fields = '__all__'
    #success_url = reverse_lazy('forms:actividad-create')
    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=FrecuenciaActividadesC._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=FrecuenciaActividadesCForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        return  reverse_lazy('forms:actividades',args=[this_id]) + '?ok'


@method_decorator(staff_member_required,name='dispatch')
class FrecuenciaActividadesCUpdate(UpdateView):
    model = FrecuenciaActividadesC
    form_class = FrecuenciaActividadesCForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('forms:actividad-update',args=[self.object.id]) + '?ok'




#### LOCALIZACION

@method_decorator(staff_member_required,name='dispatch')
class LocalizacionCreate(CreateView):
    
    model = ImagenLocalizacionC
    #form_class = FormLocalizacionC
    fields = '__all__'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=FormLocalizacionC(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        return  reverse_lazy('forms:localizacion',args=[this_id]) + '?ok'


@method_decorator(staff_member_required,name='dispatch')
class LocalizacionCListView(ListView):
    model = ImagenLocalizacionC
    template_name = "formulario/imagenlocalizacionc_list.html"
    #paginate_by = 1

@method_decorator(staff_member_required,name='dispatch')
class LocalizacionCUpdate(UpdateView):
    model = ImagenLocalizacionC
    form_class = FormLocalizacionC
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('forms:fig-update',args=[self.object.id]) + '?ok'

class CatFormUpdate(UpdateView):
    model = CatForm
    form_class = FormCatForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        
        context['p_title']="Formulario completo"
        context['p_subtitle']=id_form.componente.title+" - "+id_form.fase.title+" - "+ id_form.etapa.title
        if id_form.completo is True:
            context['txt_actualizacion']="estatus del formualario: completo"
        else:
            context['txt_actualizacion']="estatus del formualario: pendiente"
        return context

    def get_success_url(self):
        return reverse_lazy('forms:completo',args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required,name='dispatch')
class EstructuraView(TemplateView):
    template_name = "formulario/fichas.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['componentes'] = Modulo.objects.all()
        context['fases'] = Fase.objects.all().order_by('title')
        context['etapas'] = Etapa.objects.all().order_by('id').reverse()
        context['avances'] = CatForm.objects.all().order_by('title')
        context['completados'] = len(CatForm.objects.filter(completo=True))
        context['totales'] = len(CatForm.objects.values_list('title',))
        context['porcentaje'] = str((context['completados']/ context['totales'])*100)
        return context



def regresa(key,objetos):

    for i in objetos:
        if i.title == key:
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
                    tag_url = str(row['tag-url'])
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
                            nurl = tag_url,
                                            )
                        agrega_form.save()
                
                elif row['tipo_c']== 2 and componente_i.t_base == True and componente_i.t_aprov_edificable == True:  
                    nombre_f = row['nombre'] #0
                    tipo_f = str(row['tipo']) #1
                    tipoc_f = str(row['tipo_c']) #2
                    componente_f =componente_i  #3
                    fase_f =regresa(row['fase'],l_fases) #4
                    etapa_f = etapa_i  # 5
                    tag_url = str(row['tag-url'])
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
                            nurl = tag_url,
                                            )
                        agrega_form.save()

                elif row['tipo_c']== 3 and componente_i.t_base == True and componente_i.t_obras == True:  
                    nombre_f = row['nombre'] #0
                    tipo_f = str(row['tipo']) #1
                    tipoc_f = str(row['tipo_c']) #2
                    componente_f =componente_i  #3
                    fase_f =regresa(row['fase'],l_fases) #4
                    etapa_f = etapa_i  # 5
                    tag_url = str(row['tag-url'])
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
                            nurl = tag_url,
                                            )
                        agrega_form.save()

                elif row['tipo_c']== 4 and componente_i.t_base == True and componente_i.t_areas_verdes == True:  
                    nombre_f = row['nombre'] #0
                    tipo_f = str(row['tipo']) #1
                    tipoc_f = str(row['tipo_c']) #2
                    componente_f =componente_i  #3
                    fase_f =regresa(row['fase'],l_fases) #4
                    etapa_f = etapa_i  # 5
                    tag_url = str(row['tag-url'])
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
                            nurl = tag_url,
                                            )
                        agrega_form.save()

                elif row['tipo_c']== 5 and componente_i.t_base == True and componente_i.t_aprov_lineal == True:  
                    nombre_f = row['nombre'] #0
                    tipo_f = str(row['tipo']) #1
                    tipoc_f = str(row['tipo_c']) #2
                    componente_f =componente_i  #3
                    fase_f =regresa(row['fase'],l_fases) #4
                    etapa_f = etapa_i  # 5
                    tag_url = str(row['tag-url'])
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
                            nurl = tag_url,
                                            )
                        agrega_form.save()
            
            
    return HttpResponse("estructura creada")

# Create your views here.


