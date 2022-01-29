# Generated by Django 3.2.11 on 2022-01-29 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OperatorCondom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rg', models.CharField(max_length=9)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=14)),
                ('name', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('create', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('permissions', models.TextField()),
                ('administratorSystem', models.BooleanField()),
            ],
        ),
    ]
