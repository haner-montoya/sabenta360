from django.urls import path
from .views import ComercioListview

urlpatterns = [
    path('', ComercioListview.as_view(), name='comercios'),
]

