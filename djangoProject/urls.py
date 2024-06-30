"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from djangoProject import settings
from core.views import *
from core.login.views import LoginAdminView,LogoutView
from core.public.views import indexTemplateView,televisorPublicListView, RefriPublicListView, microoPublicListView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/',LoginAdminView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page=''),name='logout'),

    path('',indexTemplateView.as_view(),name=''),
    path('tvpublic/',televisorPublicListView.as_view(),name='tvpublic'),
    path('refripublic/',RefriPublicListView.as_view(),name='refripublic'),
    path('micropublic/',microoPublicListView.as_view(),name='micropublic'),



    path('inicioadmin/',InicioTemplateView.as_view(),name="inicioadmin"),

    path('listatelevisores/',televisorListView.as_view(),name='listatelevisores'),
    path('creartelevisores/',televisorCreateView.as_view(),name='creartelevisores'),
    path('actualizartv/<int:pk>',actualizarTelevisor.as_view(),name='actualizartv'),
    path('eliminartv/<int:pk>',eliminarTelevisor.as_view(),name='eliminartv'),

    path('listarefrigeradoras/',refrigeradoraListView.as_view(),name='listarefrigeradoras'),
    path('crearrefrigeradoras/',refrigeradoraCreateView.as_view(),name='crearrefrigeradoras'),
    path('actualizarrefrigeradoras/<int:pk>',actualizarRefrigeradora.as_view(),name='actualizarrefrigeradoras'),
    path('eliminarrefrigeradoras/<int:pk>',eliminarRefrigeradora.as_view(),name='eliminarrefrigeradoras'),

    path('listamicroondas/',microondasListView.as_view(),name='listamicroondas'),
    path('crearmicroondas/',microondasCreateView.as_view(),name='crearmicroondas'),
    path('actualizarmicroondas/<int:pk>',actualizarMicroondas.as_view(),name='actualizarmicroondas'),
    path('eliminarmicroondas/<int:pk>',eliminarMicroondas.as_view(),name='eliminarmicroondas'),

]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


