from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from .forms import ClienteForm,MascotaForm,CitaForm,ProdcutoForm
from django.urls import reverse_lazy

# Create your views here.

class HomeView(TemplateView):
    template_name='home.html'

class ServicioView(TemplateView):
    template_name='servicios.html'

class LoginView(TemplateView):
    template_name='login.html'

class ClienteView(TemplateView):
    template_name='Datos de Cliente.html'

class ProductoView(TemplateView):
    template_name='productos.html'


class CitasView(TemplateView):
    template_name='Citas.html'


class CrearClienteView(CreateView):
    template_name ='Datos de Cliente.html'
    form_class = ClienteForm
    success_url=reverse_lazy('home:homeapp')

class CrearMascotaView(CreateView):
    template_name ='mascota.html'
    form_class = MascotaForm
    success_url=reverse_lazy('home:clienteapp')

class CrearCitasView(CreateView):
    template_name='Citas.html'
    form_class= CitaForm
    success_url= reverse_lazy('home:homeapp')


class CrearProductoView(CreateView):
    template_name ='productos.html'
    form_class = ProdcutoForm
    success_url=reverse_lazy('home:homeapp')


