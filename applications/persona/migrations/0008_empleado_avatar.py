# Generated by Django 3.0.7 on 2020-06-26 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0007_empleado_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
    ]
