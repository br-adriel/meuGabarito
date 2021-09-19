from django.urls import path, include
from .views import criar_conta_view

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', criar_conta_view, name='register'),
]
