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
    path('edificaciones/', EdiProvisionalListView.as_view(), name='edificaciones'),
    path('edificio-create/',EdiProvisionalCreate.as_view(),name='edificio-create'),
    path('edificio-update/<int:pk>/',EdiProvisionalUpdate.as_view(),name='edificio-update'),
    path('actividades/', ActProvisionalListView.as_view(), name='actividades'),
    path('actividad-create/',ActProvisionalCreate.as_view(),name='actividad-create'),
    path('actividad-update/<int:pk>/',ActProvisionalUpdate.as_view(),name='actividad-update'),
    path('componentes/', ModuloListView.as_view(), name='componentes'),
    path('componente-create/',ModuloCreate.as_view(),name='componente-create'),
    path('componente-update/<int:pk>/',ModuloUpdate.as_view(),name='componente-update'),

],'catalogos')