from django.shortcuts import render
from django.views.generic import ListView
from .models import Comercio

# Create your views here.

class ComercioListview(ListView):
    template_name = 'comercios/catalogo.html'
    model = Comercio
    context_object_name = 'comercios'


class RestaurantesListview(ListView):
    template_name = 'comercios/restaurantes.html'
    model = Comercio
    context_object_name = 'comercios'

    def get_queryset(self):
        filtro = 'Restaurantes'
        categoria = Comercio.objects.filter(categoria = filtro)

        return categoria

class ModaListview(ListView):
    template_name = 'comercios/moda.html'
    model = Comercio
    context_object_name = 'comercios'

    def get_queryset(self):
        filtro = 'Moda'
        categoria = Comercio.objects.filter(categoria = filtro)

        return categoria
    
    # class BellezaListview(ListView):
    # template_name = 'comercios/belleza.html'
    # model = Comercio
    # context_object_name = 'comercios'

    # def get_queryset(self):
    #     filtro = 'Belleza'
    #     categoria = Comercio.objects.filter(categoria = filtro)

    #     return categoria