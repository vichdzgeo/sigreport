from django.urls import path
from . import views
from .views import *
formulario_patterns = ([
    path('localizacion/<int:pk>/', LocalizacionCreate.as_view(), name='localizacion'),
    path('fig-loc/', LocalizacionCListView.as_view(), name='fig-loc'),
    path('fig-update/<int:pk>/',LocalizacionCUpdate.as_view(),name='fig-update'),
    path('fichas/', EstructuraView.as_view(), name='fichas'),
    path('crear-estructura/',agregar_estructura),
    path('completo/<int:pk>/', CatFormUpdate.as_view(),name='completo'),
    path('actividades-list/<int:pk>/',  FrecuenciaActividadesCListView.as_view(), name='actividades-list'),
    path('actividades/<int:pk>/', FrecuenciaActividadesCCreate.as_view(),name='actividades'),
    path('actividad-update/<int:pk>/', FrecuenciaActividadesCUpdate.as_view(),name='actividad-update'),
    path('generales/<int:pk>/', DescripcionGeneralCreate.as_view(),name='generales'),
    path('generales-list/',  DescripcionGeneralListView.as_view(), name='generales-list'),
],'forms')