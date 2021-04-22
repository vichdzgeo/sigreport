from django.urls import path
from . import views
from .views import *
formulario_patterns = ([  
    path('localizacion/<int:pk>/', LocalizacionCreate.as_view(), name='localizacion'),
    path('fig-loc/<int:pk>/', LocalizacionCListView.as_view(), name='fig-loc'),
    path('fig-update/<int:pk>/',LocalizacionCUpdate.as_view(),name='fig-update'),
    path('fichas/', EstructuraView.as_view(), name='fichas'),
    path('crear-estructura/',agregar_estructura),
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

],'forms')