from django.urls import path
from .views import HomePageView, NosotrosPageView, AcercaPageView, InicioPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='inicio'),
    path('nosotros/', NosotrosPageView.as_view(), name='nosotros'),
    path('acerca/', AcercaPageView.as_view(), name='acerca'),
    path('inicio/', InicioPageView.as_view(), name='inicio')

]

