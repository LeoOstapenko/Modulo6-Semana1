from django.shortcuts import render
from reserva.forms import ReservaForm

def reserva(request):
    contexto = {'sucesso': False}
    form = ReservaForm(request.POST or None)
    if form.is_valid():
        form.save()
        contexto['sucesso'] = True
    contexto['form'] = form
    return render(request, 'reserva.html', contexto)
