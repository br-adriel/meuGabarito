# Generated by Django 3.2.7 on 2021-09-22 02:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gabarito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('tamanho', models.PositiveIntegerField()),
                ('indice', models.PositiveIntegerField(verbose_name='índice')),
                ('feitas', models.PositiveIntegerField(default=0)),
                ('acertadas', models.PositiveIntegerField(default=0)),
                ('corrigidas', models.PositiveIntegerField(default=0)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('dono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-criado_em'],
            },
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(verbose_name='número')),
                ('alternativa', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1, null=True)),
                ('corrigida', models.BooleanField(default=False)),
                ('acertada', models.BooleanField(blank=True, null=True)),
                ('gabarito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gabaritos.gabarito')),
            ],
            options={
                'verbose_name': 'Questão',
                'verbose_name_plural': 'Questões',
                'ordering': ['numero'],
            },
        ),
    ]
