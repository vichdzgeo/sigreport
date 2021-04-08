from django.urls import path
from . import views
from .views import LocalizacionCUpdate,LocalizacionCListView,LocalizacionCreate,fichascap2,EstructuraView
formulario_patterns = ([
    path('localizacion/', LocalizacionCreate.as_view(), name='localizacion'),
    path('fig-loc/', LocalizacionCListView.as_view(), name='fig-loc'),
    path('fig-update/<int:pk>/',LocalizacionCUpdate.as_view(),name='fig-update'),
    path('fichas/', EstructuraView.as_view(), name='fichas'),
    #path('fichas/', fichascap2, name='fichas'),
],'forms')