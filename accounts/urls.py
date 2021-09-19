from django.urls import path, include
from .views import criar_conta_view, editar_perfil_view

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', criar_conta_view, name='register'),
    path('profile', editar_perfil_view, name='editar_perfil'),
]
