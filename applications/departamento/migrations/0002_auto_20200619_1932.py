# Generated by Django 3.0.7 on 2020-06-20 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(editable=False, max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='shor_name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Nombre Corto'),
        ),
    ]
