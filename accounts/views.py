from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .forms import EditarPerfilForm

def criar_conta_view(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            # login do usuario criado
            username = form.cleaned_data.get('username')
            senha = form.cleaned_data.get('password1')
            usuario = authenticate(request, username=username, password=senha)

            if usuario is not None:
                login(request, usuario)
                return redirect('pagina_inicial')
    return render(request, 'registration/criar_conta.html', {'form' : form})


@login_required
def editar_perfil_view(request):
    form = EditarPerfilForm(instance=request.user)

    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            messages.success(request, 'Perfil atualizado.')
    return render(request, 'registration/editar_perfil.html', {'form' : form})


@login_required
def excluir_conta_view(request):
    usuario = request.user
    
    logout(request)
    usuario.delete()

    messages.success(request, 'Sua conta foi apagada.')
    return redirect('pagina_inicial')
