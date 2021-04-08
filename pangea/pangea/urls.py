"""pangea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from formulario.urls import formulario_patterns
from miscelanea.urls import catalogos_patterns

## estos eran anteriores a los cambios 
# from django.contrib import admin
# from django.urls import path
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from cap2 import views
# from ficha import views as fichas_views
# from formulario import views as forms_views
# from django.conf import settings


urlpatterns = [
                path('',include('cap2.urls')),
                path('forms/',include(formulario_patterns)),
                path('catalogos/',include(catalogos_patterns)),
                #pathhs de Auth
                path('accounts/',include('django.contrib.auth.urls')),
                path('accounts/',include('registration.urls')),
                path('admin/', admin.site.urls),
            ]
    # '''
    # path('',views.index),
    # path('login/',views.login_page),
    # path('logout/',views.logout_user,name='logout'),
    # path('fichas/',fichas_views.fichascap2),
    # path('crear-estructura/',forms_views.agregar_estructura),
    # path('formlocalizacion/',forms_views.LocalizacionCreate.as_view()),
    # path('pages/<str:componente>/<str:fase>/<str:etapa>/', forms_views.page),
    # '''
    
    #path('formularios/',views.FigurasList),
    #path('imagenes/', views.ImagenList.as_view()),
#]

#urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)