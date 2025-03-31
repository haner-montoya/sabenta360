from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Comercio
from .forms import RegistroComercio

# Create your views here.

class ComercioCreateView(CreateView):
    template_name = 'comercios/registro.html'
    model = Comercio
    form_class = RegistroComercio
    # success_url = '/comercios/catalogo/'
    success_url = reverse_lazy('comercios')
    
    def form_valid(self, form):
        # Aquí puedes agregar lógica adicional antes de guardar el formulario
        # Por ejemplo, puedes enviar un correo electrónico o realizar alguna validación
        return super().form_valid(form)
    
    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return render(request, self.template_name, {'form': self.form_class})

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

class BellezaListview(ListView):
    template_name = 'comercios/belleza.html'
    model = Comercio
    context_object_name = 'comercios'

    def get_queryset(self):
        filtro = 'Belleza'
        categoria = Comercio.objects.filter(categoria = filtro)

        return categoria
    
class EntretenimientoListview(ListView):
    template_name = 'comercios/entretenimiento.html'
    model = Comercio
    context_object_name = 'comercios'

    def get_queryset(self):
        filtro = 'Entretenimiento'
        categoria = Comercio.objects.filter(categoria = filtro)

        return categoria

class SaludListview(ListView):
    template_name = 'comercios/salud.html'
    model = Comercio
    context_object_name = 'comercios'

    def get_queryset(self):
        filtro = 'Salud'
        categoria = Comercio.objects.filter(categoria = filtro)

        return categoria
