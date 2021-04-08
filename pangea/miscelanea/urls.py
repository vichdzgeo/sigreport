from django.urls import path
from . import views
from .views import * #CatalogosPageView,MaquinaListView, MaquinaCreate, MaquinaUpdate,
catalogos_patterns = ([
    path('', CatalogosPageView.as_view(), name='catalogos'),
    path('maquinas/', MaquinaListView.as_view(), name='maquinas'),
    path('maquina-create/',MaquinaCreate.as_view(),name='maquina-create'),
    path('maquina-update/<int:pk>/',MaquinaUpdate.as_view(),name='maquina-update'),
    path('unidades/', UnidadListView.as_view(), name='unidades'),
    path('unidad-create/',UnidadCreate.as_view(),name='unidad-create'),
    path('unidad-update/<int:pk>/',UnidadUpdate.as_view(),name='unidad-update'),

],'catalogos')