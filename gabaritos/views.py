from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from .forms import CriarGabaritoForm
from .models import Gabarito, Questao

MESSAGES_TAGS = {
    messages.constants.ERROR : 'danger',
}


@login_required
def pagina_inicial_view(request):
    # criação de um novo gabarito
    form = CriarGabaritoForm()

    if request.method == 'POST':
        form = CriarGabaritoForm(request.POST)
        if form.is_valid():
            gabarito_criado = Gabarito.objects.create(
                nome=form.cleaned_data.get('nome'),
                tamanho=form.cleaned_data.get('tamanho'),
                indice=form.cleaned_data.get('indice'),
                dono=request.user,
            )

            #criacao das questoes do gabarito
            for i in range(0, gabarito_criado.tamanho):
                Questao.objects.create(numero=i, gabarito=gabarito_criado)

            return redirect('pagina_inicial')
        else:
            messages.error(request, 'Um erro ocorreu.')


    # listagem dos gabaritos do usuário
    gabaritos = Gabarito.objects.filter(dono=request.user)

    paginator = Paginator(gabaritos, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    contexto = {
        'form' : form,
        'page_obj': page_obj,
    }
    return render(request, 'gabaritos/pagina_inicial.html', contexto)
