from django.shortcuts import render
from django.views.generic import ListView
from .models import Comercio

# Create your views here.

class ComercioListview(ListView):
    template_name = 'comercios/catalogo.html'
    model = Comercio

