from django.urls import path
from .views import ComercioListview, RestaurantesListview, ModaListview, ComercioCreateView, BellezaListview, EntretenimientoListview, SaludListview

urlpatterns = [
    path('', ComercioListview.as_view(), name='comercios'),
    path('nuevo/', ComercioCreateView.as_view(), name='registro_comercio'),
    path('restaurantes/', RestaurantesListview.as_view(), name= 'restaurantes'),
    path('Moda/', ModaListview.as_view(), name= 'Moda'),
    path('Belleza/', BellezaListview.as_view(), name= 'Belleza'),
    path('Entretenimiento/', EntretenimientoListview.as_view(), name= 'Entretenimiento'),
    path('Salud/', SaludListview.as_view(), name= 'Salud'),
]

