from django.urls import path
from . import views
from .views import * #CatalogosPageView,MaquinaListView, MaquinaCreate, MaquinaUpdate,
catalogos_patterns = ([
    path('', CatalogosPageView.as_view(), name='catalogos'),
    path('etapas/', EtapaListView.as_view(), name='etapas'),
    path('etapa-create/',EtapaCreate.as_view(),name='etapa-create'),
    path('etapa-update/<int:pk>/',EtapaUpdate.as_view(),name='etapa-update'),
    path('componentes/', ModuloListView.as_view(), name='componentes'),
    path('componente-create/',ModuloCreate.as_view(),name='componente-create'),
    path('componente-update/<int:pk>/',ModuloUpdate.as_view(),name='componente-update'),
    
    
    path('tiposv/', ListaTipoVehiculoListView.as_view(), name='tiposv'),
    path('tipov-create/',ListaTipoVehiculoCreate.as_view(),name='tipov-create'),
    path('tipov-update/<int:pk>/',ListaTipoVehiculoUpdate.as_view(),name='tipov-update'),

    path('vehiculos/', VehiculoPorTipoListView.as_view(), name='vehiculos'),
    path('vehiculo-create/',VehiculoPorTipoCreate.as_view(),name='vehiculo-create'),
    path('vehiculo-update/<int:pk>/',VehiculoPorTipoUpdate.as_view(),name='vehiculo-update'),

    path('ins-especiales/', ListInsEspListView.as_view(), name='ins-especiales'),
    path('iespecial-create/',ListInsEspCreate.as_view(),name='iespecial-create'),
    path('iespecial-update/<int:pk>/',ListInsEspUpdate.as_view(),name='iespecial-update'),

    path('act-fase/', ListaActividadesListView.as_view(), name='act-fase'),
    path('act-create/',ListaActividadesCreate.as_view(),name='act-create'),
    path('act-update/<int:pk>/',ListaActividadesUpdate.as_view(),name='act-update'),

    path('resespecial/', ResiduosPeligrososListView.as_view(), name='resespecial'),
    path('resespecial-create/',ResiduosPeligrososCreate.as_view(),name='resespecial-create'),
    path('resespecial-update/<int:pk>/',ResiduosPeligrososUpdate.as_view(),name='resespecial-update'),

    path('ptrata/', ListaPTARListView.as_view(), name='ptrata'),
    path('ptrata-create/',ListaPTARCreate.as_view(),name='ptrata-create'),
    path('ptrata-update/<int:pk>/',ListaPTARUpdate.as_view(),name='ptrata-update'),

    path('actservic/', ListaAct_scrcListView.as_view(), name='actservic'),
    path('actservic-create/',ListaAct_scrcCreate.as_view(),name='actservic-create'),
    path('actservic-update/<int:pk>/',ListaAct_scrcUpdate.as_view(),name='actservic-update'),

    path('actvisita/', ListActVisitantesListView.as_view(), name='actvisita'),
    path('actvisita-create/',ListActVisitantesCreate.as_view(),name='actvisita-create'),
    path('actvisita-update/<int:pk>/',ListActVisitantesUpdate.as_view(),name='actvisita-update'),

    path('areasm/', ListaAreasManejoPeligrosasListView.as_view(), name='areasm'),
    path('areasm-create/',ListaAreasManejoPeligrosasCreate.as_view(),name='areasm-create'),
    path('areasm-update/<int:pk>/',ListaAreasManejoPeligrosasUpdate.as_view(),name='areasm-update'),

    path('actespeciales/', ListaActInsEspListView.as_view(), name='actespeciales'),
    path('actespeciales-create/',ListaActInsEspCreate.as_view(),name='actespeciales-create'),
    path('actespeciales-update/<int:pk>/',ListaActInsEspUpdate.as_view(),name='actespeciales-update'),


    path('maquinas/', MaquinaListView.as_view(), name='maquinas'),
    path('maquina-create/',MaquinaCreate.as_view(),name='maquina-create'),
    path('maquina-update/<int:pk>/',MaquinaUpdate.as_view(),name='maquina-update'),
    path('unidades/', UnidadListView.as_view(), name='unidades'),
    path('unidad-create/',UnidadCreate.as_view(),name='unidad-create'),
    path('unidad-update/<int:pk>/',UnidadUpdate.as_view(),name='unidad-update'),
    path('edificaciones/', EdiProvisionalListView.as_view(), name='edificaciones'),
    path('edificio-create/',EdiProvisionalCreate.as_view(),name='edificio-create'),
    path('edificio-update/<int:pk>/',EdiProvisionalUpdate.as_view(),name='edificio-update'),
    path('actividades/', ActProvisionalListView.as_view(), name='actividades'),
    path('actividad-create/',ActProvisionalCreate.as_view(),name='actividad-create'),
    path('actividad-update/<int:pk>/',ActProvisionalUpdate.as_view(),name='actividad-update'),
    path('insumos/', InsumosListaListView.as_view(), name='insumos'),
    path('insumo-create/',InsumosListaCreate.as_view(),name='insumo-create'),
    path('insumo-update/<int:pk>/',InsumosListaUpdate.as_view(),name='insumo-update'),
    path('quimicas/', SustanciasQuimicasPListView.as_view(), name='quimicas'),
    path('quimica-create/',SustanciasQuimicasPCreate.as_view(),name='quimica-create'),
    path('quimica-update/<int:pk>/',SustanciasQuimicasPUpdate.as_view(),name='quimica-update'),
    path('flores/', ListadoFloristicoListView.as_view(), name='flores'),
    path('flor-create/',ListadoFloristicoCreate.as_view(),name='flor-create'),
    path('flor-update/<int:pk>/',ListadoFloristicoUpdate.as_view(),name='flor-update'),
    path('personal/', ListaTipoPersonalListView.as_view(), name='personal'),
    path('personal-create/',ListaTipoPersonalCreate.as_view(),name='personal-create'),
    path('personal-update/<int:pk>/',ListaTipoPersonalUpdate.as_view(),name='personal-update'),
    path('personal/', ListaTipoPersonalListView.as_view(), name='personal'),
    path('personal-create/',ListaTipoPersonalCreate.as_view(),name='personal-create'),
    path('personal-update/<int:pk>/',ListaTipoPersonalUpdate.as_view(),name='personal-update'),


    path('descsistema/', SisConstructivoListView.as_view(), name='descsistema'),
    path('descsistema-create/',SisConstructivoCreate.as_view(),name='descsistema-create'),
    path('descsistema-update/<int:pk>/',SisConstructivoUpdate.as_view(),name='descsistema-update'),

    path('descproceso/', ProcConstructivoListView.as_view(), name='descproceso'),
    path('descproceso-create/',ProcConstructivoCreate.as_view(),name='descproceso-create'),
    path('descproceso-update/<int:pk>/',ProcConstructivoUpdate.as_view(),name='descproceso-update'),

    path('sistemasfiguras-create/<int:pk>/',SisFigurasCreate.as_view(),name='sistemasfiguras-create'),
    path('sistemasfiguras-update/<int:pk>/',SisFigurasUpdate.as_view(),name='sistemasfiguras-update'),

    path('residuos/', ListaTipoResiduosListView.as_view(), name='residuos'),
    path('residuo-create/',ListaTipoResiduosCreate.as_view(),name='residuo-create'),
    path('residuo-update/<int:pk>/',ListaTipoResiduosUpdate.as_view(),name='residuo-update'),

    path('residuossolidos/', ListaTipoResiduosSolidosListView.as_view(), name='residuossolidos'),
    path('residuossolidos-create/',ListaTipoResiduosSolidosCreate.as_view(),name='residuossolidos-create'),
    path('residuossolidos-update/<int:pk>/',ListaTipoResiduosSolidosUpdate.as_view(),name='residuossolidos-update'),
    path('tagua/', TipoAguaListView.as_view(), name='tagua'),
    path('tagua-create/',TipoAguaCreate.as_view(),name='tagua-create'),
    path('tagua-update/<int:pk>/',TipoAguaUpdate.as_view(),name='tagua-update'),
    path('tagresidual/', TipoAguaResidualListView.as_view(), name='tagresidual'),
    path('tagresidual-create/',TipoAguaResidualCreate.as_view(),name='tagresidual-create'),
    path('tagresidual-update/<int:pk>/',TipoAguaResidualUpdate.as_view(),name='tagresidual-update'),
    path('aprovechamiento/', ListaTiposAprovechamientoListView.as_view(), name='aprovechamiento'),
    path('aprovechamiento-create/',ListaTiposAprovechamientoCreate.as_view(),name='aprovechamiento-create'),
    path('aprovechamiento-update/<int:pk>/',ListaTiposAprovechamientoUpdate.as_view(),name='aprovechamiento-update'),
    path('cobertura/', ListaTiposCoberturaListView.as_view(), name='cobertura'),
    path('cobertura-create/',ListaTiposCoberturaCreate.as_view(),name='cobertura-create'),
    path('cobertura-update/<int:pk>/',ListaTiposCoberturaUpdate.as_view(),name='cobertura-update'),
    path('zona/', ListaZonificacionListView.as_view(), name='zona'),
    path('zona-create/',ListaZonificacionCreate.as_view(),name='zona-create'),
    path('zona-update/<int:pk>/',ListaZonificacionUpdate.as_view(),name='zona-update'),
    path('tierra/', MovimientoTierraListView.as_view(), name='tierra'),
    path('tierra-create/',MovimientoTierraCreate.as_view(),name='tierra-create'),
    path('tierra-update/<int:pk>/',MovimientoTierraUpdate.as_view(),name='tierra-update'),
    path('consedi/', ListaTiposConsEdifListView.as_view(), name='consedi'),
    path('consedi-create/',ListaTiposConsEdifCreate.as_view(),name='consedi-create'),
    path('consedi-update/<int:pk>/',ListaTiposConsEdifUpdate.as_view(),name='consedi-update'),
    path('obraslineales/', ObrasLinealesListView.as_view(), name='obraslineales'),
    path('obraslineales-create/',ObrasLinealesCreate.as_view(),name='obraslineales-create'),
    path('obraslineales-update/<int:pk>/',ObrasLinealesUpdate.as_view(),name='obraslineales-update'),

],'catalogos')