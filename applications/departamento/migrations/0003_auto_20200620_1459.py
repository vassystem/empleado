# Generated by Django 3.0.7 on 2020-06-20 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_auto_20200619_1932'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['name'], 'verbose_name': 'Mi Departamento', 'verbose_name_plural': 'Areas de las Empresa'},
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'shor_name')},
        ),
    ]