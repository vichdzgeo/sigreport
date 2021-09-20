from django.urls import path
from . import views
from .views import *
formulario_patterns = ([  
    path('localizacion/<int:pk>/', LocalizacionCreate.as_view(), name='localizacion'),
    path('fig-loc/<int:pk>/', LocalizacionCListView.as_view(), name='fig-loc'),
    path('fig-update/<int:pk>/',LocalizacionCUpdate.as_view(),name='fig-update'),
    path('fichas/', EstructuraView.as_view(), name='fichas'),
    path('ficha/<int:componente>/<int:fase>/<int:etapa>/',ensamblaficha , name='ficha'),
    #path('crear-estructura/',agregar_estructura),
    ### GENERALES###
    path('actividadf-list/<int:pk>/',  FrecuenciaActividadesListView.as_view(), name='actividadf-list'),
    path('actividadf-create/<int:pk>/', FrecuenciaActividadesCreate.as_view(),name='actividadf-create'),
    path('actividadf-update/<int:pk>/', FrecuenciaActividadesUpdate.as_view(),name='actividadf-update'),

    path('insreqalm-list/<int:pk>/',  InsumosRequeridosAlmacenadosListView.as_view(), name='insreqalm-list'),
    path('insreqalm-create/<int:pk>/', InsumosRequeridosAlmacenadosCreate.as_view(),name='insreqalm-create'),
    path('insreqalm-update/<int:pk>/', InsumosRequeridosAlmacenadosUpdate.as_view(),name='insreqalm-update'),

    path('usosusquim-list/<int:pk>/',  UsoSustanciasQuimicasListView.as_view(), name='usosusquim-list'),
    path('usosusquim-create/<int:pk>/', UsoSustanciasQuimicasCreate.as_view(),name='usosusquim-create'),
    path('usosusquim-update/<int:pk>/', UsoSustanciasQuimicasUpdate.as_view(),name='usosusquim-update'),

    path('personale-list/<int:pk>/',  PersonalListView.as_view(), name='personale-list'),
    path('personale-create/<int:pk>/', PersonalCreate.as_view(),name='personale-create'),
    path('personale-update/<int:pk>/', PersonalUpdate.as_view(),name='personale-update'),

    path('vehreszon-list/<int:pk>/',  VehiculosRestrigidosZonificacionListView.as_view(), name='vehreszon-list'),
    path('vehreszon-create/<int:pk>/', VehiculosRestrigidosZonificacionCreate.as_view(),name='vehreszon-create'),
    path('vehreszon-update/<int:pk>/', VehiculosRestrigidosZonificacionUpdate.as_view(),name='vehreszon-update'),

    path('usomaquina-list/<int:pk>/',  UsoMaquinariaListView.as_view(), name='usomaquina-list'),
    path('usomaquina-create/<int:pk>/', UsoMaquinariaCreate.as_view(),name='usomaquina-create'),
    path('usomaquina-update/<int:pk>/', UsoMaquinariaUpdate.as_view(),name='usomaquina-update'),

    path('genres-list/<int:pk>/',  GeneracionResiduosListView.as_view(), name='genres-list'),
    path('genres-create/<int:pk>/', GeneracionResiduosCreate.as_view(),name='genres-create'),
    path('genres-update/<int:pk>/', GeneracionResiduosUpdate.as_view(),name='genres-update'),

    path('afoalmveh-list/<int:pk>/',  AforoAlmacenamientoVehicularListView.as_view(), name='afoalmveh-list'),
    path('afoalmveh-create/<int:pk>/', AforoAlmacenamientoVehicularCreate.as_view(),name='afoalmveh-create'),
    path('afoalmveh-update/<int:pk>/', AforoAlmacenamientoVehicularUpdate.as_view(),name='afoalmveh-update'),

    path('extagua-list/<int:pk>/',  ExtraccionAguaListView.as_view(), name='extagua-list'),
    path('extagua-create/<int:pk>/', ExtraccionAguaCreate.as_view(),name='extagua-create'),
    path('extagua-update/<int:pk>/', ExtraccionAguaUpdate.as_view(),name='extagua-update'),

    path('freactcom-list/<int:pk>/',  FrecuenciaActComListView.as_view(), name='freactcom-list'),
    path('freactcom-create/<int:pk>/', FrecuenciaActComCreate.as_view(),name='freactcom-create'),
    path('freactcom-update/<int:pk>/', FrecuenciaActComUpdate.as_view(),name='freactcom-update'),

    path('afovis-list/<int:pk>/',  AforoVisitantesListView.as_view(), name='afovis-list'),
    path('afovis-create/<int:pk>/', AforoVisitantesCreate.as_view(),name='afovis-create'),
    path('afovis-update/<int:pk>/', AforoVisitantesUpdate.as_view(),name='afovis-update'),

    path('afovehmaxdia-list/<int:pk>/',  AforoTipoVehiMaxDiarioListView.as_view(), name='afovehmaxdia-list'),
    path('afovehmaxdia-create/<int:pk>/', AforoTipoVehiMaxDiarioCreate.as_view(),name='afovehmaxdia-create'),
    path('afovehmaxdia-update/<int:pk>/', AforoTipoVehiMaxDiarioUpdate.as_view(),name='afovehmaxdia-update'),

    path('afovehtot-list/<int:pk>/',  AforoTipoVehiListView.as_view(), name='afovehtot-list'),
    path('afovehtot-create/<int:pk>/', AforoTipoVehiCreate.as_view(),name='afovehtot-create'),
    path('afovehtot-update/<int:pk>/', AforoTipoVehiUpdate.as_view(),name='afovehtot-update'),

    path('pertra-list/<int:pk>/',  PersonalTransportadoListView.as_view(), name='pertra-list'),
    path('pertra-create/<int:pk>/', PersonalTransportadoCreate.as_view(),name='pertra-create'),
    path('pertra-update/<int:pk>/', PersonalTransportadoUpdate.as_view(),name='pertra-update'),

    path('ocualo-list/<int:pk>/',  OcupacionAlojaListView.as_view(), name='ocualo-list'),
    path('ocualo-create/<int:pk>/', OcupacionAlojaCreate.as_view(),name='ocualo-create'),
    path('ocualo-update/<int:pk>/', OcupacionAlojaUpdate.as_view(),name='ocualo-update'),

    path('mansusesp-list/<int:pk>/',  ManejoSustanciasEspecialesListView.as_view(), name='mansusesp-list'),
    path('mansusesp-create/<int:pk>/', ManejoSustanciasEspecialesCreate.as_view(),name='mansusesp-create'),
    path('mansusesp-update/<int:pk>/', ManejoSustanciasEspecialesUpdate.as_view(),name='mansusesp-update'),

    path('capalmsusesp-list/<int:pk>/',  CapacidadAlmSustanciasEspecialesListView.as_view(), name='capalmsusesp-list'),
    path('capalmsusesp-create/<int:pk>/', CapacidadAlmSustanciasEspecialesCreate.as_view(),name='capalmsusesp-create'),
    path('capalmsusesp-update/<int:pk>/', CapacidadAlmSustanciasEspecialesUpdate.as_view(),name='capalmsusesp-update'),

    path('capalmresesp-list/<int:pk>/',  CapacidadAlmResiduosEspecialesListView.as_view(), name='capalmresesp-list'),
    path('capalmresesp-create/<int:pk>/', CapacidadAlmResiduosEspecialesCreate.as_view(),name='capalmresesp-create'),
    path('capalmresesp-update/<int:pk>/', CapacidadAlmResiduosEspecialesUpdate.as_view(),name='capalmresesp-update'),

    path('freingsusesp-list/<int:pk>/',  FrecuenciaIngresoSusEspecialesListView.as_view(), name='freingsusesp-list'),
    path('freingsusesp-create/<int:pk>/', FrecuenciaIngresoSusEspecialesCreate.as_view(),name='freingsusesp-create'),
    path('freingsusesp-update/<int:pk>/', FrecuenciaIngresoSusEspecialesUpdate.as_view(),name='freingsusesp-update'),

    path('freingresesp-list/<int:pk>/',  FrecuenciaIngresoResEspecialesListView.as_view(), name='freingresesp-list'),
    path('freingresesp-create/<int:pk>/', FrecuenciaIngresoResEspecialesCreate.as_view(),name='freingresesp-create'),
    path('freingresesp-update/<int:pk>/', FrecuenciaIngresoResEspecialesUpdate.as_view(),name='freingresesp-update'),

    path('maqviaesp-list/<int:pk>/',  MaquinariaViajesEspListView.as_view(), name='maqviaesp-list'),
    path('maqviaesp-create/<int:pk>/', MaquinariaViajesEspCreate.as_view(),name='maqviaesp-create'),
    path('maqviaesp-update/<int:pk>/', MaquinariaViajesEspUpdate.as_view(),name='maqviaesp-update'),

    path('traagures-list/<int:pk>/',  TratamientoAguasResidualesListView.as_view(), name='traagures-list'),
    path('traagures-create/<int:pk>/', TratamientoAguasResidualesCreate.as_view(),name='traagures-create'),
    path('traagures-update/<int:pk>/', TratamientoAguasResidualesUpdate.as_view(),name='traagures-update'),
    
    path('completo/<int:pk>/', CatFormUpdate.as_view(),name='completo'),
    path('actividades-list/<int:pk>/',  FrecuenciaActividadesCListView.as_view(), name='actividades-list'),
    path('actividades/<int:pk>/', FrecuenciaActividadesCCreate.as_view(),name='actividades'),
    path('actividad-update/<int:pk>/', FrecuenciaActividadesCUpdate.as_view(),name='actividad-update'),
    path('datosgenerales/<int:pk>/', DatosGeneralCreate.as_view(),name='datosgenerales'),
    path('datosgenerales-list/<int:pk>/',  DatosGeneralListView.as_view(), name='datosgenerales-list'),
    path('datosgenerales-update/<int:pk>/',  DatosGeneralUpdate.as_view(),name='datosgenerales-update'),

    path('selecprocesos/<int:pk>/', SeleccionProcesosConstructivosCreate.as_view(),name='selecprocesos'),
    path('selecprocesos-update/<int:pk>/', SeleccionProcesosConstructivosUpdate.as_view(),name='selecprocesos-update'),

    path('selecsistemas/<int:pk>/', SeleccionSistemasConstructivosCreate.as_view(),name='selecsistemas'),
    path('selecsistemas-list/<int:pk>/', SeleccionSistemasConstructivosListView.as_view(), name='selecsistemas-list'),
    path('selecsistemas-update/<int:pk>/', SeleccionSistemasConstructivosUpdate.as_view(),name='selecsistemas-update'),

    path('generales/<int:pk>/', DescripcionGeneralCreate.as_view(),name='generales'),
    path('generales-list/<int:pk>/',  DescripcionGeneralListView.as_view(), name='generales-list'),
    path('generales-detail/<int:pk>/',  DescripcionGeneralDetailView.as_view(), name='generales-detail'),
    path('generales-update/<int:pk>/',  DescripcionGeneralUpdate.as_view(),name='generales-update'),

    path('generalesfiguras/<int:pk>/', DescripcionGeneralFigurasCreate.as_view(),name='generalesfiguras'),
    path('generalesfigurasu/<int:pk>/', DescripcionGeneralFigurasCreate.as_view(),name='generalesfigurasu'),
    path('generalesfiguras-list/<int:pk>/',  DescripcionGeneralFigurasListView.as_view(), name='generalesfiguras-list'),
    path('generalesfiguras-update/<int:pk>/',  DescripcionGeneralFigurasUpdate.as_view(),name='generalesfiguras-update'),

    path('personal-list/<int:pk>/',  PersonalRequeridoListView.as_view(), name='personal-list'),
    path('personal/<int:pk>/', PersonalRequeridoCreate.as_view(),name='personal'),
    path('personal-update/<int:pk>/', PersonalRequeridoUpdate.as_view(),name='personal-update'),
    path('maquinaria-list/<int:pk>/',  MaquinariaZonificacionListView.as_view(), name='maquinaria-list'),
    path('maquinaria/<int:pk>/', MaquinariaZonificacionCreate.as_view(),name='maquinaria'),
    path('maquinaria-update/<int:pk>/', MaquinariaZonificacionUpdate.as_view(),name='maquinaria-update'),
    path('flor-list/<int:pk>/',  ListadoFloristicoCListView.as_view(), name='flor-list'),
    path('flor/<int:pk>/', ListadoFloristicoCCreate.as_view(),name='flor'),
    path('flor-update/<int:pk>/', ListadoFloristicoCUpdate.as_view(),name='flor-update'),
    path('consumoagua-list/<int:pk>/',  ConsumoAguaCListView.as_view(), name='consumoagua-list'),
    path('consumoagua/<int:pk>/', ConsumoAguaCCreate.as_view(),name='consumoagua'),
    path('consumoagua-update/<int:pk>/', ConsumoAguaCUpdate.as_view(),name='consumoagua-update'),
    path('aguaresidual-list/<int:pk>/',  AguasResidualesCListView.as_view(), name='aguaresidual-list'),
    path('aguaresidual/<int:pk>/', AguasResidualesCCreate.as_view(),name='aguaresidual'),
    path('aguaresidual-update/<int:pk>/', AguasResidualesCUpdate.as_view(),name='aguaresidual-update'),
    path('obrastemporales-list/<int:pk>/',  SuperficieObrasCListView.as_view(), name='obrastemporales-list'),
    path('obrastemporales/<int:pk>/', SuperficieObrasCCreate.as_view(),name='obrastemporales'),
    path('obrastemporales-update/<int:pk>/', SuperficieObrasCUpdate.as_view(),name='obrastemporales-update'),
    path('obraslineales-list/<int:pk>/',  ObrasLinealesLongitudesListView.as_view(), name='obraslineales-list'),
    path('obraslineales/<int:pk>/', ObrasLinealesLongitudesCreate.as_view(),name='obraslineales'),
    path('obraslineales-update/<int:pk>/', ObrasLinealesLongitudesUpdate.as_view(),name='obraslineales-update'),

    path('insumo-list/<int:pk>/',  InsumosZonificacionListView.as_view(), name='insumo-list'),
    path('insumo/<int:pk>/', InsumosZonificacionCreate.as_view(),name='insumo'),
    path('insumo-update/<int:pk>/', InsumosZonificacionUpdate.as_view(),name='insumo-update'),
    path('mtierra-list/<int:pk>/',  MovimientoTierraZonificacionListView.as_view(), name='mtierra-list'),
    path('mtierra/<int:pk>/', MovimientoTierraZonificacionCreate.as_view(),name='mtierra'),
    path('mtierra-update/<int:pk>/', MovimientoTierraZonificacionUpdate.as_view(),name='mtierra-update'),

    path('rsolidos-list/<int:pk>/',  ResiduosSolidosZonificacionListView.as_view(), name='rsolidos-list'),
    path('rsolidos/<int:pk>/', ResiduosSolidosZonificacionCreate.as_view(),name='rsolidos'),
    path('rsolidos-update/<int:pk>/', ResiduosSolidosZonificacionUpdate.as_view(),name='rsolidos-update'),

],'forms')