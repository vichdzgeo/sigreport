from django.shortcuts import render
from .models import *
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
        context['num_macquina']=len(Maquina.objects.all().order_by('tipo'))
        
        return context

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