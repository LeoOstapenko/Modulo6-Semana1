# Generated by Django 4.2.4 on 2024-07-13 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pet', models.CharField(max_length=50, verbose_name='Nome Pet')),
                ('telefone', models.CharField(max_length=13, verbose_name='Telefone')),
                ('dia_reserva', models.DateField(verbose_name='Dia Reserva')),
                ('obs', models.TextField(blank=True, verbose_name='Observações')),
            ],
        ),
    ]
