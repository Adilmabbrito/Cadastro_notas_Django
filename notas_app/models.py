from django.db import models

class Nota(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()

    # Campos para as notas das disciplinas
    nota1_portugues = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    nota2_portugues = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    nota3_portugues = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    nota1_matematica = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    nota2_matematica = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    nota3_matematica = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    nota1_ciencias = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    nota2_ciencias = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    nota3_ciencias = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    nota1_geografia = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    nota2_geografia = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    nota3_geografia = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    nota1_historia = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    nota2_historia = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    nota3_historia = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    nota1_ingles = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    nota2_ingles = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    nota3_ingles = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    nota1_artes = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    nota2_artes = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    nota3_artes = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    media = models.FloatField(null=True, blank=True)
    aprovado = models.BooleanField(null=True, blank=True)
 
    def __str__(self):
        return self.titulo