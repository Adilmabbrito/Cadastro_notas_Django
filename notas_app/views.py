from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Nota
from .forms import NotaForm

def lista_notas(request):
    notas = Nota.objects.all()
    return render(request, 'notas_app/lista_notas.html', {'notas': notas})


def cadastrar_notas(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            nota = form.save(commit=False)

            # Adicione aqui a lógica para calcular a média e verificar a aprovação
            nota.media = (nota.nota_portugues_1 + nota.nota_portugues_2 + nota.nota_portugues_3) / 3.0
            nota.aprovado = nota.media >= 7.0

            nota.save()
            return redirect('lista_notas')
    else:
        form = NotaForm()

    return render(request, 'notas_app/cadastrar_notas.html', {'form': form})