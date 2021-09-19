from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def pagina_inicial_view(request):
    return render(request, 'gabaritos/pagina_inicial.html')
