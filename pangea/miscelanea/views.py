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
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required,name='dispatch')
class CatalogosPageView(TemplateView):
    template_name = "miscelanea/catalogos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_etapas']=len(Etapa.objects.all())
        context['num_componentes']=len(Modulo.objects.all())
        context['fases']=[x.title for x in Fase.objects.all()]
        context['num_tiposv']=len(ListaTipoVehiculo.objects.all())
        context['num_vehiculos']=len(VehiculoPorTipo.objects.all())
        context['num_insespeciales']=len(ListInsEsp.objects.all())
        context['num_resespeciales']=len(ResiduosPeligrosos.objects.all())
        context['num_plantas_trata']=len(ListaPTAR.objects.all())
        context['num_macquina']=len(Maquina.objects.all())
        context['num_unidades']=len(Unidad.objects.all())
        context['num_edificios']=len(EdificacionProvisional.objects.all())
        context['num_actividades']=len(ActividadProvisional.objects.all())
        context['num_insumos']=len(InsumosLista.objects.all())
        context['num_quimicas']=len(SustanciasQuimicasP.objects.all())
        context['num_flores']=len(ListadoFloristico.objects.all())
        context['num_personal']=len(ListaTipoPersonal.objects.all())
        context['num_descsistemas']=len(SisConstructivo.objects.all())
        context['num_procesos']=len(ProcConstructivo.objects.all())
        context['num_residuossol']=len(ListaTipoResiduosSolidos.objects.all())
        context['num_residuos']=len(ListaTipoResiduos.objects.all())
        context['num_tagua']=len(TipoAgua.objects.all())
        context['num_tagresidual']=len(TipoAguaResidual.objects.all())
        context['num_aprovechamiento']=len(ListaTiposAprovechamiento.objects.all())
        context['num_cobertura']=len(ListaTiposCobertura.objects.all())
        context['num_zona']=len(ListaZonificacion.objects.all())
        context['num_tierra']=len(MovimientoTierra.objects.all())
        context['num_consedi']=len(ListaTiposConsEdif.objects.all())
        context['num_obraslineales']=len(ObrasLineales.objects.all())
        context['num_act_fase']=len(ListaActividades.objects.all())
        context['num_actcom']=len(ListaAct_scrc.objects.all())
        context['num_actvis']=len(ListActVisitantes.objects.all())
        context['num_areasmanejo']=len(ListaAreasManejoPeligrosas.objects.all())
        context['num_actesp']=len(ListaActInsEsp.objects.all())
        
        return context



##### --- GENERALES --- ####
#### -- PARA etapas - ######
@method_decorator(login_required,name='dispatch')
class EtapaListView(ListView):
    model = Etapa
    template_name = "miscelanea/etapa_list.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Lista de etapas"
        
        return context

@method_decorator(login_required,name='dispatch')
class EtapaCreate(CreateView):
    model = Etapa
    form_class = EtapaForm
    success_url = reverse_lazy('catalogos:etapas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Agregar etapa"
        return context

@method_decorator(login_required,name='dispatch')
class EtapaUpdate(UpdateView):
    model = Etapa
    form_class = EtapaForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar etapa"
        context['txt_actualizacion']="Etapa  actualizada correctamente"
        return context
    
    def get_success_url(self):

        return reverse_lazy('catalogos:etapas')




#### -- PARA COMPONENTES - ######
@method_decorator(login_required,name='dispatch')
class ModuloListView(ListView):
    model = Modulo
    template_name = "miscelanea/modulo_list.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Lista de componentes"
        
        return context

@method_decorator(login_required,name='dispatch')
class ModuloCreate(CreateView):
    model = Modulo
    form_class = ModuloForm
    success_url = reverse_lazy('catalogos:componentes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Agregar componente"
        return context

@method_decorator(login_required,name='dispatch')
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

## unidades

@method_decorator(login_required,name='dispatch')
class UnidadListView(ListView):
    model = Unidad
    template_name = "miscelanea/unidad_list.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Lista de unidades"
        
        return context
@method_decorator(login_required,name='dispatch')
class UnidadCreate(CreateView):
    model = Unidad
    form_class = UnidadForm
    success_url = reverse_lazy('catalogos:unidades')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Agregar unidad"
        return context

@method_decorator(login_required,name='dispatch')
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


## Tipos de vehículos
@method_decorator(login_required,name='dispatch')
class ListaTipoVehiculoListView(ListView):
    model = ListaTipoVehiculo
    template_name = "miscelanea/listatipovehiculo_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
      
        return context

@method_decorator(login_required,name='dispatch')
class ListaTipoVehiculoCreate(CreateView):
    model =ListaTipoVehiculo
    form_class =ListaTipoVehiculoForm
    template_name = "miscelanea/listatipovehiculo_form.html"
    success_url = reverse_lazy('catalogos:tiposv')

@method_decorator(login_required,name='dispatch')
class ListaTipoVehiculoUpdate(UpdateView):
    model =ListaTipoVehiculo
    form_class =ListaTipoVehiculoForm
    template_name_suffix = '_update_form'
    
    
    def get_success_url(self):

        return reverse_lazy('catalogos:tipov-update',args=[self.object.id]) + '?ok'
## Vehículos por tipo
@method_decorator(login_required,name='dispatch')
class VehiculoPorTipoListView(ListView):
    model = VehiculoPorTipo
    template_name = "miscelanea/vehiculoportipo_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Lista de vehículos por tipo"
        context['crear']='catalogos:vehiculo-create'
        context['actualizar']='catalogos:vehiculo-update'
        campos_exc = ['id','created','updated']

        context['campos']=[field.verbose_name for field in VehiculoPorTipo._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in VehiculoPorTipo._meta.concrete_fields if field.name not in campos_exc]
        return context

@method_decorator(login_required,name='dispatch')
class VehiculoPorTipoCreate(CreateView):
    model =VehiculoPorTipo
    form_class =VehiculoPorTipoForm
    template_name = "miscelanea/vehiculoportipo_form.html"
    success_url = reverse_lazy('catalogos:vehiculos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Agregar vehículo"
        return context


@method_decorator(login_required,name='dispatch')
class VehiculoPorTipoUpdate(UpdateView):
    model =VehiculoPorTipo
    form_class =VehiculoPorTipoForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar vehículo"
        context['regresar']='catalogos:vehiculos'
        context['txt_actualizacion']="Vehículo actualizado correctamente"
        return context
    def get_success_url(self):

        return reverse_lazy('catalogos:vehiculo-update',args=[self.object.id]) + '?ok'


## Instalación especial

@method_decorator(login_required,name='dispatch')
class ListInsEspListView(ListView):
    model = ListInsEsp
    template_name = "miscelanea/listsnsesp_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=self.model._meta.verbose_name
        context['crear']='catalogos:iespecial-create'
        context['actualizar']='catalogos:iespecial-update'
        campos_exc = ['id','created','updated']
        context['campos']=[field.verbose_name for field in ListInsEsp._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in ListInsEsp._meta.concrete_fields if field.name not in campos_exc]
        return context

@method_decorator(login_required,name='dispatch')
class ListInsEspCreate(CreateView):
    model =ListInsEsp
    form_class =ListInsEspForm
    template_name = "miscelanea/listinsesp_form.html"
    success_url = reverse_lazy('catalogos:ins-especiales')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Agregar Instalación"
        return context


@method_decorator(login_required,name='dispatch')
class ListInsEspUpdate(UpdateView):
    model =ListInsEsp
    form_class =ListInsEspForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar Instalación"
        context['regresar']='catalogos:ins-especiales'
        context['txt_actualizacion']="Instalación actualizada correctamente"
        return context
    def get_success_url(self):

        return reverse_lazy('catalogos:iespecial-update',args=[self.object.id]) + '?ok'



## Tipos de agua

@method_decorator(login_required,name='dispatch')
class TipoAguaListView(ListView):
    model = TipoAgua
    template_name = "miscelanea/tipoagua_list.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=TipoAgua._meta.verbose_name
        
        return context

@method_decorator(login_required,name='dispatch')

class TipoAguaCreate(CreateView):
    model = TipoAgua
    form_class = TipoAguaForm
    success_url = reverse_lazy('catalogos:tagua')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=TipoAgua._meta.verbose_name
        return context

@method_decorator(login_required,name='dispatch')
class TipoAguaUpdate(UpdateView):
    model = TipoAgua
    form_class = TipoAguaForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar"
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    
    def get_success_url(self):

        return reverse_lazy('catalogos:tagua-update',args=[self.object.id]) + '?ok'

## Tipos de agua residual
@method_decorator(login_required,name='dispatch')
class TipoAguaResidualListView(ListView):
    model = TipoAguaResidual
    template_name = "miscelanea/tipoaguaresidual_list.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=TipoAguaResidual._meta.verbose_name
        
        return context

@method_decorator(login_required,name='dispatch')
class TipoAguaResidualCreate(CreateView):
    model = TipoAguaResidual
    form_class = TipoAguaResidualForm
    success_url = reverse_lazy('catalogos:tagresidual')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=TipoAguaResidual._meta.verbose_name
        return context

@method_decorator(login_required,name='dispatch')
class TipoAguaResidualUpdate(UpdateView):
    model = TipoAguaResidual
    form_class = TipoAguaResidualForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar"
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    
    def get_success_url(self):

        return reverse_lazy('catalogos:tagresidual-update',args=[self.object.id]) + '?ok'

## Tipos de cobertura
@method_decorator(login_required,name='dispatch')
class ListaTiposCoberturaListView(ListView):
    model = ListaTiposCobertura
    template_name = "miscelanea/listatiposcobertura_list.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=ListaTiposCobertura._meta.verbose_name
        
        return context

@method_decorator(login_required,name='dispatch')
class ListaTiposCoberturaCreate(CreateView):
    model = ListaTiposCobertura
    form_class = ListaTiposCoberturaForm
    success_url = reverse_lazy('catalogos:cobertura')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=ListaTiposCobertura._meta.verbose_name
        return context

@method_decorator(login_required,name='dispatch')
class ListaTiposCoberturaUpdate(UpdateView):
    model = ListaTiposCobertura
    form_class = ListaTiposCoberturaForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar"
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    
    def get_success_url(self):

        return reverse_lazy('catalogos:cobertura-update',args=[self.object.id]) + '?ok'

## Tipos zonificación
@method_decorator(login_required,name='dispatch')
class ListaZonificacionListView(ListView):
    model = ListaZonificacion
    template_name = "miscelanea/listazonificacion_list.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=ListaZonificacion._meta.verbose_name
        
        return context

@method_decorator(login_required,name='dispatch')
class ListaZonificacionCreate(CreateView):
    model = ListaZonificacion
    form_class = ListaZonificacionForm
    success_url = reverse_lazy('catalogos:zona')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=ListaZonificacion._meta.verbose_name
        return context

@method_decorator(login_required,name='dispatch')
class ListaZonificacionUpdate(UpdateView):
    model = ListaZonificacion
    form_class = ListaZonificacionForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar"
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    
    def get_success_url(self):

        return reverse_lazy('catalogos:zona-update',args=[self.object.id]) + '?ok'


## Insumos lista

@method_decorator(login_required,name='dispatch')
class InsumosListaListView(ListView):
    model = InsumosLista
    template_name = "miscelanea/insumoslista_list.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=InsumosLista._meta.verbose_name
        
        return context

@method_decorator(login_required,name='dispatch')

class InsumosListaCreate(CreateView):
    model = InsumosLista
    form_class = InsumosListaForm
    success_url = reverse_lazy('catalogos:insumos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=InsumosLista._meta.verbose_name
        return context

@method_decorator(login_required,name='dispatch')
class InsumosListaUpdate(UpdateView):
    model = InsumosLista
    form_class = InsumosListaForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar"
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    
    def get_success_url(self):

        return reverse_lazy('catalogos:insumo-update',args=[self.object.id]) + '?ok'
## Sustancias quimicas

@method_decorator(login_required,name='dispatch')
class SustanciasQuimicasPListView(ListView):
    model = SustanciasQuimicasP
    template_name = "miscelanea/sustanciasquimicasp_list.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=SustanciasQuimicasP._meta.verbose_name
        
        return context

@method_decorator(login_required,name='dispatch')

class SustanciasQuimicasPCreate(CreateView):
    model = SustanciasQuimicasP
    form_class = SustanciasQuimicasPForm
    success_url = reverse_lazy('catalogos:quimicas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=SustanciasQuimicasP._meta.verbose_name
        return context

@method_decorator(login_required,name='dispatch')
class SustanciasQuimicasPUpdate(UpdateView):
    model = SustanciasQuimicasP
    form_class = SustanciasQuimicasPForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar"
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    
    def get_success_url(self):

        return reverse_lazy('catalogos:quimica-update',args=[self.object.id]) + '?ok'
## ListaTipoPersonal

@method_decorator(login_required,name='dispatch')
class  ListaTipoPersonalListView(ListView):
    model =  ListaTipoPersonal
    template_name = "miscelanea/listatipopersonal_list.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=ListaTipoPersonal._meta.verbose_name
        
        return context

@method_decorator(login_required,name='dispatch')
class  ListaTipoPersonalCreate(CreateView):
    model = ListaTipoPersonal
    form_class = ListaTipoPersonalForm
    success_url = reverse_lazy('catalogos:personal')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Agregar"
        return context



@method_decorator(login_required,name='dispatch')
class  ListaTipoPersonalUpdate(UpdateView):
    model =  ListaTipoPersonal
    form_class =  ListaTipoPersonalForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar"
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    
    def get_success_url(self):

        return reverse_lazy('catalogos:personal-update',args=[self.object.id]) + '?ok'

## Tipos de residuos solidos

@method_decorator(login_required,name='dispatch')
class ListaTipoResiduosSolidosListView(ListView):
    model = ListaTipoResiduosSolidos
    template_name = "miscelanea/listatiporesiduossolidos_list.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=ListaTipoResiduosSolidos._meta.verbose_name
        
        return context

@method_decorator(login_required,name='dispatch')

class ListaTipoResiduosSolidosCreate(CreateView):
    model = ListaTipoResiduosSolidos
    form_class = ListaTipoResiduosSolidosForm
    template_name = "miscelanea/listatiporesiduos_form.html"
    paginate_by = 100
    success_url = reverse_lazy('catalogos:residuossolidos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=ListaTipoResiduosSolidos._meta.verbose_name
        return context

@method_decorator(login_required,name='dispatch')
class ListaTipoResiduosSolidosUpdate(UpdateView):
    model = ListaTipoResiduosSolidos
    form_class = ListaTipoResiduosSolidosForm 
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar"
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    
    def get_success_url(self):

        return reverse_lazy('catalogos:residuossolidos-update',args=[self.object.id]) + '?ok'


## Tipos de residuos tóxicos

@method_decorator(login_required,name='dispatch')
class ListaTipoResiduosListView(ListView):
    model = ListaTipoResiduos
    template_name_suffix = '_update_form'
    template_name = "miscelanea/listatiporesiduos_list.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=ListaTipoResiduos._meta.verbose_name
        
        return context

@method_decorator(login_required,name='dispatch')

class ListaTipoResiduosCreate(CreateView):
    model = ListaTipoResiduos
    form_class = ListaTipoResiduosForm
    success_url = reverse_lazy('catalogos:residuos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=ListaTipoResiduos._meta.verbose_name
        return context

@method_decorator(login_required,name='dispatch')
class ListaTipoResiduosUpdate(UpdateView):
    model = ListaTipoResiduos
    form_class = ListaTipoResiduosForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar"
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    
    def get_success_url(self):

        return reverse_lazy('catalogos:residuo-update',args=[self.object.id]) + '?ok'


## Actividades 

@method_decorator(login_required,name='dispatch')
class ListaActividadesListView(ListView):
    model = ListaActividades
    template_name = "miscelanea/listaactividades_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=self.model._meta.verbose_name
        context['crear']='catalogos:act-create'
        context['actualizar']='catalogos:act-update'
        campos_exc = ['id','created','updated']
        context['campos']=[field.verbose_name for field in ListaActividades._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in ListaActividades._meta.concrete_fields if field.name not in campos_exc]
        return context

@method_decorator(login_required,name='dispatch')
class ListaActividadesCreate(CreateView):
    model =ListaActividades
    form_class =ListaActividadesForm
    template_name = "miscelanea/template_form.html"
    success_url = reverse_lazy('catalogos:act-fase')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Agregar Actividad"
        context['regresar']='catalogos:act-fase'
        return context


@method_decorator(login_required,name='dispatch')
class ListaActividadesUpdate(UpdateView):
    model =ListaActividades
    form_class =ListaActividadesForm
    template_name = "miscelanea/template_update_form.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar actividad"
        context['regresar']='catalogos:act-fase'
        context['txt_actualizacion']="Actividad actualizada correctamente"
        return context
    def get_success_url(self):

        return reverse_lazy('catalogos:act-update',args=[self.object.id]) + '?ok'
## Residuos peligrosos por instalación especial 

@method_decorator(login_required,name='dispatch')
class ResiduosPeligrososListView(ListView):
    model = ResiduosPeligrosos
    template_name = "miscelanea/residuospeligrosos_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=self.model._meta.verbose_name
        context['crear']='catalogos:resespecial-create'
        context['actualizar']='catalogos:resespecial-update'
        campos_exc = ['id','created','updated']
        context['campos']=[field.verbose_name for field in ResiduosPeligrosos._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in ResiduosPeligrosos._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        return context

@method_decorator(login_required,name='dispatch')
class ResiduosPeligrososCreate(CreateView):
    model =ResiduosPeligrosos
    form_class =ResiduosPeligrososForm
    template_name = "miscelanea/template_form.html"
    success_url = reverse_lazy('catalogos:resespecial')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Agregar residuo peligroso"
        context['regresar']='catalogos:resespecial'
        return context


@method_decorator(login_required,name='dispatch')
class ResiduosPeligrososUpdate(UpdateView):
    model =ResiduosPeligrosos
    form_class =ResiduosPeligrososForm
    template_name = "miscelanea/template_update_form.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar residuo"
        context['regresar']='catalogos:resespecial'
        context['txt_actualizacion']="Residuo actualizado correctamente"
        return context
    def get_success_url(self):

        return reverse_lazy('catalogos:resespecial-update',args=[self.object.id]) + '?ok'
## Plantas de tratamiento

@method_decorator(login_required,name='dispatch')
class ListaPTARListView(ListView):
    model = ListaPTAR
    template_name = "miscelanea/listaptar_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=self.model._meta.verbose_name
        context['crear']='catalogos:ptrata-create'
        context['actualizar']='catalogos:ptrata-update'
        campos_exc = ['id','created','updated']
        context['campos']=[field.verbose_name for field in ListaPTAR._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in ListaPTAR._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        return context

@method_decorator(login_required,name='dispatch')
class ListaPTARCreate(CreateView):
    model =ListaPTAR
    form_class =ListaPTARForm
    template_name = "miscelanea/template_form.html"
    success_url = reverse_lazy('catalogos:ptrata')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Agregar planta de tratamiento"
        context['regresar']='catalogos:ptrata'
        return context


@method_decorator(login_required,name='dispatch')
class ListaPTARUpdate(UpdateView):
    model =ListaPTAR
    form_class =ListaPTARForm
    template_name = "miscelanea/template_update_form.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar planta"
        context['regresar']='catalogos:ptrata'
        context['txt_actualizacion']="Planta actualizado correctamente"
        return context
    def get_success_url(self):

        return reverse_lazy('catalogos:ptrata-update',args=[self.object.id]) + '?ok'

###  TERMINA GENERALES ---------------------#####
###################################################

############# INICIA CONTRUCCIÓN ######################
##########################################################
### Maquinas
@method_decorator(login_required,name='dispatch')
class MaquinaListView(ListView):
    model = Maquina
    template_name = "miscelanea/maquina_list.html"
    paginate_by = 100

@method_decorator(login_required,name='dispatch')
class MaquinaCreate(CreateView):
    model = Maquina
    form_class = MaquinaForm
    success_url = reverse_lazy('catalogos:maquinas')

@method_decorator(login_required,name='dispatch')
class MaquinaUpdate(UpdateView):
    model = Maquina
    form_class = MaquinaForm
    template_name_suffix = '_update_form'
    
    
    def get_success_url(self):

        return reverse_lazy('catalogos:maquina-update',args=[self.object.id]) + '?ok'




## Obras lineales

@method_decorator(login_required,name='dispatch')
class ObrasLinealesListView(ListView):
    model = ObrasLineales
    template_name = "miscelanea/obraslineales_list.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=ObrasLineales._meta.verbose_name
        
        return context
@method_decorator(login_required,name='dispatch')
class ObrasLinealesCreate(CreateView):
    model = ObrasLineales
    form_class = ObrasLinealesForm
    success_url = reverse_lazy('catalogos:obraslineales')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Agregar obra lineal"
        return context

@method_decorator(login_required,name='dispatch')
class ObrasLinealesUpdate(UpdateView):
    model = ObrasLineales
    form_class = ObrasLinealesForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar"
        context['txt_actualizacion']="registro actualizado correctamente"
        return context
    
    def get_success_url(self):

        return reverse_lazy('catalogos:obraslineales-update',args=[self.object.id]) + '?ok'



## Edificacion Provisional

@method_decorator(login_required,name='dispatch')
class EdiProvisionalListView(ListView):
    model = EdificacionProvisional
    template_name = "miscelanea/edificacionprovisional_list.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=EdificacionProvisional._meta.verbose_name
        
        return context

@method_decorator(login_required,name='dispatch')
class EdiProvisionalCreate(CreateView):
    model = EdificacionProvisional
    form_class = EdificacionProvisionalForm
    success_url = reverse_lazy('catalogos:edificaciones')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Agregar edificación"
        return context

@method_decorator(login_required,name='dispatch')
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
@method_decorator(login_required,name='dispatch')
class ActProvisionalListView(ListView):
    model = ActividadProvisional
    template_name = "miscelanea/actividadprovisional_list.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Lista de actividades provisionales"
        
        return context

@method_decorator(login_required,name='dispatch')

class ActProvisionalCreate(CreateView):
    model = ActividadProvisional
    form_class = ActividadProvisionalForm
    success_url = reverse_lazy('catalogos:actividades')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Agregar actividad"
        return context

@method_decorator(login_required,name='dispatch')
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




## listado floristico

@method_decorator(login_required,name='dispatch')
class  ListadoFloristicoListView(ListView):
    model =  ListadoFloristico
    template_name = "miscelanea/listadofloristico_list.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=ListadoFloristico._meta.verbose_name
        
        return context

@method_decorator(login_required,name='dispatch')
class  ListadoFloristicoCreate(CreateView):
    model =  ListadoFloristico
    form_class = ListadoFloristicoForm
    success_url = reverse_lazy('catalogos:flores')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Agregar"
        return context



@method_decorator(login_required,name='dispatch')
class  ListadoFloristicoUpdate(UpdateView):
    model =  ListadoFloristico
    form_class =  ListadoFloristicoForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar"
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    
    def get_success_url(self):

        return reverse_lazy('catalogos:flor-update',args=[self.object.id]) + '?ok'




## PROCESOS constructivos

@method_decorator(login_required,name='dispatch')
class ListaProcesoConstructivoListView(ListView):
    model = ListaProcesoConstructivo
    template_name = "miscelanea/listaprocesoconstructivo_list.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=ListaProcesoConstructivo._meta.verbose_name
        
        return context

@method_decorator(login_required,name='dispatch')

class ListaProcesoConstructivoCreate(CreateView):
    model = ListaProcesoConstructivo
    form_class = ListaProcesoConstructivoForm
    success_url = reverse_lazy('catalogos:procesos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=ListaProcesoConstructivo._meta.verbose_name
        return context

@method_decorator(login_required,name='dispatch')
class ListaProcesoConstructivoUpdate(UpdateView):
    model = ListaProcesoConstructivo
    form_class = ListaProcesoConstructivoForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar"
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    
    def get_success_url(self):

        return reverse_lazy('catalogos:proceso-update',args=[self.object.id]) + '?ok'






## Tipos de aprovechamiento
@method_decorator(login_required,name='dispatch')
class ListaTiposAprovechamientoListView(ListView):
    model = ListaTiposAprovechamiento
    template_name = "miscelanea/listatiposaprovechamiento_list.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=ListaTiposAprovechamiento._meta.verbose_name
        
        return context

@method_decorator(login_required,name='dispatch')
class ListaTiposAprovechamientoCreate(CreateView):
    model = ListaTiposAprovechamiento
    form_class = ListaTiposAprovechamientoForm
    success_url = reverse_lazy('catalogos:aprovechamiento')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=ListaTiposAprovechamiento._meta.verbose_name
        return context

@method_decorator(login_required,name='dispatch')
class ListaTiposAprovechamientoUpdate(UpdateView):
    model = ListaTiposAprovechamiento
    form_class = ListaTiposAprovechamientoForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar"
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    
    def get_success_url(self):
        return reverse_lazy('catalogos:aprovechamiento-update',args=[self.object.id]) + '?ok'



## Tipos de movimienttos de tierra
@method_decorator(login_required,name='dispatch')
class MovimientoTierraListView(ListView):
    model = MovimientoTierra
    template_name = "miscelanea/movimientotierra_list.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=MovimientoTierra._meta.verbose_name
        
        return context

@method_decorator(login_required,name='dispatch')
class MovimientoTierraCreate(CreateView):
    model = MovimientoTierra
    form_class = MovimientoTierraForm
    success_url = reverse_lazy('catalogos:tierra')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=MovimientoTierra._meta.verbose_name
        return context

@method_decorator(login_required,name='dispatch')
class MovimientoTierraUpdate(UpdateView):
    model = MovimientoTierra
    form_class = MovimientoTierraForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar"
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    
    def get_success_url(self):

        return reverse_lazy('catalogos:tierra-update',args=[self.object.id]) + '?ok'

## Tipos de construcción y edificacion
@method_decorator(login_required,name='dispatch')
class ListaTiposConsEdifListView(ListView):
    model = ListaTiposConsEdif
    template_name = "miscelanea/listatiposconsedif_list.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=ListaTiposConsEdif._meta.verbose_name
        
        return context

@method_decorator(login_required,name='dispatch')
class ListaTiposConsEdifCreate(CreateView):
    model = ListaTiposConsEdif
    form_class = ListaTiposConsEdifForm
    success_url = reverse_lazy('catalogos:consedi')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=ListaTiposConsEdif._meta.verbose_name
        return context

@method_decorator(login_required,name='dispatch')
class ListaTiposConsEdifUpdate(UpdateView):
    model = ListaTiposConsEdif
    form_class = ListaTiposConsEdifForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar"
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    
    def get_success_url(self):

        return reverse_lazy('catalogos:consedi-update',args=[self.object.id]) + '?ok'

## Descripción de Procesos constructivos

@method_decorator(login_required,name='dispatch')
class ProcConstructivoListView(ListView):
    model = ProcConstructivo
    template_name = "miscelanea/procconstructivo_list.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=ProcConstructivo._meta.verbose_name
        
        return context

@method_decorator(login_required,name='dispatch')

class ProcConstructivoCreate(CreateView):
    model = ProcConstructivo
    form_class = ProcConstructivoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['n']=1
        context['p_title']=ProcConstructivo._meta.verbose_name
        return context

    def get_success_url(self):

        return reverse_lazy('catalogos:descproceso')

@method_decorator(login_required,name='dispatch')
class ProcConstructivoUpdate(UpdateView):
    model = ProcConstructivo
    form_class = ProcConstructivoForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super().get_context_data(**kwargs)
        context['p_title']=ProcConstructivo._meta.verbose_name
        context['sis_id']= context['object'].id
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    
    def get_success_url(self):

        return reverse_lazy('catalogos:descproceso')


## Descripción de Sistemas constructivos

@method_decorator(login_required,name='dispatch')
class SisConstructivoListView(ListView):
    model = SisConstructivo
    template_name = "miscelanea/sisconstructivo_list.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=SisConstructivo._meta.verbose_name
        
        return context

@method_decorator(login_required,name='dispatch')

class SisConstructivoCreate(CreateView):
    model = SisConstructivo
    form_class = SisConstructivoForm
    #success_url = reverse_lazy('catalogos:descsistema')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['n']=1
        context['p_title']=SisConstructivo._meta.verbose_name
        context['lasfiguras']= SisFiguras.objects.all()
        return context

    def get_success_url(self):

        return reverse_lazy('catalogos:descsistema')

@method_decorator(login_required,name='dispatch')
class SisConstructivoUpdate(UpdateView):
    model = SisConstructivo
    form_class = SisConstructivoForm
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super().get_context_data(**kwargs)
        context['p_title']=SisConstructivo._meta.verbose_name
        #context['sistemaTitle']="Actualizar"
        context['sis_id']= context['object'].id
        context['lasfiguras']= SisFiguras.objects.filter(sistema=context['object'])
        context['txt_actualizacion']="Registro actualizado correctamente"
        return context
    
    def get_success_url(self):

        return reverse_lazy('catalogos:descsistema')

########## figuras sistemas constructivos

@method_decorator(login_required,name='dispatch')
class SisFigurasCreate(CreateView):
    
    model = SisFiguras
    form_class = SisFigurasForm
    
    #success_url = reverse_lazy('forms:actividad-create')
    def form_valid(self, form):
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        this_sis = SisConstructivo.objects.filter(id=this_id)[0]
        form.instance.sistema = this_sis
        #form.instance.descripcion = self.request.
        return super(SisFigurasCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        this_sis = SisConstructivo.objects.filter(id=this_id)[0]
        context['titulo'] = this_sis.title
        initial_data = {'sistema':this_sis.id}
        context['f_id']=this_id
        print(context)
        context['form']=SisFigurasForm(initial=initial_data)
        return context

    def get_success_url(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_id =  int(str(self.request.get_full_path()).split("/")[-2])
        id_form = SisConstructivo.objects.filter(id=this_id)[0]
        return  reverse_lazy('catalogos:descsistema-update',args=[id_form.id,])



@method_decorator(login_required,name='dispatch')
class SisFigurasUpdate(UpdateView):
    model = SisFiguras
    form_class = SisFigurasForm
    template_name_suffix = '_update_form'
    

    def get_success_url(self):
        return reverse_lazy('miscelanea:sistemasfiguras-update',args=[self.object.id]) + '?ok'


###### FINALIZA CONTRUCCIÓN #######

###### COMIENZA OPERACIÓN #################

## actividades de servicios, comerciales, recreativas o culturales

@method_decorator(login_required,name='dispatch')
class ListaAct_scrcListView(ListView):
    model = ListaAct_scrc
    template_name = "miscelanea/listaact_scrc_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=self.model._meta.verbose_name
        context['crear']='catalogos:actservic-create'
        context['actualizar']='catalogos:actservic-update'
        campos_exc = ['id','created','updated']
        context['campos']=[field.verbose_name for field in ListaAct_scrc._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in ListaAct_scrc._meta.concrete_fields if field.name not in campos_exc]
        context['n_campos']=len(context['col'])
        return context

@method_decorator(login_required,name='dispatch')
class ListaAct_scrcCreate(CreateView):
    model =ListaAct_scrc
    form_class =ListaAct_scrcForm
    template_name = "miscelanea/template_form.html"
    success_url = reverse_lazy('catalogos:actservic')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Agregar actividad de sevicio, comercial, recreativa o cultural"
        context['regresar']='catalogos:actservic'
        return context


@method_decorator(login_required,name='dispatch')
class ListaAct_scrcUpdate(UpdateView):
    model =ListaAct_scrc
    form_class =ListaAct_scrcForm
    template_name = "miscelanea/template_update_form.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar planta"
        context['regresar']='catalogos:actservic'
        context['txt_actualizacion']="Actividad actualizada correctamente"
        return context
    def get_success_url(self):

        return reverse_lazy('catalogos:actservic-update',args=[self.object.id]) + '?ok'


## actividades de visitantes

@method_decorator(login_required,name='dispatch')
class ListActVisitantesListView(ListView):
    model = ListActVisitantes
    template_name = "miscelanea/listactvisitantes_list.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=self.model._meta.verbose_name
        context['crear']='catalogos:actvisita-create'
        context['actualizar']='catalogos:actvisita-update'
        campos_exc = ['id','created','updated','fase']
        context['campos']=[field.verbose_name for field in ListActVisitantes._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in ListActVisitantes._meta.concrete_fields if field.name not in campos_exc]
        
        return context

@method_decorator(login_required,name='dispatch')
class ListActVisitantesCreate(CreateView):
    model =ListActVisitantes
    form_class =ListActVisitantesForm
    template_name = "miscelanea/template_form.html"
    success_url = reverse_lazy('catalogos:actvisita')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Agregar actividad de visitante"
        context['regresar']='catalogos:actvisita'
        return context


@method_decorator(login_required,name='dispatch')
class ListActVisitantesUpdate(UpdateView):
    model =ListActVisitantes
    form_class =ListActVisitantesForm
    template_name = "miscelanea/template_update_form.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar actividad"
        context['regresar']='catalogos:actvisita'
        context['txt_actualizacion']="Actividad actualizada correctamente"
        return context
    def get_success_url(self):

        return reverse_lazy('catalogos:actvisita-update',args=[self.object.id]) + '?ok'

## áreas de manejo

@method_decorator(login_required,name='dispatch')
class ListaAreasManejoPeligrosasListView(ListView):
    model = ListaAreasManejoPeligrosas
    template_name = "miscelanea/areas_manejo.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=self.model._meta.verbose_name
        context['crear']='catalogos:areasm-create'
        context['actualizar']='catalogos:areasm-update'
        campos_exc = ['id','created','updated']
        context['campos']=[field.verbose_name for field in ListaAreasManejoPeligrosas._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in ListaAreasManejoPeligrosas._meta.concrete_fields if field.name not in campos_exc]
        
        return context

@method_decorator(login_required,name='dispatch')
class ListaAreasManejoPeligrosasCreate(CreateView):
    model =ListaAreasManejoPeligrosas
    form_class =ListaAreasManejoPeligrosasForm
    template_name = "miscelanea/template_form.html"
    success_url = reverse_lazy('catalogos:areasm')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Agregar área de manejo"
        context['regresar']='catalogos:areasm'
        return context


@method_decorator(login_required,name='dispatch')
class ListaAreasManejoPeligrosasUpdate(UpdateView):
    model =ListaAreasManejoPeligrosas
    form_class =ListaAreasManejoPeligrosasForm
    template_name = "miscelanea/template_update_form.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar área de manejo"
        context['regresar']='catalogos:areasm'
        context['txt_actualizacion']="Área de manejo actualizada correctamente"
        return context
    def get_success_url(self):

        return reverse_lazy('catalogos:areasm-update',args=[self.object.id]) + '?ok'

## actividades en instalaciones peligrosas

@method_decorator(login_required,name='dispatch')
class ListaActInsEspListView(ListView):
    model = ListaActInsEsp
    template_name = "miscelanea/actividades_instalaciones.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']=self.model._meta.verbose_name
        context['crear']='catalogos:actespeciales-create'
        context['actualizar']='catalogos:actespeciales-update'
        campos_exc = ['id','created','updated']
        context['campos']=[field.verbose_name for field in ListaActInsEsp._meta.concrete_fields if field.name not in campos_exc]
        context['col']=[field.name for field in ListaActInsEsp._meta.concrete_fields if field.name not in campos_exc]
        
        return context

@method_decorator(login_required,name='dispatch')
class ListaActInsEspCreate(CreateView):
    model =ListaActInsEsp
    form_class =ListaActInsEspForm
    template_name = "miscelanea/template_form.html"
    success_url = reverse_lazy('catalogos:actespeciales')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Agregar actividad en instalación especial"
        context['regresar']='catalogos:actespeciales'
        return context


@method_decorator(login_required,name='dispatch')
class ListaActInsEspUpdate(UpdateView):
    model =ListaActInsEsp
    form_class =ListaActInsEspForm
    template_name = "miscelanea/template_update_form.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p_title']="Actualizar actividad"
        context['regresar']='catalogos:actespeciales'
        context['txt_actualizacion']="Actividad actualizada correctamente"
        return context
    def get_success_url(self):

        return reverse_lazy('catalogos:actespeciales-update',args=[self.object.id]) + '?ok'

# ## Sustancias quimicas

# @method_decorator(login_required,name='dispatch')
# class SustanciasQuimicasPListView(ListView):
#     model = SustanciasQuimicasP
#     template_name = "miscelanea/sustanciasquimicasp_list.html"
#     paginate_by = 100

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['p_title']=SustanciasQuimicasP._meta.verbose_name
        
#         return context

# @method_decorator(login_required,name='dispatch')

# class SustanciasQuimicasPCreate(CreateView):
#     model = SustanciasQuimicasP
#     form_class = SustanciasQuimicasPForm
#     success_url = reverse_lazy('catalogos:quimicas')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['p_title']=SustanciasQuimicasP._meta.verbose_name
#         return context

# @method_decorator(login_required,name='dispatch')
# class SustanciasQuimicasPUpdate(UpdateView):
#     model = SustanciasQuimicasP
#     form_class = SustanciasQuimicasPForm
#     template_name_suffix = '_update_form'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['p_title']="Actualizar"
#         context['txt_actualizacion']="Registro actualizado correctamente"
#         return context
    
#     def get_success_url(self):

#         return reverse_lazy('catalogos:quimica-update',args=[self.object.id]) + '?ok'


## Sistemas constructivos

# @method_decorator(login_required,name='dispatch')
# class ListaSisConstructivoListView(ListView):
#     model = ListaSisConstructivo
#     template_name = "miscelanea/listasisconstructivo_list.html"
#     paginate_by = 100

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['p_title']=ListaSisConstructivo._meta.verbose_name
        
#         return context

# @method_decorator(login_required,name='dispatch')

# class ListaSisConstructivoCreate(CreateView):
#     model = ListaSisConstructivo
#     form_class = ListaSisConstructivoForm
#     success_url = reverse_lazy('catalogos:sistema')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['p_title']=ListaSisConstructivo._meta.verbose_name
#         return context

# @method_decorator(login_required,name='dispatch')
# class ListaSisConstructivoUpdate(UpdateView):
#     model = ListaSisConstructivo
#     form_class = ListaSisConstructivoForm
#     template_name_suffix = '_update_form'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['p_title']="Actualizar"
#         context['txt_actualizacion']="Registro actualizado correctamente"
#         return context
    
#     def get_success_url(self):

#         return reverse_lazy('catalogos:sistema-update',args=[self.object.id]) + '?ok'


