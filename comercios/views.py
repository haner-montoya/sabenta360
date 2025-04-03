from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from src import settings
from .models import Comercio
from .forms import RegistroComercio
import matplotlib.pyplot as plt
import os


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

    def get_queryset(self):
        publicados = Comercio.objects.filter(publicado = True)

        return publicados
    

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
    

class GraficoPageView(TemplateView):
    template_name = 'comercios/estadistica.html'

    def get(self, request, *args, **kwargs):
        # Creamos 2 arreglos para los ejes de los gráficos:
        categorias = ['Restaurantes', 'Salud', 'Belleza', 'Moda', 'Entretenimiento']
        conteo = [Comercio.objects.filter(categoria=c).count() for c in categorias]
        
        # Crear la gráfica
        plt.figure(figsize=(6,4))
        bars = plt.bar(categorias, conteo, color=['yellow', 'blue', 'red', 'purple', 'orange'])
        plt.xlabel('Categoría')
        plt.ylabel('Cantidad de Negocios')
        plt.title('Negocios por Categoría')

        # Agregar los valores sobre las barras:
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom')

        # Creamos el directorio de la gráfica:
        graf = os.path.join(settings.STATICFILES_DIRS[0], 'media/img/graficas')
        os.makedirs(graf, exist_ok=True)

        # Guardamos la gráfica
        img_path = os.path.join(graf, 'conteo_comercios.png')
        plt.savefig(img_path)
        plt.close()

        # Nota: El gráfico se rendizará por cada vez que abramos la página:
        return render(request, self.template_name, {'titulog': 'Cantidad de Comercios por Categoría', 'grafica':f'{graf}/conteo_comercios.png'})
    
    
        