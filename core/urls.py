from django.urls import path
from .views import HomePageView, NosotrosPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='inicio'),
    path('nosotros/', NosotrosPageView.as_view(), name='nosotros')
]

