from django.urls import path
from .views import ComercioListview, RestaurantesListview, ModaListview

urlpatterns = [
    path('', ComercioListview.as_view(), name='comercios'),
    path('restaurantes/', RestaurantesListview.as_view(), name= 'restaurantes'),
    path('Moda/', ModaListview.as_view(), name= 'Moda'),
]

