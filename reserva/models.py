from django.db import models

class Reserva(models.Model):

    nome_pet = models.CharField('Nome Pet', max_length=50)
    telefone = models.CharField('Telefone', max_length=13)
    dia_reserva = models.DateField('Dia Reserva')
    obs = models.TextField('Observações', blank=True)