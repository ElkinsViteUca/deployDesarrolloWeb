from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView
from core.models import *
from .forms import *
# Create your views here.


class InicioTemplateView(TemplateView):
  template_name = "Administrador/cardsAdministrador.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['titulo'] = "Administrador"
    return context



class televisorListView(ListView):
  template_name = "formularios/listadotv.html"
  context_object_name = 'Televisor'
  model = Televisor

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['titulo'] = "LISTA DE TELEVISORES"
    context['boton'] = "Crear Registro"
    context['listar_url'] = '/listatelevisores/'
    context['crear_url'] = '/creartelevisores/'
    context['table_title'] = 'Listado de Televisores'
    #context['pdf'] = '/pdfactivo/'
    context['query'] = self.request.GET.get("query")
    return context



class televisorCreateView(CreateView):
    template_name = 'formularios/formulariotvPrueba.html'
    model = Televisor
    form_class = TelevisorForm
    success_url = reverse_lazy('listatelevisores')


    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['titulo'] = "CREAR REGISTRO TV"
      context['boton'] = "Guardar Registro"
      context['listar_url'] = '/listaempleado/'
      context['action_save'] = '/creartelevisores/'
      context['form_title'] = 'Formulario TV'
      context['mensaje'] = 'Creado'
      return context

#     def post(self,request,*args ,**kwargs):
#       print(request.POST)
#       return redirect('listatelevisores')

    # def form_valid(self,form):
    #   messages.success(self.request,"El registro se ha guardado Correctamente")
    #   return super().form_valid(form)

class actualizarTelevisor(UpdateView):
  model = Televisor
  template_name = "formularios/formulariotvPrueba.html"
  success_url = reverse_lazy('listatelevisores')
  form_class = TelevisorForm
  success_message = "Se ha modificado correctamente"
  #queryset = Televisor.objects.get(pk=request.GET.get("id"))

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['action_save'] = self.request.path
    context['titulo'] = 'Administrador'
    context['form_title'] = 'ACTUALIZAR REGISTRO TV'
    context['listar_url'] = '/listatelevisores'
    context['boton'] = "Actualizar"
    context['table_title'] = 'Listado TV'
    context['mensaje'] = 'Listado TV'
    context['form_actualizar'] = 'Nota: Si no ingresas ninguna img, queda la anterior. No te preocupes'
    return context

class eliminarTelevisor(DeleteView):
  model = Televisor
  template_name = "formularios/eliminarTv.html"
  success_url = reverse_lazy('listatelevisores')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['action_save'] = self.request.path
    context['titulo'] = 'Administrador'
    context['form_title'] = 'Eliminación De Registro TV'
    context['listar_url'] = '/listatelevisores'
    context['boton'] = "Eliminar"
    context['table_title'] = 'Seguro Que Deseas Eliminar este Registro?'
    return context


#******************************************** Refrigeradora ********************************************************
class refrigeradoraListView(ListView):
  template_name = "formularios/listadoRefrigeradora.html"
  context_object_name = 'Refrigeradora'
  model = Refrigeradora

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['titulo'] = "LISTA DE REFRIGERADORAS"
    context['listar_url'] = '/listarefrigeradoras/'
    context['crear_url'] = '/crearrefrigeradoras/'
    context['table_title'] = 'Listado Refrigeradora'
    context['boton'] = "Crear Registro"
    context['query'] = self.request.GET.get("query")
    return context

class refrigeradoraCreateView(CreateView):
  template_name = 'formularios/formularioRefrigeradoa.html'
  model = Refrigeradora
  form_class = RefrigeradoraForm
  success_url = reverse_lazy('listarefrigeradoras')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['titulo'] = "CREAR REGISTRO DE REFRIGERADORA"
    context['boton'] = "Guardar Registro"
    context['listar_url'] = '/listarefrigeradoras/'
    context['action_save'] = '/crearrefrigeradoras/'
    context['form_title'] = 'Formulario Refrigeradora'
    return context

class actualizarRefrigeradora(UpdateView):
  model = Refrigeradora
  template_name = "formularios/formularioRefrigeradoa.html"
  success_url = reverse_lazy('listarefrigeradoras')
  form_class = RefrigeradoraForm
  #queryset = Televisor.objects.get(pk=request.GET.get("id"))

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['action_save'] = self.request.path
    context['titulo'] = 'Administrador'
    context['form_title'] = 'ACTUALIZAR REGISTRO REFRIGERADORA'
    context['listar_url'] = '/listarefrigeradoras'
    context['boton'] = "Actualizar"
    context['table_title'] = 'Listado Refrigeradora'
    return context

class eliminarRefrigeradora(DeleteView):
  model = Refrigeradora
  template_name = "formularios/eliminarRefri.html"
  success_url = reverse_lazy('listarefrigeradoras')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['action_save'] = self.request.path
    context['titulo'] = 'Eliminación De Refrigeradora'
    context['listar_url'] = '/listatelevisores'
    context['boton'] = "Eliminar"
    context['table_title'] = 'Seguro Que Deseas Eliminar este Registro?'
    return context

#******************************************** Microondas ********************************************************
class microondasListView(ListView):
  template_name = "formularios/listadoMicroo.html"
  context_object_name = 'Microondas'
  model = Microondas

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['titulo'] = "Lista de Microondas"
    context['listar_url'] = '/listamicroondas/'
    context['crear_url'] = '/crearmicroondas/'
    context['table_title'] = 'Listado de Microondas'
    context['boton'] = "Crear Registro"
    context['query'] = self.request.GET.get("query")
    return context

class microondasCreateView(CreateView):
  template_name = 'formularios/formularioMicroo.html'
  model = Microondas
  form_class = MicroondasForm
  success_url = reverse_lazy('listamicroondas')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['titulo'] = "CREAR REGISTRO DE MICROONDAS"
    context['boton'] = "Guardar Registro"
    context['listar_url'] = '/listamicroondas/'
    context['action_save'] = '/crearmicroondas/'
    context['form_title'] = 'Formulario Microondas'
    return context

class actualizarMicroondas(UpdateView):
  model = Microondas
  template_name = "formularios/formularioMicroo.html"
  success_url = reverse_lazy('listamicroondas')
  form_class = MicroondasForm
  #queryset = Televisor.objects.get(pk=request.GET.get("id"))

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['action_save'] = self.request.path
    context['titulo'] = 'Administrador'
    context['form_title'] = 'ACTUALIZAR REGISTRO MICROONDAS'
    context['listar_url'] = '/listamicroondas'
    context['boton'] = "Actualizar"
    context['table_title'] = 'Listado de Microondas'
    return context

class eliminarMicroondas(DeleteView):
  model = Microondas
  template_name = "formularios/eliminarMicroo.html"
  success_url = reverse_lazy('listamicroondas')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['action_save'] = self.request.path
    context['titulo'] = 'Eliminación De Refrigeradora'
    context['listar_url'] = '/listamicroondas'
    context['boton'] = "Eliminar"
    context['table_title'] = 'Seguro Que Deseas Eliminar este Registro?'
    return context