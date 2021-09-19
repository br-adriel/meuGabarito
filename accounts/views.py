from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


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
