from django.urls import path

from .views import (corrigir_gabarito_view, corrigir_questao_view,
                    excluir_gabarito_view, marcar_questao_view,
                    pagina_inicial_view, ver_gabarito_view)

urlpatterns = [
    path('', pagina_inicial_view, name='pagina_inicial'),
    path('gabarito/<int:id>', ver_gabarito_view, name='ver_gabarito'),
    path('gabarito/<int:id>/corrigir', corrigir_gabarito_view, name='corrigir_gabarito'),
    path('gabarito/<int:id>/excluir', excluir_gabarito_view, name='excluir_gabarito'),
    path('gabarito/<str:pagina>/marcar/<int:id>/<str:alternativa>', marcar_questao_view, name='marcar_questao'),
    path('gabarito/<str:pagina>/corrigir/<int:id>/<int:correta>', corrigir_questao_view, name='corrigir_questao'),
]
