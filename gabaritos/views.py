from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse

from .forms import CriarGabaritoForm, RenomearGabaritoForm
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
                Questao.objects.create(numero=gabarito_criado.indice+i, gabarito=gabarito_criado)

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


@login_required
def ver_gabarito_view(request, id):
    gabarito = get_object_or_404(Gabarito, id=id)

    if gabarito is not None and gabarito.dono == request.user:
        # renomear gabarito
        form = RenomearGabaritoForm()
        if request.method == 'POST':
            form = RenomearGabaritoForm(request.POST)
            if form.is_valid():
                nome_antigo = gabarito.nome
                nome_novo= form.cleaned_data.get('nome')
                gabarito.nome = nome_novo
                gabarito.save()
                
                msg = 'Gabarito renomeado de "' + nome_antigo + '" para "' + nome_novo + '".'
                messages.success(request, msg)
            return redirect('ver_gabarito', id)

        # listagem de gabarito/questões
        paginator = Paginator(gabarito.questao_set.all(), 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        contexto = {
            'form' : form,
            'gabarito' : gabarito,
            'page_obj' : page_obj,
        }
        
        return render(request, 'gabaritos/gabarito.html', contexto)

    messages.error(request, 'O gabarito não existe.')
    return redirect('pagina_inicial')


@login_required
def excluir_gabarito_view(request, id):
    gabarito = get_object_or_404(Gabarito, id=id)

    if gabarito is not None and gabarito.dono == request.user:
        gabarito.delete()
        messages.success(request, 'Gabarito excluído com sucesso.')
        return redirect('pagina_inicial')

    messages.error(request, 'O gabarito não existe.')
    return redirect('pagina_inicial')


@login_required
def marcar_questao_view(request, id, alternativa):
    questao = get_object_or_404(Questao, id=id)

    if questao.gabarito.dono == request.user and not questao.corrigida:
        # verifica se foi passada uma alternativa válida
        if alternativa in ['A', 'B', 'C', 'D', 'E']:
            # adiciona a contagem de questões feitas
            if questao.alternativa == None: # verifica se já havia sido marcada para não contar repetido
                gabarito = Gabarito.objects.get(id=questao.gabarito.id)
                gabarito.feitas += 1
                gabarito.save()

            # marca a alternativa no banco de dados
            questao.alternativa = alternativa
            questao.save()

    html = render_to_string('gabaritos/render_alternativas.html', {'questao': questao}, request)
    return JsonResponse({'html' : html})


@login_required
def corrigir_gabarito_view(request, id):
    gabarito = get_object_or_404(Gabarito, id=id)

    if gabarito is not None and gabarito.dono == request.user:
        paginator = Paginator(gabarito.questao_set.all(), 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        contexto = {
            'gabarito': gabarito,
            'page_obj' : page_obj,
        }

        return render(request, 'gabaritos/corrigir_gabarito.html', contexto)

    messages.error(request, 'Gabarito não encontrado')
    return redirect('pagina_inicial')


@login_required
def corrigir_questao_view(request, pagina, id, correta):
    questao = get_object_or_404(Questao, id=id)

    if questao.gabarito.dono == request.user and not questao.corrigida:
        # adiciona a contagem de questões corrigidas
        if questao.corrigida == False: # verifica se já havia sido corrigida para não contar repetido
            if correta in [0, 1]:
                gabarito = Gabarito.objects.get(id=questao.gabarito.id)
                gabarito.corrigidas += 1

                if correta == 1:
                    questao.acertada = True
                    gabarito.acertadas +=1
                else:
                    questao.acertada = False

                questao.corrigida = True
                questao.save()
                gabarito.save()
            else:
                messages.error(request, 'Erro na correção.')

    # gera a url com a paginação da questao que está sendo alterada
    url_base = reverse(corrigir_gabarito_view, args=(questao.gabarito.id,))

    parametros = 'page=' + pagina
    url = '{}?{}'.format(url_base, parametros)
    return redirect(url)
