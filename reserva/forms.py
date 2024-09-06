from django import forms
from reserva.models import Reserva

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = ['nome_pet', 'telefone', 'dia_reserva', 'obs',]