# forms.py
from django import forms
from .models import Nota

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['nota1_portugues', 'nota2_portugues', 'nota3_portugues',
                  'nota1_matematica', 'nota2_matematica', 'nota3_matematica',
                  # Adicione os campos de nota para outras disciplinas aqui
                  'nota1_ciencias', 'nota2_ciencias', 'nota3_ciencias',
                  'nota1_geografia', 'nota2_geografia', 'nota3_geografia',
                  'nota1_historia', 'nota2_historia', 'nota3_historia',
                  'nota1_ingles', 'nota2_ingles', 'nota3_ingles',
                  'nota1_artes', 'nota2_artes', 'nota3_artes',
                  'media', 'aprovado']
