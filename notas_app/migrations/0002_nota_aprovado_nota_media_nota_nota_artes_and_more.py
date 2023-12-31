# Generated by Django 5.0 on 2023-12-28 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nota',
            name='aprovado',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nota',
            name='media',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nota',
            name='nota_artes',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='nota',
            name='nota_ciencias',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='nota',
            name='nota_geografia',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='nota',
            name='nota_historia',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='nota',
            name='nota_ingles',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='nota',
            name='nota_matematica',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='nota',
            name='nota_portugues',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
