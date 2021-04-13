from django.shortcuts import render
from .models import *
from cap2.models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic import TemplateView
from .forms import *
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(staff_member_required,name='dispatch')
class CatalogosPageView(TemplateView):
    template_name = "miscelanea/catalogos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_componentes']=len(Modulo.objects.all().order_by('title'))
        context['num_macquina']=len(Maquina.objects.all().order_by('tipo'))
        context['num_unidades']=len(Unidad.objects.all().order_by('title'))
        context['num_edificios']=len(EdificacionProvisional.objects.all().order_by('title'))
        context['num_actividades']=len(ActividadProvisional.objects.all().order_by('title'))
        
        return context

#### -- PARA MODULOS - ######
class ModuloListView(ListView):
    model = Modulo
    template_name = "miscelanea/modulo_list.html"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Lista de componentes"
        
        return context

class ModuloCreate(CreateView):
    model = Modulo
    form_class = ModuloForm
    success_url = reverse_lazy('catalogos:componenetes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Agregar componente"
        return context

@method_decorator(staff_member_required,name='dispatch')
class ModuloUpdate(UpdateView):
    model = Modulo
    form_class = ModuloForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar componente"
        context['txt_actualizacion']="Componente  actualizado correctamente"
        return context
    
    def get_success_url(self):

        return reverse_lazy('catalogos:componente-update',args=[self.object.id]) + '?ok'




### Maquinas
@method_decorator(staff_member_required,name='dispatch')
class MaquinaListView(ListView):
    model = Maquina
    template_name = "miscelanea/maquina_list.html"
    paginate_by = 20

@method_decorator(staff_member_required,name='dispatch')
class MaquinaCreate(CreateView):
    model = Maquina
    form_class = MaquinaForm
    success_url = reverse_lazy('catalogos:maquinas')

@method_decorator(staff_member_required,name='dispatch')
class MaquinaUpdate(UpdateView):
    model = Maquina
    form_class = MaquinaForm
    template_name_suffix = '_update_form'
    
    
    def get_success_url(self):

        return reverse_lazy('catalogos:maquina-update',args=[self.object.id]) + '?ok'

## unidades

@method_decorator(staff_member_required,name='dispatch')
class UnidadListView(ListView):
    model = Unidad
    template_name = "miscelanea/unidad_list.html"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Lista de unidades"
        
        return context
@method_decorator(staff_member_required,name='dispatch')
class UnidadCreate(CreateView):
    model = Unidad
    form_class = UnidadForm
    success_url = reverse_lazy('catalogos:unidades')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Agregar unidad"
        return context

@method_decorator(staff_member_required,name='dispatch')
class UnidadUpdate(UpdateView):
    model = Unidad
    form_class = UnidadForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar unidad"
        context['txt_actualizacion']="Unidad actualizada correctamente"
        return context
    
    def get_success_url(self):

        return reverse_lazy('catalogos:unidad-update',args=[self.object.id]) + '?ok'


## Edificacion Provisional

@method_decorator(staff_member_required,name='dispatch')
class EdiProvisionalListView(ListView):
    model = EdificacionProvisional
    template_name = "miscelanea/edificacionprovisional_list.html"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Lista de edificaciones provisionales"
        
        return context

@method_decorator(staff_member_required,name='dispatch')

class EdiProvisionalCreate(CreateView):
    model = EdificacionProvisional
    form_class = EdificacionProvisionalForm
    success_url = reverse_lazy('catalogos:edificaciones')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Agregar edificación"
        return context

@method_decorator(staff_member_required,name='dispatch')
class EdiProvisionalUpdate(UpdateView):
    model = EdificacionProvisional
    form_class = EdificacionProvisionalForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar edificación"
        context['txt_actualizacion']="Edificación actualizada correctamente"
        return context
    
    def get_success_url(self):

        return reverse_lazy('catalogos:edificio-update',args=[self.object.id]) + '?ok'

## Actividad Provisional

@method_decorator(staff_member_required,name='dispatch')
class ActProvisionalListView(ListView):
    model = ActividadProvisional
    template_name = "miscelanea/actividadprovisional_list.html"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Lista de actividades provisionales"
        
        return context

@method_decorator(staff_member_required,name='dispatch')

class ActProvisionalCreate(CreateView):
    model = ActividadProvisional
    form_class = ActividadProvisionalForm
    success_url = reverse_lazy('catalogos:actividades')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Agregar actividad"
        return context

@method_decorator(staff_member_required,name='dispatch')
class ActProvisionalUpdate(UpdateView):
    model = ActividadProvisional
    form_class = ActividadProvisionalForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar actividad"
        context['txt_actualizacion']="Actividad provisional actualizada correctamente"
        return context
    
    def get_success_url(self):

        return reverse_lazy('catalogos:actividad-update',args=[self.object.id]) + '?ok'