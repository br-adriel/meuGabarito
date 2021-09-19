from django.urls import path
from .views import pagina_inicial_view

urlpatterns = [
    path('', pagina_inicial_view, name='pagina_inicial'),
]