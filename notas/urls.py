from django.urls import path
from notas_app.views import lista_notas, cadastrar_notas

urlpatterns = [
    path('notas/', lista_notas, name='lista_notas'),  # Verifique se essa linha está correta
    path('notas/cadastrar/', cadastrar_notas, name='cadastrar_notas'),  # Verifique se essa linha está correta
]
