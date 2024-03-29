# -*- coding: utf-8 -*-
from django.views.generic.edit import CreateView,UpdateView,DeleteView, FormMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from cap2.models import Modulo,Fase,Etapa
from .forms import *
from django.urls import reverse_lazy
from django import forms 
from .models import * 
import pandas as pd 
from django.conf import settings
import os 
from django.http import HttpResponse
from django.shortcuts import redirect
import pypandoc
import jinja2
import codecs
import re
from jinja2 import Template
import subprocess
import time as time_old

def regresa(key,modelo):
    for i in objetos:
        if i.title == key:
            return i.id
        

def regresa_username(key,modelo):
    objetos = modelo.objects.all()

    for i in objetos:
        if i.id == int(key):
            return i.username
        else:
            return " "
    


def regresa_instancia_id(key,modelo):
    objetos = modelo.objects.all()

    for i in objetos:
        if i.id == int(key):
            return i


##### Selección de procesos constructivos 

@method_decorator(login_required,name='dispatch')
class SeleccionProcesosConstructivosCreate(CreateView):
    
    model = SeleccionProcesosConstructivos
    form_class = SeleccionProcesosConstructivosForm

    def get(self, *args, **kwargs):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        if SeleccionProcesosConstructivos.objects.filter(componente=id_form.componente.id,fase=id_form.fase.id,etapa=id_form.etapa.id):
            id_form_fig = SeleccionProcesosConstructivos.objects.filter(componente=id_form.componente.id,fase=id_form.fase.id,etapa=id_form.etapa.id)
            return redirect('forms:selecprocesos-update',id_form_fig[0].id)
        else:
            return super().get(*args, **kwargs)
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(SeleccionProcesosConstructivosCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=SeleccionProcesosConstructivos._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=SeleccionProcesosConstructivosForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        return  reverse_lazy('forms:fichas')


@method_decorator(login_required,name='dispatch')
class SeleccionProcesosConstructivosUpdate(UpdateView):
    model = SeleccionProcesosConstructivos
    form_class = SeleccionProcesosConstructivosForm
    template_name_suffix = '_update_form'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        elemento = SeleccionProcesosConstructivos.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['i']=elemento   
        context['p_componente']=elemento.componente
        context['p_fase']= elemento.fase
        context['p_etapa']= elemento.etapa
        context['avance'] = CatForm.objects.filter(title='Selección de procesos constructivos',
                                            etapa=elemento.etapa,
                                            componente=elemento.componente)[0]
        return context

    def get_success_url(self):
        return reverse_lazy('forms:fichas')




##### Selección de sistemas constructivos 

@method_decorator(login_required,name='dispatch')
class SeleccionSistemasConstructivosCreate(CreateView):
    
    model = SeleccionSistemasConstructivos
    form_class = SeleccionSistemasConstructivosForm

    def get(self, *args, **kwargs):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        if SeleccionSistemasConstructivos.objects.filter(componente=id_form.componente.id,fase=id_form.fase.id,etapa=id_form.etapa.id):
            id_form_fig = SeleccionSistemasConstructivos.objects.filter(componente=id_form.componente.id,fase=id_form.fase.id,etapa=id_form.etapa.id)
            return redirect('forms:selecsistemas-update',id_form_fig[0].id)
        else:
            return super().get(*args, **kwargs)
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(SeleccionSistemasConstructivosCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=SeleccionSistemasConstructivos._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=SeleccionSistemasConstructivosForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        return  reverse_lazy('forms:fichas')

@method_decorator(login_required,name='dispatch')
class SeleccionSistemasConstructivosListView(ListView):
    model = SeleccionSistemasConstructivos
    template_name = "formulario/seleccionsistemasconstructivos_list.html"
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=SeleccionSistemasConstructivos._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        
        return context

@method_decorator(login_required,name='dispatch')
class SeleccionSistemasConstructivosUpdate(UpdateView):
    model = SeleccionSistemasConstructivos
    form_class = SeleccionSistemasConstructivosForm
    template_name_suffix = '_update_form'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        elemento = SeleccionSistemasConstructivos.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['i']=elemento   
        context['p_componente']=elemento.componente
        context['p_fase']= elemento.fase
        context['p_etapa']= elemento.etapa
        context['avance'] = CatForm.objects.filter(title='Selección de sistemas constructivos',
                                            etapa=elemento.etapa,
                                            componente=elemento.componente)[0]
        return context

    def get_success_url(self):
        return reverse_lazy('forms:fichas')


###### Longitud de obras lineales
@method_decorator(login_required,name='dispatch')
class ObrasLinealesLongitudesListView(ListView):
    model = ObrasLinealesLongitudes
    template_name = "formulario/obraslinealeslongitudes_list.html"
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=ObrasLinealesLongitudes._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        
        return context

@method_decorator(login_required,name='dispatch')
class ObrasLinealesLongitudesCreate(CreateView):
    
    model = ObrasLinealesLongitudes
    form_class = ObrasLinealesLongitudesForm

    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(ObrasLinealesLongitudesCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=ObrasLinealesLongitudes._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=ObrasLinealesLongitudesForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        return  reverse_lazy('forms:obraslineales',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class ObrasLinealesLongitudesUpdate(UpdateView):
    model = ObrasLinealesLongitudes
    form_class = ObrasLinealesLongitudesForm
    template_name_suffix = '_update_form'
    

    def get_success_url(self):
        return reverse_lazy('forms:obraslineales-update',args=[self.object.id]) + '?ok'

###### Superficie de obras o edificaciones provisionales temporales



@method_decorator(login_required,name='dispatch')
class SuperficieObrasCListView(ListView):
    model = SuperficieObrasC
    template_name = "formulario/superficieobrasc_list.html"
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=SuperficieObrasC._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        
        return context

@method_decorator(login_required,name='dispatch')
class SuperficieObrasCCreate(CreateView):
    
    model = SuperficieObrasC
    form_class = SuperficieObrasCForm

    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(SuperficieObrasCCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=SuperficieObrasC._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=SuperficieObrasCForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        return  reverse_lazy('forms:obrastemporales',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class SuperficieObrasCUpdate(UpdateView):
    model = SuperficieObrasC
    form_class = SuperficieObrasCForm
    template_name_suffix = '_update_form'
    

    def get_success_url(self):
        return reverse_lazy('forms:obrastemporales-update',args=[self.object.id]) + '?ok'





###### Generación de aguas residuales 

    
@method_decorator(login_required,name='dispatch')
class AguasResidualesCListView(ListView):
    model = AguasResidualesC
    template_name = "formulario/aguasresidualesc_list.html"
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=AguasResidualesC._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        
        return context

@method_decorator(login_required,name='dispatch')
class AguasResidualesCCreate(CreateView):
    
    model = AguasResidualesC
    form_class = AguasResidualesCForm

    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(AguasResidualesCCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=AguasResidualesC._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=AguasResidualesCForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        return  reverse_lazy('forms:aguaresidual',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class AguasResidualesCUpdate(UpdateView):
    model = AguasResidualesC
    form_class = AguasResidualesCForm
    template_name_suffix = '_update_form'
    

    def get_success_url(self):
        return reverse_lazy('forms:aguaresidual-update',args=[self.object.id]) + '?ok'



###### Consumo de agua

    
@method_decorator(login_required,name='dispatch')
class ConsumoAguaCListView(ListView):
    model = ConsumoAguaC
    template_name = "formulario/consumoaguac_list.html"
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=ConsumoAguaC._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        
        return context

@method_decorator(login_required,name='dispatch')
class ConsumoAguaCCreate(CreateView):
    
    model = ConsumoAguaC
    form_class = ConsumoAguaCForm

    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(ConsumoAguaCCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=ConsumoAguaC._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=ConsumoAguaCForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        return  reverse_lazy('forms:consumoagua',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class ConsumoAguaCUpdate(UpdateView):
    model = ConsumoAguaC
    form_class = ConsumoAguaCForm
    template_name_suffix = '_update_form'
    

    def get_success_url(self):
        return reverse_lazy('forms:consumoagua-update',args=[self.object.id]) + '?ok'


###### Listado floristico 

    
@method_decorator(login_required,name='dispatch')
class ListadoFloristicoCListView(ListView):
    model = ListadoFloristicoC
    template_name = "formulario/listadofloristicoc_list.html"
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=ListadoFloristicoC._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        
        return context

@method_decorator(login_required,name='dispatch')
class ListadoFloristicoCCreate(CreateView):
    
    model = ListadoFloristicoC
    form_class = ListadoFloristicoCForm

    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(ListadoFloristicoCCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=ListadoFloristicoC._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=ListadoFloristicoCForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        return  reverse_lazy('forms:flor',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class ListadoFloristicoCUpdate(UpdateView):
    model = ListadoFloristicoC
    form_class = ListadoFloristicoCForm
    template_name_suffix = '_update_form'
    

    def get_success_url(self):
        return reverse_lazy('forms:flor-update',args=[self.object.id]) + '?ok'


###### Numero de personal

    
@method_decorator(login_required,name='dispatch')
class PersonalRequeridoListView(ListView):
    model = PersonalRequerido
    template_name = "formulario/personalrequerido_list.html"
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=PersonalRequerido._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        
        return context

@method_decorator(login_required,name='dispatch')
class PersonalRequeridoCreate(CreateView):
    
    model = PersonalRequerido
    form_class = PersonalRequeridoForm

    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(PersonalRequeridoCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=PersonalRequerido._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=PersonalRequeridoForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        return  reverse_lazy('forms:personal',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class PersonalRequeridoUpdate(UpdateView):
    model = PersonalRequerido
    form_class = PersonalRequeridoForm
    template_name_suffix = '_update_form'
    

    def get_success_url(self):
        return reverse_lazy('forms:personal-update',args=[self.object.id]) + '?ok'


################################################ Insumos zonificación

@method_decorator(login_required,name='dispatch')
class InsumosZonificacionListView(ListView):
    model = InsumosZonificacion
    template_name = "formulario/insumoszonificacion_list.html"
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=InsumosZonificacion._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa

        
        return context

@method_decorator(login_required,name='dispatch')
class InsumosZonificacionCreate(CreateView):
    
    model = InsumosZonificacion
    form_class = InsumosZonificacionForm
    template_name = "formulario/templatezonificacion_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
        
        return super(InsumosZonificacionCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['lista'] ='forms:insumo-list'
        context['id_f']=this_id
        context['p_title']=InsumosZonificacion._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=InsumosZonificacionForm(initial=initial_data)
        context['form'].fields['insumo'].queryset = InsumosLista.objects.filter(fase=id_form.fase)
        
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        return  reverse_lazy('forms:insumo',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class InsumosZonificacionUpdate(UpdateView):
    model = InsumosZonificacion
    form_class = InsumosZonificacionForm
    template_name = "formulario/templatezonificacion_update_form.html"
    def get_success_url(self):
        return reverse_lazy('forms:insumo-update',args=[self.object.id]) + '?ok'

################################################ maquinaria zonificacion

@method_decorator(login_required,name='dispatch')
class MaquinariaZonificacionListView(ListView):
    model = MaquinariaZonificacion
    template_name = "formulario/maquinariazonificacion_list.html"
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=MaquinariaZonificacion._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        
        return context

@method_decorator(login_required,name='dispatch')
class MaquinariaZonificacionCreate(CreateView):
    
    model = MaquinariaZonificacion
    form_class = MaquinariaZonificacionForm

    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(MaquinariaZonificacionCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=MaquinariaZonificacion._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=MaquinariaZonificacionForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        CatForm.objects.filter(id=this_id).update(completo = False)
        return  reverse_lazy('forms:maquinaria',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class MaquinariaZonificacionUpdate(UpdateView):
    model = MaquinariaZonificacion
    form_class = MaquinariaZonificacionForm
    template_name_suffix = '_update_form'

    
    def get_success_url(self):
        elemento = MaquinariaZonificacion.objects.filter(id =self.object.id)[0]
        CatForm.objects.filter(componente=elemento.componente,etapa=elemento.etapa,title="Maquinaria por zonificación").update(completo = False)

        return reverse_lazy('forms:maquinaria-update',args=[self.object.id]) + '?ok'

################################################ Desmonte, despalme, #############################################

@method_decorator(login_required,name='dispatch')
class MovimientoTierraZonificacionListView(ListView):
    model = MovimientoTierraZonificacion
    template_name = "formulario/movimientotierrazonificacion_list.html"
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=MovimientoTierraZonificacion._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        
        return context

@method_decorator(login_required,name='dispatch')
class MovimientoTierraZonificacionCreate(CreateView):
    
    model = MovimientoTierraZonificacion
    form_class = MovimientoTierraZonificacionForm

    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(MovimientoTierraZonificacionCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=MovimientoTierraZonificacion._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=MovimientoTierraZonificacionForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        CatForm.objects.filter(id=this_id).update(completo = False)
        return  reverse_lazy('forms:mtierra',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class MovimientoTierraZonificacionUpdate(UpdateView):
    model = MovimientoTierraZonificacion
    form_class = MovimientoTierraZonificacionForm
    template_name_suffix = '_update_form'

    
    def get_success_url(self):
        elemento = MovimientoTierraZonificacion.objects.filter(id =self.object.id)[0]
        CatForm.objects.filter(componente=elemento.componente,etapa=elemento.etapa,title="Desmonte, despalme, excavación y relleno por tipo de zonificación").update(completo = False)

        return reverse_lazy('forms:mtierra-update',args=[self.object.id]) + '?ok'


################################################ Residuos sólidos por zonificación #############################################

@method_decorator(login_required,name='dispatch')
class ResiduosSolidosZonificacionListView(ListView):
    model = ResiduosSolidosZonificacion
    template_name = "formulario/residuossolidoszonificacion_list.html"
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=ResiduosSolidosZonificacion._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        
        return context

@method_decorator(login_required,name='dispatch')
class ResiduosSolidosZonificacionCreate(CreateView):
    
    model = ResiduosSolidosZonificacion
    form_class = ResiduosSolidosZonificacionForm

    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(ResiduosSolidosZonificacionCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=ResiduosSolidosZonificacion._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=ResiduosSolidosZonificacionForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        CatForm.objects.filter(id=this_id).update(completo = False)
        return  reverse_lazy('forms:rsolidos',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class ResiduosSolidosZonificacionUpdate(UpdateView):
    model = ResiduosSolidosZonificacion
    form_class = ResiduosSolidosZonificacionForm
    template_name_suffix = '_update_form'

    
    def get_success_url(self):
        elemento = ResiduosSolidosZonificacion.objects.filter(id =self.object.id)[0]
        CatForm.objects.filter(componente=elemento.componente,etapa=elemento.etapa,title="Generación de residuos sólidos por zonificación").update(completo = False)

        return reverse_lazy('forms:rsolidos-update',args=[self.object.id]) + '?ok'




################################################ Procesos constructivos por zonificación #############################################

@method_decorator(login_required,name='dispatch')
class ProcesosConstructivosZonificacionListView(ListView):
    model = ProcesosConstructivosZonificacion
    template_name = "formulario/procesosconstructivos_list.html"
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=ProcesosConstructivosZonificacion._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        
        return context

@method_decorator(login_required,name='dispatch')
class ProcesosConstructivosZonificacionCreate(CreateView):
    
    model = ProcesosConstructivosZonificacion
    form_class = ProcesosConstructivosZonificacionForm

    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(ProcesosConstructivosZonificacionCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=ProcesosConstructivosZonificacion._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=ProcesosConstructivosZonificacionForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        CatForm.objects.filter(id=this_id).update(completo = False)
        return  reverse_lazy('forms:pconsz',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class ProcesosConstructivosZonificacionUpdate(UpdateView):
    model = ProcesosConstructivosZonificacion
    form_class = ProcesosConstructivosZonificacionForm
    template_name_suffix = '_update_form'

    
    def get_success_url(self):
        elemento = ProcesosConstructivosZonificacion.objects.filter(id =self.object.id)[0]
        CatForm.objects.filter(componente=elemento.componente,etapa=elemento.etapa,title="Procesos constructivos por zonificación").update(completo = False)

        return reverse_lazy('forms:rsolidos-update',args=[self.object.id]) + '?ok'

################################################ Uso de sustancias quimicas peligrosas por zonificación #############################################

@method_decorator(login_required,name='dispatch')
class UsoSustanciasZonificacionListView(ListView):
    model = UsoSustanciasZonificacion
    template_name = "formulario/usosustanciaszonificacion_list.html"
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=UsoSustanciasZonificacion._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        
        return context

@method_decorator(login_required,name='dispatch')
class UsoSustanciasZonificacionCreate(CreateView):
    
    model = UsoSustanciasZonificacion
    form_class = UsoSustanciasZonificacionForm

    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(UsoSustanciasZonificacionCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=UsoSustanciasZonificacion._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=UsoSustanciasZonificacionForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        CatForm.objects.filter(id=this_id).update(completo = False)
        return  reverse_lazy('forms:usosusz-list',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class UsoSustanciasZonificacionUpdate(UpdateView):
    model = UsoSustanciasZonificacion
    form_class = UsoSustanciasZonificacionForm
    template_name_suffix = '_update_form'

    
    def get_success_url(self):
        elemento = UsoSustanciasZonificacion.objects.filter(id =self.object.id)[0]
        CatForm.objects.filter(componente=elemento.componente,etapa=elemento.etapa,title=UsoSustanciasZonificacion._meta.verbose_name).update(completo = False)

        return reverse_lazy('forms:usosusz-update',args=[self.object.id]) + '?ok'






###################

### Datos generales general 
@method_decorator(login_required,name='dispatch')
class DatosGeneralListView(ListView):
    model = DatosGeneral
    template_name = "formulario/datosgeneral_list.html"
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=DatosGeneral._meta.verbose_name
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        return context


class DatosGeneralCreate(CreateView):
    
    model = DatosGeneral
    form_class = DatosGeneralForm
    
    def get(self, *args, **kwargs):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        if DatosGeneral.objects.filter(componente=id_form.componente.id,fase=id_form.fase.id,etapa=id_form.etapa.id):
            id_form_fig = DatosGeneral.objects.filter(componente=id_form.componente.id,fase=id_form.fase.id,etapa=id_form.etapa.id)
            return redirect('forms:datosgenerales-update',id_form_fig[0].id)
        else:
            return super().get(*args, **kwargs)


    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(DatosGeneralCreate, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['validado']=id_form.completo

        context['p_title']=DatosGeneral._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['f_id']= this_id
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=DatosGeneralForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        return  reverse_lazy('forms:datosgenerales',args=[this_id]) + '?ok'

@method_decorator(login_required,name='dispatch')
class DatosGeneralUpdate(UpdateView):
    model = DatosGeneral
    form_class = DatosGeneralForm
    template_name_suffix = '_update_form'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        elemento = DatosGeneral.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=DatosGeneral._meta.verbose_name
        context['i']=elemento   
        context['p_componente']=elemento.componente
        context['p_fase']= elemento.fase
        context['p_etapa']= elemento.etapa
        context['avance'] = CatForm.objects.filter(title=DatosGeneral._meta.verbose_name,
                                            etapa=elemento.etapa,
                                            componente=elemento.componente)[0]
        return context
    def get_success_url(self):
        return reverse_lazy('forms:datosgenerales-update',args=[self.object.id]) + '?ok'







### Descipcion general 
@method_decorator(login_required,name='dispatch')
class DescripcionGeneralDetailView(DetailView):
    model = DescripcionGeneral
    template_name = "formulario/descripciongeneral_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=DescripcionGeneral._meta.verbose_name
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = DescripcionGeneral.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['existe1'] = len(DescripcionGeneral.objects.filter(componente=id_form.componente.id,fase=id_form.fase.id,etapa=id_form.etapa.id))

        return context


#### esto no se ocupa ya ###
@method_decorator(login_required,name='dispatch')
class DescripcionGeneralListView(ListView):
    model = DescripcionGeneral
    template_name = "formulario/descripciongeneral_list.html"
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=DescripcionGeneral._meta.verbose_name
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['existe1'] = len(DescripcionGeneral.objects.filter(componente=id_form.componente.id,fase=id_form.fase.id,etapa=id_form.etapa.id))

        return context


class DescripcionGeneralCreate(CreateView):
    
    model = DescripcionGeneral
    form_class = DescripcionGeneralForm


    def get(self, *args, **kwargs):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        if DescripcionGeneral.objects.filter(componente=id_form.componente.id,fase=id_form.fase.id,etapa=id_form.etapa.id).exists():
            id_form_fig = DescripcionGeneral.objects.filter(componente=id_form.componente.id,fase=id_form.fase.id,etapa=id_form.etapa.id)
            return redirect('forms:generales-update',id_form_fig[0].id)
        else:
            return super().get(*args, **kwargs)

    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(DescripcionGeneralCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR

        context['p_title']=DescripcionGeneral._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['f_id']= this_id
        
        #context['descripcionfiguras']= DescripcionGeneralFiguras.objects.all()
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=DescripcionGeneralForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        return  reverse_lazy('forms:fichas')

@method_decorator(login_required,name='dispatch')

class DescripcionGeneralUpdate(UpdateView):
    model = DescripcionGeneral
    form_class = DescripcionGeneralForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        elemento = DescripcionGeneral.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_componente']=elemento.componente.title
        context['p_fase']=elemento.fase.title
        context['p_etapa']= elemento.etapa.title
        context['f_id']= this_id
        context['p_title']=DescripcionGeneral._meta.verbose_name
        context['avance'] = CatForm.objects.filter(title='Descripción general del componente',
                                            etapa=elemento.etapa,
                                            componente=elemento.componente)[0]
        context['descripcionfiguras']= DescripcionGeneralFiguras.objects.filter(componente=elemento.componente.id,etapa=elemento.etapa)
        context['txt_exitoso']='Actualizado correctamente'

        return context
    def get_success_url(self):
        return reverse_lazy('forms:generales-update',args=[self.object.id]) + '?ok'

###### Descripción general Figuras
@method_decorator(login_required,name='dispatch')
class DescripcionGeneralFigurasListView(ListView):
    model = DescripcionGeneralFiguras
    template_name = "formulario/descripciongeneralfiguras_list.html"
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=DescripcionGeneralFiguras._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        
        return context

@method_decorator(login_required,name='dispatch')
class DescripcionGeneralFigurasCreate(CreateView):
    
    model = DescripcionGeneralFiguras
    form_class = DescripcionGeneralFigurasForm
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = DescripcionGeneral.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(DescripcionGeneralFigurasCreate, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_lugar =str(self.request.get_full_path()).split("/")[-3]
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = DescripcionGeneral.objects.filter(id=this_id)[0] #NO MODIFICAR

        context['id_f']=this_id
        context['this_lugar']=this_lugar
        context['p_title']=DescripcionGeneralFiguras._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=DescripcionGeneralFigurasForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =str(self.request.get_full_path()).split("/")[-2]
        return  reverse_lazy('forms:generales-update',args=[this_id]) + '?ok'
 


@method_decorator(login_required,name='dispatch')
class DescripcionGeneralFigurasUpdate(UpdateView):
    model = DescripcionGeneralFiguras
    form_class = DescripcionGeneralFigurasForm
    template_name_suffix = '_update_form'
    

    def get_success_url(self):
        return reverse_lazy('forms:generalesfiguras-update',args=[self.object.id]) + '?ok'


###### FRECUENCIA DE ACTIVIDADES DE OBRAS PROVISIONALES


    
@method_decorator(login_required,name='dispatch')
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

@method_decorator(login_required,name='dispatch')
class FrecuenciaActividadesCCreate(CreateView):
    
    model = FrecuenciaActividadesC
    form_class = FrecuenciaActividadesCForm

    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(FrecuenciaActividadesCCreate, self).form_valid(form)

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


@method_decorator(login_required,name='dispatch')
class FrecuenciaActividadesCUpdate(UpdateView):
    model = FrecuenciaActividadesC
    form_class = FrecuenciaActividadesCForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('forms:actividad-update',args=[self.object.id]) + '?ok'


####################################---- GENERALES --- ##########################

#### LOCALIZACION

@method_decorator(login_required,name='dispatch')
class LocalizacionCreate(CreateView):
    
    model = ImagenLocalizacionC
    form_class = FormLocalizacionC
    def get(self, *args, **kwargs):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        if ImagenLocalizacionC.objects.filter(componente=id_form.componente.id,fase=id_form.fase.id,etapa=id_form.etapa.id):
            id_form_fig = ImagenLocalizacionC.objects.filter(componente=id_form.componente.id,fase=id_form.fase.id,etapa=id_form.etapa.id)
            return redirect('forms:fig-update',id_form_fig[0].id)
        else:
            return super().get(*args, **kwargs)
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(LocalizacionCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=FormLocalizacionC(initial=initial_data)
        context['p_componente']=id_form.componente
        context['p_etapa']= id_form.etapa
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        return  reverse_lazy('forms:fichas')


@method_decorator(login_required,name='dispatch')
class LocalizacionCListView(ListView):
    model = ImagenLocalizacionC
    template_name = "formulario/imagenlocalizacionc_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=ImagenLocalizacionC._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['existe1'] = len(ImagenLocalizacionC.objects.filter(componente=id_form.componente.id,fase=id_form.fase.id,etapa=id_form.etapa.id))
        
        return context






@method_decorator(login_required,name='dispatch')
class LocalizacionCUpdate(UpdateView):
    model = ImagenLocalizacionC
    form_class = FormLocalizacionC
    template_name_suffix = '_update_form'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        figura = ImagenLocalizacionC.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['i']=figura   
        context['p_componente']=figura.componente
        context['p_fase']= figura.fase
        context['p_etapa']= figura.etapa
        context['avance'] = CatForm.objects.filter(title='Imagen de localización y tipos de aprovechamiento',
                                            etapa=figura.etapa.id,
                                            componente=figura.componente.id)[0]
        return context

    def get_success_url(self):
        return reverse_lazy('forms:fig-update',args=[self.object.id]) + '?ok'


#### FRECUENCIA DE ACTIVIDADES
@method_decorator(login_required,name='dispatch')
class FrecuenciaActividadesListView(ListView):
    model = FrecuenciaActividades
    template_name = "formulario/frecuenciaactividades_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=FrecuenciaActividades._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['crear']='forms:actividadf-create'
        context['actualizar']='forms:actividadf-update'
        campos_exc = ['id','created','updated','componente','fase','etapa']
        context['campos']=[field.verbose_name for field in FrecuenciaActividades._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in FrecuenciaActividades._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        
        return context

@method_decorator(login_required,name='dispatch')
class FrecuenciaActividadesCreate(CreateView):
    
    model = FrecuenciaActividades
    form_class = FrecuenciaActividadesForm
    template_name = "formulario/template_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(FrecuenciaActividadesCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=FrecuenciaActividades._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:actividadf-list'
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=FrecuenciaActividadesForm(initial=initial_data)
        context['form'].fields['actividades'].queryset = ListaActividades.objects.filter(fase=id_form.fase)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        return  reverse_lazy('forms:actividadf-create',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class FrecuenciaActividadesUpdate(UpdateView):
    model = FrecuenciaActividades
    form_class = FrecuenciaActividadesForm
    template_name = "formulario/template_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=FrecuenciaActividades._meta.verbose_name
        context['regresar']='forms:actividadf-list'
        context['txt_actualizacion']="Actividad actualizada correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:actividadf-update',args=[self.object.id]) + '?ok'



#### INSUMOS REQUERIDOS Y ALMACENADOS
@method_decorator(login_required,name='dispatch')
class InsumosRequeridosAlmacenadosListView(ListView):
    model = InsumosRequeridosAlmacenados
    template_name = "formulario/insumos_req_alm_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=InsumosRequeridosAlmacenados._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['crear']='forms:insreqalm-create'
        context['actualizar']='forms:insreqalm-update'
        campos_exc = ['id','created','updated','componente','fase','etapa']
        context['campos']=[field.verbose_name for field in InsumosRequeridosAlmacenados._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in InsumosRequeridosAlmacenados._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        
        return context

@method_decorator(login_required,name='dispatch')
class InsumosRequeridosAlmacenadosCreate(CreateView):
    
    model = InsumosRequeridosAlmacenados
    form_class = InsumosRequeridosAlmacenadosForm
    template_name = "formulario/template_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(InsumosRequeridosAlmacenadosCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=InsumosRequeridosAlmacenados._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:insreqalm-list'
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=InsumosRequeridosAlmacenadosForm(initial=initial_data)
        context['form'].fields['insumo'].queryset = InsumosLista.objects.filter(fase=id_form.fase)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        return  reverse_lazy('forms:insreqalm-create',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class InsumosRequeridosAlmacenadosUpdate(UpdateView):
    model = InsumosRequeridosAlmacenados
    form_class = InsumosRequeridosAlmacenadosForm
    template_name = "formulario/template_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=InsumosRequeridosAlmacenados._meta.verbose_name
        context['regresar']='forms:insreqalm-list'
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:insreqalm-update',args=[self.object.id]) + '?ok'

###### Uso de sustancias químicas peligrosas

@method_decorator(login_required,name='dispatch')
class UsoSustanciasQuimicasListView(ListView):
    model = UsoSustanciasQuimicas
    template_name = "formulario/uso_sustancias_quim.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=UsoSustanciasQuimicas._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['crear']='forms:usosusquim-create'
        context['actualizar']='forms:usosusquim-update'
        campos_exc = ['id','created','updated','componente','fase','etapa']
        context['campos']=[field.verbose_name for field in UsoSustanciasQuimicas._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in UsoSustanciasQuimicas._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        
        return context

@method_decorator(login_required,name='dispatch')
class UsoSustanciasQuimicasCreate(CreateView):
    
    model = UsoSustanciasQuimicas
    form_class = UsoSustanciasQuimicasForm
    template_name = "formulario/template_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(UsoSustanciasQuimicasCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=UsoSustanciasQuimicas._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:usosusquim-list'
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=UsoSustanciasQuimicasForm(initial=initial_data)
        context['form'].fields['sustancia'].queryset = SustanciasQuimicasP.objects.filter(fase=id_form.fase)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        return  reverse_lazy('forms:usosusquim-create',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class UsoSustanciasQuimicasUpdate(UpdateView):
    model = UsoSustanciasQuimicas
    form_class = UsoSustanciasQuimicasForm
    template_name = "formulario/template_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=UsoSustanciasQuimicas._meta.verbose_name
        context['regresar']='forms:usosusquim-list'
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:usosusquim-update',args=[self.object.id]) + '?ok'


###### Personal

@method_decorator(login_required,name='dispatch')
class PersonalListView(ListView):
    model = Personal
    template_name = "formulario/personal_etapa.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=Personal._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['crear']='forms:personale-create'
        context['actualizar']='forms:personale-update'
        campos_exc = ['id','created','updated','componente','fase','etapa']
        context['campos']=[field.verbose_name for field in Personal._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in Personal._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        
        return context

@method_decorator(login_required,name='dispatch')
class PersonalCreate(CreateView):
    
    model = Personal
    form_class = PersonalForm
    template_name = "formulario/template_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(PersonalCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=Personal._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:personale-list'
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=PersonalForm(initial=initial_data)
        context['form'].fields['personal'].queryset = ListaTipoPersonal.objects.filter(fase=id_form.fase)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        return  reverse_lazy('forms:personale-create',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class PersonalUpdate(UpdateView):
    model = Personal
    form_class = PersonalForm
    template_name = "formulario/template_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=Personal._meta.verbose_name
        context['regresar']='forms:personale-list'
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:personale-update',args=[self.object.id]) + '?ok'


### Tipo de vehículos por zonificación
@method_decorator(login_required,name='dispatch')
class VehiculosRestrigidosZonificacionListView(ListView):
    model = VehiculosRestrigidosZonificacion
    template_name = "formulario/vehreszon_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=VehiculosRestrigidosZonificacion._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['crear']='forms:vehreszon-create'
        context['actualizar']='forms:vehreszon-update'
        campos_exc = ['id','created','updated','componente','fase','etapa']
        context['campos']=[field.verbose_name for field in VehiculosRestrigidosZonificacion._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in VehiculosRestrigidosZonificacion._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        
        return context

@method_decorator(login_required,name='dispatch')
class VehiculosRestrigidosZonificacionCreate(CreateView):
    
    model = VehiculosRestrigidosZonificacion
    form_class = VehiculosRestrigidosZonificacionForm
    template_name = "formulario/template_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(VehiculosRestrigidosZonificacionCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=VehiculosRestrigidosZonificacion._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:vehreszon-list'
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=VehiculosRestrigidosZonificacionForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        return  reverse_lazy('forms:vehreszon-create',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class VehiculosRestrigidosZonificacionUpdate(UpdateView):
    model = VehiculosRestrigidosZonificacion
    form_class = VehiculosRestrigidosZonificacionForm
    template_name = "formulario/template_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=VehiculosRestrigidosZonificacion._meta.verbose_name
        context['regresar']='forms:vehreszon-list'
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:vehreszon-update',args=[self.object.id]) + '?ok'


### Uso de maquinaria
@method_decorator(login_required,name='dispatch')
class UsoMaquinariaListView(ListView):
    model = UsoMaquinaria
    template_name = "formulario/usomaquina_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=UsoMaquinaria._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['crear']='forms:usomaquina-create'
        context['actualizar']='forms:usomaquina-update'
        campos_exc = ['id','created','updated','componente','fase','etapa']
        context['campos']=[field.verbose_name for field in UsoMaquinaria._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in UsoMaquinaria._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        
        return context

@method_decorator(login_required,name='dispatch')
class UsoMaquinariaCreate(CreateView):
    
    model = UsoMaquinaria
    form_class = UsoMaquinariaForm
    template_name = "formulario/template_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(UsoMaquinariaCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=UsoMaquinaria._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:usomaquina-list'
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=UsoMaquinariaForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        return  reverse_lazy('forms:usomaquina-create',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class UsoMaquinariaUpdate(UpdateView):
    model = UsoMaquinaria
    form_class = UsoMaquinariaForm
    template_name = "formulario/template_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=UsoMaquinaria._meta.verbose_name
        context['regresar']='forms:usomaquina-list'
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:usomaquina-update',args=[self.object.id]) + '?ok'

### GENERACION DE RESIDUOS SOLIDOS
@method_decorator(login_required,name='dispatch')
class GeneracionResiduosListView(ListView):
    model = GeneracionResiduos
    template_name = "formulario/genres_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=GeneracionResiduos._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['crear']='forms:genres-create'
        context['actualizar']='forms:genres-update'
        campos_exc = ['id','created','updated','componente','fase','etapa']
        context['campos']=[field.verbose_name for field in GeneracionResiduos._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in GeneracionResiduos._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        
        return context

@method_decorator(login_required,name='dispatch')
class GeneracionResiduosCreate(CreateView):
    
    model = GeneracionResiduos
    form_class = GeneracionResiduosForm
    template_name = "formulario/template_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(GeneracionResiduosCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=GeneracionResiduos._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:genres-list'
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=GeneracionResiduosForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        return  reverse_lazy('forms:genres-create',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class GeneracionResiduosUpdate(UpdateView):
    model = GeneracionResiduos
    form_class = GeneracionResiduosForm
    template_name = "formulario/template_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=GeneracionResiduos._meta.verbose_name
        context['regresar']='forms:genres-list'
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:genres-update',args=[self.object.id]) + '?ok'


### AFORO Y ALMACENAMIENTO VEHICULAR PARA ESTA FASE
@method_decorator(login_required,name='dispatch')
class AforoAlmacenamientoVehicularListView(ListView):
    model = AforoAlmacenamientoVehicular
    template_name = "formulario/afoalmveh_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=AforoAlmacenamientoVehicular._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['crear']='forms:afoalmveh-create'
        context['actualizar']='forms:afoalmveh-update'
        campos_exc = ['id','created','updated','componente','fase','etapa']
        context['campos']=[field.verbose_name for field in AforoAlmacenamientoVehicular._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in AforoAlmacenamientoVehicular._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        
        return context

@method_decorator(login_required,name='dispatch')
class AforoAlmacenamientoVehicularCreate(CreateView):
    
    model = AforoAlmacenamientoVehicular
    form_class = AforoAlmacenamientoVehicularForm
    template_name = "formulario/template_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(AforoAlmacenamientoVehicularCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=AforoAlmacenamientoVehicular._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:afoalmveh-list'
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=AforoAlmacenamientoVehicularForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        return  reverse_lazy('forms:afoalmveh-create',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class AforoAlmacenamientoVehicularUpdate(UpdateView):
    model = AforoAlmacenamientoVehicular
    form_class = AforoAlmacenamientoVehicularForm
    template_name = "formulario/template_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=AforoAlmacenamientoVehicular._meta.verbose_name
        context['regresar']='forms:afoalmveh-list'
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:afoalmveh-update',args=[self.object.id]) + '?ok'

### EXTRACCIÓN AGUA
@method_decorator(login_required,name='dispatch')
class ExtraccionAguaListView(ListView):
    model = ExtraccionAgua
    template_name = "formulario/extagua_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=ExtraccionAgua._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['crear']='forms:extagua-create'
        context['actualizar']='forms:extagua-update'
        campos_exc = ['id','created','updated','componente','fase','etapa']
        context['campos']=[field.verbose_name for field in ExtraccionAgua._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in ExtraccionAgua._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        
        return context

@method_decorator(login_required,name='dispatch')
class ExtraccionAguaCreate(CreateView):
    
    model = ExtraccionAgua
    form_class = ExtraccionAguaForm
    template_name = "formulario/template_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(ExtraccionAguaCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=ExtraccionAgua._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:extagua-list'
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=ExtraccionAguaForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        return  reverse_lazy('forms:extagua-create',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class ExtraccionAguaUpdate(UpdateView):
    model = ExtraccionAgua
    form_class = ExtraccionAguaForm
    template_name = "formulario/template_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=ExtraccionAgua._meta.verbose_name
        context['regresar']='forms:extagua-list'
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:extagua-update',args=[self.object.id]) + '?ok'

### Frecuencia de actividades comerciales o de servicio
@method_decorator(login_required,name='dispatch')
class FrecuenciaActComListView(ListView):
    model = FrecuenciaActCom
    template_name = "formulario/freactcom_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=FrecuenciaActCom._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['crear']='forms:freactcom-create'
        context['actualizar']='forms:freactcom-update'
        campos_exc = ['id','created','updated','componente','fase','etapa']
        context['campos']=[field.verbose_name for field in FrecuenciaActCom._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in FrecuenciaActCom._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        
        return context

@method_decorator(login_required,name='dispatch')
class FrecuenciaActComCreate(CreateView):
    
    model = FrecuenciaActCom
    form_class = FrecuenciaActComForm
    template_name = "formulario/template_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(FrecuenciaActComCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=FrecuenciaActCom._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:freactcom-list'
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=FrecuenciaActComForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        return  reverse_lazy('forms:freactcom-create',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class FrecuenciaActComUpdate(UpdateView):
    model = FrecuenciaActCom
    form_class = FrecuenciaActComForm
    template_name = "formulario/template_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=FrecuenciaActCom._meta.verbose_name
        context['regresar']='forms:freactcom-list'
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:freactcom-update',args=[self.object.id]) + '?ok'


### AFORO VISITANTES
@method_decorator(login_required,name='dispatch')
class AforoVisitantesListView(ListView):
    model = AforoVisitantes
    template_name = "formulario/afovis_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=AforoVisitantes._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['crear']='forms:afovis-create'
        context['actualizar']='forms:afovis-update'
        campos_exc = ['id','created','updated','componente','fase','etapa']
        context['campos']=[field.verbose_name for field in AforoVisitantes._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in AforoVisitantes._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        
        return context

@method_decorator(login_required,name='dispatch')
class AforoVisitantesCreate(CreateView):
    
    model = AforoVisitantes
    form_class = AforoVisitantesForm
    template_name = "formulario/template_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(AforoVisitantesCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=AforoVisitantes._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:afovis-list'
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=AforoVisitantesForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        return  reverse_lazy('forms:afovis-create',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class AforoVisitantesUpdate(UpdateView):
    model = AforoVisitantes
    form_class = AforoVisitantesForm
    template_name = "formulario/template_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=AforoVisitantes._meta.verbose_name
        context['regresar']='forms:afovis-list'
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:afovis-update',args=[self.object.id]) + '?ok'


### AFORO MAXIMO VEHICULAR
@method_decorator(login_required,name='dispatch')
class AforoTipoVehiMaxDiarioListView(ListView):
    model = AforoTipoVehiMaxDiario
    template_name = "formulario/afovehmaxdia_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=AforoTipoVehiMaxDiario._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['crear']='forms:afovehmaxdia-create'
        context['actualizar']='forms:afovehmaxdia-update'
        campos_exc = ['id','created','updated','componente','fase','etapa']
        context['campos']=[field.verbose_name for field in AforoTipoVehiMaxDiario._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in AforoTipoVehiMaxDiario._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        
        return context

@method_decorator(login_required,name='dispatch')
class AforoTipoVehiMaxDiarioCreate(CreateView):
    
    model = AforoTipoVehiMaxDiario
    form_class = AforoTipoVehiMaxDiarioForm
    template_name = "formulario/template_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(AforoTipoVehiMaxDiarioCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=AforoTipoVehiMaxDiario._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:afovehmaxdia-list'
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=AforoTipoVehiMaxDiarioForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        return  reverse_lazy('forms:afovehmaxdia-create',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class AforoTipoVehiMaxDiarioUpdate(UpdateView):
    model = AforoTipoVehiMaxDiario
    form_class = AforoTipoVehiMaxDiarioForm
    template_name = "formulario/template_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=AforoTipoVehiMaxDiario._meta.verbose_name
        context['regresar']='forms:afovehmaxdia-list'
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:afovehmaxdia-update',args=[self.object.id]) + '?ok'


### AFORO  VEHICULAR TOTAL
@method_decorator(login_required,name='dispatch')
class AforoTipoVehiListView(ListView):
    model = AforoTipoVehi
    template_name = "formulario/afovehtot_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=AforoTipoVehi._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['crear']='forms:afovehtot-create'
        context['actualizar']='forms:afovehtot-update'
        campos_exc = ['id','created','updated','componente','fase','etapa']
        context['campos']=[field.verbose_name for field in AforoTipoVehi._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in AforoTipoVehi._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        
        return context

@method_decorator(login_required,name='dispatch')
class AforoTipoVehiCreate(CreateView):
    
    model = AforoTipoVehi
    form_class = AforoTipoVehiForm
    template_name = "formulario/template_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(AforoTipoVehiCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=AforoTipoVehi._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:afovehtot-list'
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=AforoTipoVehiForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        return  reverse_lazy('forms:afovehtot-create',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class AforoTipoVehiUpdate(UpdateView):
    model = AforoTipoVehi
    form_class = AforoTipoVehiForm
    template_name = "formulario/template_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=AforoTipoVehi._meta.verbose_name
        context['regresar']='forms:afovehtot-list'
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:afovehtot-update',args=[self.object.id]) + '?ok'

### PERSONAL TRANSPORTADO 
@method_decorator(login_required,name='dispatch')
class PersonalTransportadoListView(ListView):
    model = PersonalTransportado
    template_name = "formulario/pertra_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=PersonalTransportado._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['crear']='forms:pertra-create'
        context['actualizar']='forms:pertra-update'
        campos_exc = ['id','created','updated','componente','fase','etapa']
        context['campos']=[field.verbose_name for field in PersonalTransportado._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in PersonalTransportado._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        
        return context

@method_decorator(login_required,name='dispatch')
class PersonalTransportadoCreate(CreateView):
    
    model = PersonalTransportado
    form_class = PersonalTransportadoForm
    template_name = "formulario/template_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(PersonalTransportadoCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=PersonalTransportado._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:pertra-list'
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=PersonalTransportadoForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        return  reverse_lazy('forms:pertra-create',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class PersonalTransportadoUpdate(UpdateView):
    model = PersonalTransportado
    form_class = PersonalTransportadoForm
    template_name = "formulario/template_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=PersonalTransportado._meta.verbose_name
        context['regresar']='forms:pertra-list'
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:pertra-update',args=[self.object.id]) + '?ok'


### Ocupacion estimada de alojamiento
@method_decorator(login_required,name='dispatch')
class OcupacionAlojaListView(ListView):
    model = OcupacionAloja
    template_name = "formulario/ocualo_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=OcupacionAloja._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['crear']='forms:ocualo-create'
        context['actualizar']='forms:ocualo-update'
        campos_exc = ['id','created','updated','componente','fase','etapa']
        context['campos']=[field.verbose_name for field in OcupacionAloja._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in OcupacionAloja._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        
        return context

@method_decorator(login_required,name='dispatch')
class OcupacionAlojaCreate(CreateView):
    
    model = OcupacionAloja
    form_class = OcupacionAlojaForm
    template_name = "formulario/template_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(OcupacionAlojaCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=OcupacionAloja._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:ocualo-list'
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=OcupacionAlojaForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        return  reverse_lazy('forms:ocualo-create',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class OcupacionAlojaUpdate(UpdateView):
    model = OcupacionAloja
    form_class = OcupacionAlojaForm
    template_name = "formulario/template_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=OcupacionAloja._meta.verbose_name
        context['regresar']='forms:ocualo-list'
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:ocualo-update',args=[self.object.id]) + '?ok'


### MANEJO DE SUSTANCIAS ESPECIALES
@method_decorator(login_required,name='dispatch')
class ManejoSustanciasEspecialesListView(ListView):
    model = ManejoSustanciasEspeciales
    template_name = "formulario/mansusesp_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=ManejoSustanciasEspeciales._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['crear']='forms:mansusesp-create'
        context['actualizar']='forms:mansusesp-update'
        campos_exc = ['id','created','updated','componente','fase','etapa']
        context['campos']=[field.verbose_name for field in ManejoSustanciasEspeciales._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in ManejoSustanciasEspeciales._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        
        return context

@method_decorator(login_required,name='dispatch')
class ManejoSustanciasEspecialesCreate(CreateView):
    
    model = ManejoSustanciasEspeciales
    form_class = ManejoSustanciasEspecialesForm
    template_name = "formulario/template_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(ManejoSustanciasEspecialesCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=ManejoSustanciasEspeciales._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:mansusesp-list'
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=ManejoSustanciasEspecialesForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        return  reverse_lazy('forms:mansusesp-create',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class ManejoSustanciasEspecialesUpdate(UpdateView):
    model = ManejoSustanciasEspeciales
    form_class = ManejoSustanciasEspecialesForm
    template_name = "formulario/template_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=ManejoSustanciasEspeciales._meta.verbose_name
        context['regresar']='forms:mansusesp-list'
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:mansusesp-update',args=[self.object.id]) + '?ok'

#### CAPACIDAD DE ALMACENAMIENTO DE SUSTANCIAS

@method_decorator(login_required,name='dispatch')
class CapacidadAlmSustanciasEspecialesListView(ListView):
    model = CapacidadAlmSustanciasEspeciales
    template_name = "formulario/capalmsusesp_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=CapacidadAlmSustanciasEspeciales._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['crear']='forms:capalmsusesp-create'
        context['actualizar']='forms:capalmsusesp-update'
        campos_exc = ['id','created','updated','componente','fase','etapa']
        context['campos']=[field.verbose_name for field in CapacidadAlmSustanciasEspeciales._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in CapacidadAlmSustanciasEspeciales._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        
        return context

@method_decorator(login_required,name='dispatch')
class CapacidadAlmSustanciasEspecialesCreate(CreateView):
    
    model = CapacidadAlmSustanciasEspeciales
    form_class = CapacidadAlmSustanciasEspecialesForm
    template_name = "formulario/template_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(CapacidadAlmSustanciasEspecialesCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=CapacidadAlmSustanciasEspeciales._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:capalmsusesp-list'
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=CapacidadAlmSustanciasEspecialesForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        return  reverse_lazy('forms:capalmsusesp-create',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class CapacidadAlmSustanciasEspecialesUpdate(UpdateView):
    model = CapacidadAlmSustanciasEspeciales
    form_class = CapacidadAlmSustanciasEspecialesForm
    template_name = "formulario/template_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=CapacidadAlmSustanciasEspeciales._meta.verbose_name
        context['regresar']='forms:capalmsusesp-list'
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:capalmsusesp-update',args=[self.object.id]) + '?ok'


#### CAPACIDAD DE ALMACENAMIENTO DE RESIDUOS

@method_decorator(login_required,name='dispatch')
class CapacidadAlmResiduosEspecialesListView(ListView):
    model = CapacidadAlmResiduosEspeciales
    template_name = "formulario/capalmresesp_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=CapacidadAlmResiduosEspeciales._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['crear']='forms:capalmresesp-create'
        context['actualizar']='forms:capalmresesp-update'
        campos_exc = ['id','created','updated','componente','fase','etapa']
        context['campos']=[field.verbose_name for field in CapacidadAlmResiduosEspeciales._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in CapacidadAlmResiduosEspeciales._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        
        return context

@method_decorator(login_required,name='dispatch')
class CapacidadAlmResiduosEspecialesCreate(CreateView):
    
    model = CapacidadAlmResiduosEspeciales
    form_class = CapacidadAlmResiduosEspecialesForm
    template_name = "formulario/template_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(CapacidadAlmResiduosEspecialesCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=CapacidadAlmResiduosEspeciales._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:capalmresesp-list'
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=CapacidadAlmResiduosEspecialesForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        return  reverse_lazy('forms:capalmresesp-create',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class CapacidadAlmResiduosEspecialesUpdate(UpdateView):
    model = CapacidadAlmResiduosEspeciales
    form_class = CapacidadAlmResiduosEspecialesForm
    template_name = "formulario/template_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=CapacidadAlmResiduosEspeciales._meta.verbose_name
        context['regresar']='forms:capalmresesp-list'
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:capalmresesp-update',args=[self.object.id]) + '?ok'


#### FRECUENCIA DE INGRESO DE SUSTANCIAS EN INSTALACIONES ESPECIALES

@method_decorator(login_required,name='dispatch')
class FrecuenciaIngresoSusEspecialesListView(ListView):
    model = FrecuenciaIngresoSusEspeciales
    template_name = "formulario/freingsusesp_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=FrecuenciaIngresoSusEspeciales._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['crear']='forms:freingsusesp-create'
        context['actualizar']='forms:freingsusesp-update'
        campos_exc = ['id','created','updated','componente','fase','etapa']
        context['campos']=[field.verbose_name for field in FrecuenciaIngresoSusEspeciales._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in FrecuenciaIngresoSusEspeciales._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        
        return context

@method_decorator(login_required,name='dispatch')
class FrecuenciaIngresoSusEspecialesCreate(CreateView):
    
    model = FrecuenciaIngresoSusEspeciales
    form_class = FrecuenciaIngresoSusEspecialesForm
    template_name = "formulario/template_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(FrecuenciaIngresoSusEspecialesCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=FrecuenciaIngresoSusEspeciales._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:freingsusesp-list'
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=FrecuenciaIngresoSusEspecialesForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        return  reverse_lazy('forms:freingsusesp-create',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class FrecuenciaIngresoSusEspecialesUpdate(UpdateView):
    model = FrecuenciaIngresoSusEspeciales
    form_class = FrecuenciaIngresoSusEspecialesForm
    template_name = "formulario/template_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=FrecuenciaIngresoSusEspeciales._meta.verbose_name
        context['regresar']='forms:freingsusesp-list'
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:freingsusesp-update',args=[self.object.id]) + '?ok'


#### FRECUENCIA DE INGRESO DE RESIDUOS EN INSTALACIONES ESPECIALES

@method_decorator(login_required,name='dispatch')
class FrecuenciaIngresoResEspecialesListView(ListView):
    model = FrecuenciaIngresoResEspeciales
    template_name = "formulario/freingresesp_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=FrecuenciaIngresoResEspeciales._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['crear']='forms:freingresesp-create'
        context['actualizar']='forms:freingresesp-update'
        campos_exc = ['id','created','updated','componente','fase','etapa']
        context['campos']=[field.verbose_name for field in FrecuenciaIngresoResEspeciales._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in FrecuenciaIngresoResEspeciales._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        
        return context

@method_decorator(login_required,name='dispatch')
class FrecuenciaIngresoResEspecialesCreate(CreateView):
    
    model = FrecuenciaIngresoResEspeciales
    form_class = FrecuenciaIngresoResEspecialesForm
    template_name = "formulario/template_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(FrecuenciaIngresoResEspecialesCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=FrecuenciaIngresoResEspeciales._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:freingresesp-list'
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=FrecuenciaIngresoResEspecialesForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        return  reverse_lazy('forms:freingresesp-create',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class FrecuenciaIngresoResEspecialesUpdate(UpdateView):
    model = FrecuenciaIngresoResEspeciales
    form_class = FrecuenciaIngresoResEspecialesForm
    template_name = "formulario/template_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=FrecuenciaIngresoResEspeciales._meta.verbose_name
        context['regresar']='forms:freingresesp-list'
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:freingresesp-update',args=[self.object.id]) + '?ok'


#### MAQUINARIA Y VIAJES PARA EL SUMINISTRO DE SUSTANCIAS

@method_decorator(login_required,name='dispatch')
class MaquinariaViajesEspListView(ListView):
    model = MaquinariaViajesEsp
    template_name = "formulario/maqviaesp_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=MaquinariaViajesEsp._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['crear']='forms:maqviaesp-create'
        context['actualizar']='forms:maqviaesp-update'
        campos_exc = ['id','created','updated','componente','fase','etapa']
        context['campos']=[field.verbose_name for field in MaquinariaViajesEsp._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in MaquinariaViajesEsp._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        
        return context

@method_decorator(login_required,name='dispatch')
class MaquinariaViajesEspCreate(CreateView):
    
    model = MaquinariaViajesEsp
    form_class = MaquinariaViajesEspForm
    template_name = "formulario/template_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(MaquinariaViajesEspCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=MaquinariaViajesEsp._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:maqviaesp-list'
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=MaquinariaViajesEspForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        return  reverse_lazy('forms:maqviaesp-create',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class MaquinariaViajesEspUpdate(UpdateView):
    model = MaquinariaViajesEsp
    form_class = MaquinariaViajesEspForm
    template_name = "formulario/template_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=MaquinariaViajesEsp._meta.verbose_name
        context['regresar']='forms:maqviaesp-list'
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:maqviaesp-update',args=[self.object.id]) + '?ok'


#### Tratamiento de aguas residuales

@method_decorator(login_required,name='dispatch')
class TratamientoAguasResidualesListView(ListView):
    model = TratamientoAguasResiduales
    template_name = "formulario/traagures_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=TratamientoAguasResiduales._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        context['crear']='forms:traagures-create'
        context['actualizar']='forms:traagures-update'
        campos_exc = ['id','created','updated','componente','fase','etapa']
        context['campos']=[field.verbose_name for field in TratamientoAguasResiduales._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in TratamientoAguasResiduales._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        
        return context

@method_decorator(login_required,name='dispatch')
class TratamientoAguasResidualesCreate(CreateView):
    
    model = TratamientoAguasResiduales
    form_class = TratamientoAguasResidualesForm
    template_name = "formulario/template_form.html"
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(TratamientoAguasResidualesCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=TratamientoAguasResiduales._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:traagures-list'
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=TratamientoAguasResidualesForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        return  reverse_lazy('forms:traagures-create',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class TratamientoAguasResidualesUpdate(UpdateView):
    model = TratamientoAguasResiduales
    form_class = TratamientoAguasResidualesForm
    template_name = "formulario/template_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=TratamientoAguasResiduales._meta.verbose_name
        context['regresar']='forms:traagures-list'
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:traagures-update',args=[self.object.id]) + '?ok'

## Descripción de las obras provisionales temporales de este componente

@method_decorator(login_required,name='dispatch')
class DescripcionObrasTemporalesCreate(CreateView):
    
    model = DescripcionObrasTemporales
    form_class = DescripcionObrasTemporalesForm
    template_name = "formulario/template_text_form.html"
    
    def get(self, *args, **kwargs):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        if DescripcionObrasTemporales.objects.filter(componente=id_form.componente.id,fase=id_form.fase.id,etapa=id_form.etapa.id):
            id_form_fig = DescripcionObrasTemporales.objects.filter(componente=id_form.componente.id,fase=id_form.fase.id,etapa=id_form.etapa.id)
            return redirect('forms:desopemanobrtem-update',id_form_fig[0].id)
        else:
            return super().get(*args, **kwargs)



    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(DescripcionObrasTemporalesCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['validado']=id_form.completo
        context['id_f']=this_id
        context['p_title']=DescripcionObrasTemporales._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:fichas'
        context['txt_exitoso']='Agregado correctamente.'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=DescripcionObrasTemporalesForm(initial=initial_data)
        return context

    def get_success_url(self):
        
        return  reverse_lazy('forms:fichas')


@method_decorator(login_required,name='dispatch')
class DescripcionObrasTemporalesUpdate(UpdateView):
    model = DescripcionObrasTemporales
    form_class = DescripcionObrasTemporalesForm
    template_name = "formulario/template_text_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        elemento = DescripcionObrasTemporales.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_componente']=elemento.componente.title
        context['p_fase']=elemento.fase.title
        context['p_etapa']= elemento.etapa
        context['f_id']= this_id
        context['p_title']=DescripcionObrasTemporales._meta.verbose_name
        context['regresar']='forms:fichas'
        context['avance'] = CatForm.objects.filter(title=context['p_title'],
                                            etapa=elemento.etapa,
                                            componente=elemento.componente)[0]
        context['txt_actualizacion']="Actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:desopemanobrtem-update',args=[self.object.id]) + '?ok'


## Descripción de la operación y mantenimiento de las obras provisionales temporales de este componente

@method_decorator(login_required,name='dispatch')
class DescripcionOpeManObrasTemporalesCreate(CreateView):
    
    model = DescripcionOpeManObrasTemporales
    form_class = DescripcionOpeManObrasTemporalesForm
    template_name = "formulario/template_text_form.html"
    
    def get(self, *args, **kwargs):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        if DescripcionOpeManObrasTemporales.objects.filter(componente=id_form.componente.id,fase=id_form.fase.id,etapa=id_form.etapa.id):
            id_form_fig = DescripcionOpeManObrasTemporales.objects.filter(componente=id_form.componente.id,fase=id_form.fase.id,etapa=id_form.etapa.id)
            return redirect('forms:desopemanobrtem-update',id_form_fig[0].id)
        else:
            return super().get(*args, **kwargs)



    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        form.instance.etapa = id_form.etapa
        form.instance.fase = id_form.fase
        form.instance.componente = id_form.componente
   
        return super(DescripcionOpeManObrasTemporalesCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['validado']=id_form.completo
        context['id_f']=this_id
        context['p_title']=DescripcionOpeManObrasTemporales._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['regresar']='forms:fichas'
        context['txt_exitoso']='Agregado correctamente.'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=DescripcionOpeManObrasTemporalesForm(initial=initial_data)
        return context

    def get_success_url(self):
        
        return  reverse_lazy('forms:fichas')


@method_decorator(login_required,name='dispatch')
class DescripcionOpeManObrasTemporalesUpdate(UpdateView):
    model = DescripcionOpeManObrasTemporales
    form_class = DescripcionOpeManObrasTemporalesForm
    template_name = "formulario/template_text_update_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        elemento = DescripcionOpeManObrasTemporales.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_componente']=elemento.componente.title
        context['p_fase']=elemento.fase.title
        context['p_etapa']= elemento.etapa
        context['f_id']= this_id
        context['p_title']=DescripcionOpeManObrasTemporales._meta.verbose_name
        context['regresar']='forms:fichas'
        context['avance'] = CatForm.objects.filter(title=context['p_title'],
                                            etapa=elemento.etapa,
                                            componente=elemento.componente)[0]
        context['txt_actualizacion']="Actualizado correctamente"
        return context
    def get_success_url(self):
        return reverse_lazy('forms:desopemanobrtem-update',args=[self.object.id]) + '?ok'


#########################################################
##### CONFIRMACIÓN DE FORMULARIOS Y ARMADO DE FICHAS ####
#########################################################

## Confirmación de formularios
class CatFormUpdate(UpdateView):
    model = CatForm
    form_class = FormCatForm
    template_name_suffix = '_update_form'
    
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        usuario = self.request.user
        form.instance.user = usuario
   
        return super(CatFormUpdate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]

        
        context['p_title']="Formulario completo"
        context['p_subtitle']=id_form.componente.title+" - "+id_form.fase.title+" - "+ str(id_form.etapa.title)
 
        if id_form.completo is True:
            context['txt_actualizacion']="Estado del formualario: completo y validado por: " +str(id_form.user)
            context['estado']="Estado del formualario: completo y validado por: " + str(id_form.user)
        else:
            context['txt_actualizacion']="Estado del formualario: pendiente"
        return context

    def get_success_url(self):
        return reverse_lazy('forms:completo',args=[self.object.id]) + '?ok'

@method_decorator(login_required,name='dispatch')
class EstructuraView(TemplateView):
    template_name = "formulario/fichas.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user.username
        context['login_usuario']=usuario
        #context['componentes'] = Modulo.objects.all()
        estructura = []
        componentes = Modulo.objects.all()#list(set([x.componente for x in CatForm.objects.all()]))
        etapas_l = []
        dicc_form = {}
        for componente in componentes:
            etapas_l.append(componente.etapas.all())
            estructura.append(CatForm.objects.filter(componente=componente).order_by('title'))
               
        

        context['componentes'] = Modulo.objects.all()
        context['etapas'] = etapas_l
        context['avances'] = zip(componentes,etapas_l,estructura) #CatForm.objects.all().order_by('title') #pd.DataFrame(list(CatForm.objects.all().values())) #
        context['completados'] = len(CatForm.objects.filter(completo=True))
        context['totales'] = len(CatForm.objects.values_list('title',))
        #context['formularios']=CatForm.objects.all()
        if context['totales']!=0:
            context['porcentaje'] = str(round((context['completados']/ context['totales'])*100,0))
        else:
            context['porcentaje'] = 0
        return context 

# @method_decorator(login_required,name='dispatch')
# class EstructuraView(TemplateView):
#     template_name = "formulario/fichas.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         usuario = self.request.user.username
#         context['login_usuario']=usuario
#         #context['componentes'] = Modulo.objects.all()
#         context['componentes'] = list(set([x.componente for x in CatForm.objects.all()]))
#         context['fases'] = Fase.objects.all().order_by('title')
#         context['etapas'] = Etapa.objects.all().order_by('id').reverse()
#         context['avances'] = CatForm.objects.all().order_by('title') #pd.DataFrame(list(CatForm.objects.all().values())) #
#         context['completados'] = len(CatForm.objects.filter(completo=True))
#         context['totales'] = len(CatForm.objects.values_list('title',))
#         if context['totales']!=0:
#             context['porcentaje'] = str(round((context['completados']/ context['totales'])*100,0))
#         else:
#             context['porcentaje'] = 0
#         return context


def regresa(key,objetos):

    for i in objetos:
        if i.title == key:
            return i

def regresa_i(key,objetos):
    for i in objetos:
        if i.title == key:
            return i

## aqui va lo del template
def getTemplate(tpl_path):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename)

def ensamblaficha(request,componente,fase,etapa):
   
    proyecto = "Pangea 4C"
    module_dir = os.path.dirname(__file__)  
    jinja_template_path = os.path.join(module_dir, 'templates','template_ficha.jinja')
    elcomponente = Modulo.objects.filter(id=componente)[0]
    descripcion_raw = DescripcionGeneral.objects.filter(componente_id=componente,fase_id=fase,etapa_id=etapa)[0].content
    descripcion_latex = pypandoc.convert_text(descripcion_raw,'latex', format='html', extra_args=['--atx-headers'])
    descripcion_bits = re.split('(\(fig\d+\))',descripcion_latex)
    descripcion = []
    for bit in descripcion_bits:
        if bit.startswith("(fig"):
            fig_id = int(bit.replace("(fig","").replace(")",""))
            path_figura = DescripcionGeneralFiguras.objects.filter(id=fig_id)[0].image.path
            path_figura = path_figura.replace(os.path.sep,"/")
            pie = DescripcionGeneralFiguras.objects.filter(id=fig_id)[0].pie
            
            descripcion.append("\includegraphics[width=0.5\\textwidth]{"+path_figura+"} \captionof{figure}{"+pie+"}")
        else:
            descripcion.append(bit)

    loc_img_path = ImagenLocalizacionC.objects.filter(componente_id=componente,fase_id=fase,etapa_id=etapa)[0].image.path
    loc_img_path = loc_img_path.replace(os.path.sep,"/")
    componente_title = elcomponente.title
    clave = elcomponente.abreviatura
    fase_title = Fase.objects.filter(id=fase)[0].title
    etapas = []
    for e in Etapa.objects.filter(fase_id=fase):
        etapas.append((e.inicio,e.fin))
    
    n_etapas = len(etapas)
    duracion_obra = DescripcionGeneral.objects.filter(componente_id=componente,fase_id=fase,etapa_id=etapa)[0].duracion
    hlines = ["~~|-|~~","~~|~|~~","~~|-|~~","~~|-|~~"]
    for e in range(0,n_etapas):
        hlines[0] += "~"
        hlines[1] += "|-"
        hlines[2] += "|-"
        hlines[3] += "~"
    hlines[0] += "~"
    hlines[1] += "~"
    hlines[2] += "~"
    hlines[3] += "~"

    datos = DatosGeneral.objects.filter(componente_id=componente,fase_id=fase,etapa_id=etapa)[0]
    titulo2 = "Datos generales del componente para esta fase"
    tabla2 = [["Superficie aprovechable total (ha)", datos.sup_aprov_total],
    ["Superficie edificable (ha)", datos.sup_edi],
    ["Superficie a construir no edificable (ha)", datos.sup_const_no_edi],
    ["Niveles máximos construidos", datos.nivel_max],
    ["Zonificación", datos.zonificacion]]
    anchos2 = [7,"N"]

    filterProcesos = SeleccionProcesosConstructivos.objects.filter(componente_id=componente,fase_id=fase,etapa_id=etapa)[0] 
    procesos_c = []
    for proceso in filterProcesos.procesos.all():
        procesos_c.append([proceso.title,pypandoc.convert_text(proceso.content,'latex', format='html', extra_args=['--atx-headers'])])

    titulo5 = "Frecuencia de actividades de obras provisionales"
    frecs_prov = FrecuenciaActividadesC.objects.filter(componente_id=componente,fase_id=fase,etapa_id=etapa)
    tabla5 = [["Actividades", "Jornadas/fase"]]
    for frec_prov in frecs_prov:
        tabla5.append([frec_prov.actividades,frec_prov.horas])
    anchos5 = [7,"N"]


    filterSistemas = SeleccionSistemasConstructivos.objects.filter(componente_id=componente,fase_id=fase,etapa_id=etapa)[0]
    sistemas_c = []
    for sistema in filterSistemas.sistemas.all():
        sistema_raw = sistema.content
        sistema_latex = pypandoc.convert_text(sistema_raw,'latex', format='html', extra_args=['--atx-headers'])
        sistema_bits = re.split('(\(fig\d+\))',sistema_latex)
        sistema_desc = []
        for bit in sistema_bits:
            if bit.startswith("(fig"):
                fig_id = int(bit.replace("(fig","").replace(")",""))
                path_figura = SisFiguras.objects.filter(id=fig_id)[0].image.path
                path_figura = path_figura.replace(os.path.sep,"/")
                pie = SisFiguras.objects.filter(id=fig_id)[0].pie
                
                sistema_desc.append("\includegraphics[width=0.5\\textwidth]{"+path_figura+"} \captionof{figure}{"+pie+"}")
            else:
                sistema_desc.append("\\footnotesize " + bit)
        sistemas_c.append([sistema.title,sistema_desc])



 

    context = {
        'loc_img_path': loc_img_path,
        'proyecto': proyecto,
        'etapa': etapa,
        'etapas': etapas,
        'n_etapas': n_etapas,
        'hlines': hlines,
        'componente': componente_title,
        'clave': clave,
        'fase': fase_title,
        'duracion_obra': f"{duracion_obra:,}",
        'descripcion': descripcion,
        'titulo2': titulo2,
        'tabla2': tabla2,
        'anchos2': anchos2,
        'titulo5': titulo5,
        'tabla5': tabla5,
        'anchos5': anchos5,
        'procesos_c': procesos_c,
        'sistemas_c': sistemas_c
    }
    

    template = getTemplate(jinja_template_path)
    tex_path = os.path.join(module_dir, 'pdfs','ficha_'+str(componente)+"_"+str(fase)+"_"+str(etapa)+".tex")
    
    with codecs.open (tex_path, "w", "utf-8") as miFile:
        output = template.render(context)
        output = re.sub(r'\{§', '{', output)
        output = re.sub(r'§\}', '}', output)
        output = re.sub(r'×', r'\\( \\times \\)', output)
        # jinja returns unicode - so `output` needs to be encoded to a bytestring
        # before writing it to a file
        miFile.write(output)

    
    #tex_path = tex_path.replace("/", "\\\\") ##descomentar para la version local

    #check_call(['xelatex', tex_path], stdin=DEVNULL, stdout=DEVNULL, stderr=STDOUT)

    time_old.sleep(1)
    os.chdir(os.path.join(module_dir, 'pdfs'))
    subprocess.run(["xelatex", "-interaction=nonstopmode", tex_path], stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    pdf_path = tex_path.replace(".tex",".pdf")

    with open(pdf_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=some_file.pdf'
        return response
    #output = pypandoc.convert_text('<h1>Primary Heading</h1>','latex', format='html', extra_args=['--atx-headers'])
    #return HttpResponse(elcomponente.title+descripcion)

# def agregar_estructura(request):
#     module_dir = os.path.dirname(__file__)  
#     file_path = os.path.join(module_dir, 'estructura_arbol_form2.txt')
#     estructura = pd.read_csv(file_path, delimiter='\t',encoding='utf-8')
#     estructura.sort_values(by='nombre',ascending=False)
#     l_componentes  = Modulo.objects.all()
#     l_etapas = Etapa.objects.all()
#     l_fases = Fase.objects.all()
#     dicc_fases ={}

    
#     for componente_i in l_componentes:
#         for etapa_i in l_etapas:
#             if etapa_i in componente_i.etapas.all():
#                 print("si esta")
#                 for index, row in estructura.iterrows():

#                     if row['tipo_c']== 1 and componente_i.t_base == True: #and componente_i.t_aprov_edificable == False and componente_i.t_obras == False and componente_i.t_areas_verdes == False and componente_i.t_aprov_lineal == False:
#                         nombre_f = row['nombre'] #0
#                         tipo_f = str(row['tipo']) #1
#                         tipoc_f = str(row['tipo_c']) #2
#                         componente_f =componente_i  #3
#                         fase_f =regresa_i(row['fase'],l_fases) #4
#                         etapa_f = etapa_i  # 5
#                         tag_url = str(row['tag-url'])
#                         orden = int(row['orden'])

#                         existe_form = CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f)
#                         print (len(existe_form))
#                         if len(existe_form)==0:

#                             agrega_form = CatForm(
#                                 title = nombre_f,
#                                 tipo = tipo_f,
#                                 tipo_c = tipoc_f,
#                                 componente = componente_f,
#                                 fase = fase_f,
#                                 etapa =etapa_f,
#                                 nurl = tag_url,
#                                 orden=orden,
#                                                 )
#                             agrega_form.save()
                    
#                     elif row['tipo_c']== 2 and componente_i.t_base == True and componente_i.t_aprov_edificable == True:  
#                         nombre_f = row['nombre'] #0
#                         tipo_f = str(row['tipo']) #1
#                         tipoc_f = str(row['tipo_c']) #2
#                         componente_f =componente_i  #3
#                         fase_f =regresa_i(row['fase'],l_fases) #4
#                         etapa_f = etapa_i  # 5
#                         tag_url = str(row['tag-url'])
#                         orden = int(row['orden'])
#                         existe_form = CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f)
#                         print (len(existe_form))
#                         if len(existe_form)==0:

#                             agrega_form = CatForm(
#                                 title = nombre_f,
#                                 tipo = tipo_f,
#                                 tipo_c = tipoc_f,
#                                 componente = componente_f,
#                                 fase = fase_f,
#                                 etapa =etapa_f,
#                                 nurl = tag_url,
#                                 orden=orden,
#                                                 )
#                             agrega_form.save()

#                     elif row['tipo_c']== 3 and componente_i.t_base == True and componente_i.t_obras == True:  
#                         nombre_f = row['nombre'] #0
#                         tipo_f = str(row['tipo']) #1
#                         tipoc_f = str(row['tipo_c']) #2
#                         componente_f =componente_i  #3
#                         fase_f =regresa_i(row['fase'],l_fases) #4
#                         etapa_f = etapa_i  # 5
#                         tag_url = str(row['tag-url'])
#                         orden = int(row['orden'])
#                         existe_form = CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f)
#                         print (len(existe_form))
#                         if len(existe_form)==0:

#                             agrega_form = CatForm(
#                                 title = nombre_f,
#                                 tipo = tipo_f,
#                                 tipo_c = tipoc_f,
#                                 componente = componente_f,
#                                 fase = fase_f,
#                                 etapa =etapa_f,
#                                 nurl = tag_url,
#                                 orden=orden,
#                                                 )
#                             agrega_form.save()

#                     elif row['tipo_c']== 4 and componente_i.t_base == True and componente_i.t_areas_verdes == True:  
#                         nombre_f = row['nombre'] #0
#                         tipo_f = str(row['tipo']) #1
#                         tipoc_f = str(row['tipo_c']) #2
#                         componente_f =componente_i  #3
#                         fase_f =regresa_i(row['fase'],l_fases) #4
#                         etapa_f = etapa_i  # 5
#                         tag_url = str(row['tag-url'])
#                         orden = int(row['orden'])
#                         existe_form = CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f)
#                         print (len(existe_form))
#                         if len(existe_form)==0:

#                             agrega_form = CatForm(
#                                 title = nombre_f,
#                                 tipo = tipo_f,
#                                 tipo_c = tipoc_f,
#                                 componente = componente_f,
#                                 fase = fase_f,
#                                 etapa =etapa_f,
#                                 nurl = tag_url,
#                                 orden=orden,
#                                                 )
#                             agrega_form.save()

#                     elif row['tipo_c']== 5 and componente_i.t_base == True and componente_i.t_aprov_lineal == True:  
#                         nombre_f = row['nombre'] #0
#                         tipo_f = str(row['tipo']) #1
#                         tipoc_f = str(row['tipo_c']) #2
#                         componente_f =componente_i  #3
#                         fase_f =regresa_i(row['fase'],l_fases) #4
#                         etapa_f = etapa_i  # 5
#                         tag_url = str(row['tag-url'])
#                         orden = int(row['orden'])
#                         existe_form = CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f)
#                         print (len(existe_form))
#                         if len(existe_form)==0:

#                             agrega_form = CatForm(
#                                 title = nombre_f,
#                                 tipo = tipo_f,
#                                 tipo_c = tipoc_f,
#                                 componente = componente_f,
#                                 fase = fase_f,
#                                 etapa =etapa_f,
#                                 nurl = tag_url,
#                                 orden=orden,
#                                                 )
#                             agrega_form.save()
            
#     return HttpResponse("estructura creada")

# Create your views here.


