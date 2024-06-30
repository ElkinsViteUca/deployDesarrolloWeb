from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from core.models import *


# Create your views here.
class indexTemplateView(TemplateView):
  template_name = "Public/indexPublic.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['titulo'] = "Administrador"
    return context

class televisorPublicListView(ListView):
  template_name = "Public/listTvPublic.html"
  context_object_name = 'Televisor'
  model = Televisor

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['titulo'] = "LISTA DE TELEVISORES"
    # context['boton'] = "Crear Registro"
    # context['listar_url'] = '/listatelevisores/'
    # context['crear_url'] = '/creartelevisores/'
    # context['table_title'] = 'Listado de Televisores'
    #context['pdf'] = '/pdfactivo/'
    context['query'] = self.request.GET.get("query")
    return context

class RefriPublicListView(ListView):
  template_name = "Public/listRefriPublic.html"
  context_object_name = 'Refrigeradora'
  model = Refrigeradora

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['titulo'] = "LISTA DE REFRIGERADORAS"
    # context['boton'] = "Crear Registro"
    # context['listar_url'] = '/listatelevisores/'
    # context['crear_url'] = '/creartelevisores/'
    # context['table_title'] = 'Listado de Televisores'
    #context['pdf'] = '/pdfactivo/'
    context['query'] = self.request.GET.get("query")
    return context

class microoPublicListView(ListView):
  template_name = "Public/listMicroPublic.html"
  context_object_name = 'Microondas'
  model = Microondas

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['titulo'] = "LISTA DE MICROONDAS"
    # context['boton'] = "Crear Registro"
    # context['listar_url'] = '/listatelevisores/'
    # context['crear_url'] = '/creartelevisores/'
    # context['table_title'] = 'Listado de Televisores'
    #context['pdf'] = '/pdfactivo/'
    context['query'] = self.request.GET.get("query")
    return context