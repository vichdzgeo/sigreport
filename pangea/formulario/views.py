# -*- coding: utf-8 -*-
from django.views.generic.edit import CreateView,UpdateView,DeleteView, FormMixin
from django.contrib.admin.views.decorators import staff_member_required
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
import pandas as pd 
from django.conf import settings
import os 
from django.http import HttpResponse
def regresa(key,modelo):
    for i in objetos:
        if i.title == key:
            return i.id
        


def regresa_instancia_id(key,modelo):
    objetos = modelo.objects.all()

    for i in objetos:
        if i.id == int(key):
            return i


###### Descripción de procesos constructivos
@method_decorator(login_required,name='dispatch')
class DescripcionProcesosConstructivosListView(ListView):
    model = DescripcionProcesosConstructivos
    template_name = "formulario/descripcionprocesosconstructivos_list.html"
    paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        context['id_f']=this_id
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_title']=DescripcionProcesosConstructivos._meta.verbose_name
        context['p_componente']=id_form.componente
        context['p_fase']=id_form.fase
        context['p_etapa']= id_form.etapa
        
        return context

@method_decorator(login_required,name='dispatch')
class DescripcionProcesosConstructivosCreate(CreateView):
    
    model = DescripcionProcesosConstructivos
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['id_f']=this_id
        context['p_title']=DescripcionProcesosConstructivos._meta.verbose_name
        context['p_componente']=id_form.componente.title
        context['p_fase']=id_form.fase.title
        context['p_etapa']= id_form.etapa.title
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=DescripcionProcesosConstructivosForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        return  reverse_lazy('forms:descprocesos',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class DescripcionProcesosConstructivosUpdate(UpdateView):
    model = DescripcionProcesosConstructivos
    form_class = DescripcionProcesosConstructivosForm
    template_name_suffix = '_update_form'
    

    def get_success_url(self):
        return reverse_lazy('forms:descprocesos-update',args=[self.object.id]) + '?ok'



##### Selección de sistemas constructivos 

@method_decorator(login_required,name='dispatch')
class SeleccionSistemasConstructivosCreate(CreateView):
    
    model = SeleccionSistemasConstructivos
    fields = '__all__'
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
        return  reverse_lazy('forms:selecsistemas',args=[this_id]) + '?ok'

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
    

    def get_success_url(self):
        return reverse_lazy('forms:selecsistemas-update',args=[self.object.id]) + '?ok'


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
    #form_class = FormLocalizacionC
    fields = '__all__'
    #success_url = reverse_lazy('forms:actividad-create')
    


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
    #form_class = FormLocalizacionC
    fields = '__all__'
    #success_url = reverse_lazy('forms:actividad-create')
    


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
    #form_class = FormLocalizacionC
    fields = '__all__'
    #success_url = reverse_lazy('forms:actividad-create')
    


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
    #form_class = FormLocalizacionC
    fields = '__all__'
    #success_url = reverse_lazy('forms:actividad-create')
    


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
    #form_class = FormLocalizacionC
    fields = '__all__'
    #success_url = reverse_lazy('forms:actividad-create')
    


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
    #form_class = FormLocalizacionC
    fields = '__all__'
    #success_url = reverse_lazy('forms:actividad-create')
    


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
    #form_class = FormLocalizacionC
    fields = '__all__'
    #success_url = reverse_lazy('forms:actividad-create')
    


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
        return  reverse_lazy('forms:maquinaria',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class MaquinariaZonificacionUpdate(UpdateView):
    model = MaquinariaZonificacion
    form_class = MaquinariaZonificacionForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('forms:maquinaria-update',args=[self.object.id]) + '?ok'






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
    fields = '__all__'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR

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
        context['f_id']= this_id
        
        context['descripcionfiguras']= DescripcionGeneralFiguras.objects.all()
        context['txt_exitoso']='Agregado correctamente. Puedes agregar otro registro si lo requieres'
        initial_data = {'componente':id_form.componente.id,'fase':id_form.fase.id,"etapa":id_form.etapa.id}
        context['form']=DescripcionGeneralForm(initial=initial_data)
        return context

    def get_success_url(self):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = CatForm.objects.filter(id=this_id)[0]
        return  reverse_lazy('forms:generales-list',args=[this_id]) + '?ok'

@method_decorator(login_required,name='dispatch')
class DescripcionGeneralUpdate(UpdateView):
    model = DescripcionGeneral
    form_class = DescripcionGeneralForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_element = DescripcionGeneral.objects.filter(id=this_id)[0] #NO MODIFICAR
        context['p_componente']=id_element.componente.title
        context['p_fase']=id_element.fase.title
        context['p_etapa']= id_element.etapa.title
        context['f_id']= this_id
        context['p_title']=DescripcionGeneral._meta.verbose_name
        context['descripcionfiguras']= DescripcionGeneralFiguras.objects.all()
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
    #form_class = FormLocalizacionC
    fields = '__all__'
    #success_url = reverse_lazy('forms:actividad-create')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_lugar =str(self.request.get_full_path()).split("/")[-3]
        if this_lugar == 'generalesfiguras':
            this_id =  int(str(self.request.get_full_path()).split("/")[-2])
            id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
        elif this_lugar == 'generalesfigurasu':
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
        this_lugar =str(self.request.get_full_path()).split("/")[-3]
        if this_lugar == 'generalesfiguras':
            this_id =  int(str(self.request.get_full_path()).split("/")[-2])
            id_form = CatForm.objects.filter(id=this_id)[0] #NO MODIFICAR
            return  reverse_lazy('forms:generalesfiguras',args=[this_id]) + '?ok'
        elif this_lugar == 'generalesfigurasu':
            this_id =  int(str(self.request.get_full_path()).split("/")[-2])
            id_form = DescripcionGeneral.objects.filter(id=this_id)[0]

            return  reverse_lazy('forms:generalesfigurasu',args=[this_id]) + '?ok'


@method_decorator(login_required,name='dispatch')
class DescripcionGeneralFigurasUpdate(UpdateView):
    model = DescripcionGeneralFiguras
    form_class = DescripcionGeneralFigurasForm
    template_name_suffix = '_update_form'
    

    def get_success_url(self):
        return reverse_lazy('forms:generalesfiguras-update',args=[self.object.id]) + '?ok'


###### FRECUENCIA DE ACTIVIDADES


    
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


@method_decorator(login_required,name='dispatch')
class FrecuenciaActividadesCUpdate(UpdateView):
    model = FrecuenciaActividadesC
    form_class = FrecuenciaActividadesCForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('forms:actividad-update',args=[self.object.id]) + '?ok'

#### LOCALIZACION

@method_decorator(login_required,name='dispatch')
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
        return  reverse_lazy('forms:fig-loc',args=[this_id]) + '?ok'

login_required
#@method_decorator(login_required,name='dispatch')
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
        
        return context





@method_decorator(login_required,name='dispatch')
class LocalizacionCUpdate(UpdateView):
    model = ImagenLocalizacionC
    form_class = FormLocalizacionC
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('forms:fig-update',args=[self.object.id]) + '?ok'


## Confirmación de formularios
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
            context['txt_actualizacion']="Estado del formualario: completo y validado"
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
        context['componentes'] = Modulo.objects.all()
        context['fases'] = Fase.objects.all().order_by('title')
        context['etapas'] = Etapa.objects.all().order_by('id').reverse()
        context['avances'] = CatForm.objects.all().order_by('title')
        context['completados'] = len(CatForm.objects.filter(completo=True))
        context['totales'] = len(CatForm.objects.values_list('title',))
        if context['totales']!=0:
            context['porcentaje'] = str((context['completados']/ context['totales'])*100)
        else:
            context['porcentaje'] = 0
        return context



def regresa(key,objetos):

    for i in objetos:
        if i.title == key:
            return i

def regresa_i(key,objetos):
    for i in objetos:
        if i.title == key:
            return i


def agregar_estructura(request):
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'estructura_arbol_form2.txt')
    estructura = pd.read_csv(file_path, delimiter='\t',encoding='utf-8')
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
                    fase_f =regresa_i(row['fase'],l_fases) #4
                    etapa_f = etapa_i  # 5
                    tag_url = str(row['tag-url'])
                    orden = int(row['orden'])

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
                            orden=orden,
                                            )
                        agrega_form.save()
                
                elif row['tipo_c']== 2 and componente_i.t_base == True and componente_i.t_aprov_edificable == True:  
                    nombre_f = row['nombre'] #0
                    tipo_f = str(row['tipo']) #1
                    tipoc_f = str(row['tipo_c']) #2
                    componente_f =componente_i  #3
                    fase_f =regresa_i(row['fase'],l_fases) #4
                    etapa_f = etapa_i  # 5
                    tag_url = str(row['tag-url'])
                    orden = int(row['orden'])
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
                            orden=orden,
                                            )
                        agrega_form.save()

                elif row['tipo_c']== 3 and componente_i.t_base == True and componente_i.t_obras == True:  
                    nombre_f = row['nombre'] #0
                    tipo_f = str(row['tipo']) #1
                    tipoc_f = str(row['tipo_c']) #2
                    componente_f =componente_i  #3
                    fase_f =regresa_i(row['fase'],l_fases) #4
                    etapa_f = etapa_i  # 5
                    tag_url = str(row['tag-url'])
                    orden = int(row['orden'])
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
                            orden=orden,
                                            )
                        agrega_form.save()

                elif row['tipo_c']== 4 and componente_i.t_base == True and componente_i.t_areas_verdes == True:  
                    nombre_f = row['nombre'] #0
                    tipo_f = str(row['tipo']) #1
                    tipoc_f = str(row['tipo_c']) #2
                    componente_f =componente_i  #3
                    fase_f =regresa_i(row['fase'],l_fases) #4
                    etapa_f = etapa_i  # 5
                    tag_url = str(row['tag-url'])
                    orden = int(row['orden'])
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
                            orden=orden,
                                            )
                        agrega_form.save()

                elif row['tipo_c']== 5 and componente_i.t_base == True and componente_i.t_aprov_lineal == True:  
                    nombre_f = row['nombre'] #0
                    tipo_f = str(row['tipo']) #1
                    tipoc_f = str(row['tipo_c']) #2
                    componente_f =componente_i  #3
                    fase_f =regresa_i(row['fase'],l_fases) #4
                    etapa_f = etapa_i  # 5
                    tag_url = str(row['tag-url'])
                    orden = int(row['orden'])
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
                            orden=orden,
                                            )
                        agrega_form.save()
            
            
    return HttpResponse("estructura creada")

# Create your views here.


