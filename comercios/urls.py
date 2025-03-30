from django.urls import path
from .views import ComercioListview, RestaurantesListview, ModaListview, ComercioCreateView

urlpatterns = [
    path('', ComercioListview.as_view(), name='comercios'),
    path('nuevo/', ComercioCreateView.as_view(), name='registro_comercio'),
    path('restaurantes/', RestaurantesListview.as_view(), name= 'restaurantes'),
    path('Moda/', ModaListview.as_view(), name= 'Moda'),
]

