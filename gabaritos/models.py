from django.db import models
from django.contrib.auth.models import User
from django.db.models.expressions import OrderBy


ALTERNATIVA_CHOICES = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
]

class Gabarito(models.Model):
    nome = models.CharField(max_length=60)
    tamanho = models.PositiveIntegerField()
    indice = models.PositiveIntegerField(verbose_name='índice')
    criado_em = models.DateTimeField(auto_now_add=True)
    dono = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    
    class Meta:
        ordering = ['-criado_em']


class Questao(models.Model):
    numero = models.PositiveIntegerField(verbose_name='número')
    alternativa = models.CharField(max_length=1, choices=ALTERNATIVA_CHOICES, null=True, blank=True)
    corrigida = models.BooleanField(default=False)
    gabarito = models.ForeignKey(Gabarito, on_delete=models.CASCADE)

    def __str__(self):
        return '' + self.gabarito + ' | Questão ' + str(self.numero)

    
    class Meta:
        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'
        ordering = ['numero']
