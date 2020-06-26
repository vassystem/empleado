from django.db import models
#
from applications.departamento.models import Departamento

from ckeditor.fields import RichTextField


class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad

# Create your models here.


class Empleado(models.Model):
    """Modelo para tabla empleado"""

    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('3', 'Economista'),
        ('4', 'Otro')
    )
    # Contador
    # Administrador
    # Economista
    # Otro
    first_name = models.CharField(
        'Nombres',
        max_length=50)
    last_name = models.CharField(
        'apellidos',
        max_length=50
    )
    full_name = models.CharField(
        'Nombres completos',
        max_length=120,
        blank=True
    )
    job = models.CharField(
        'trabajo',
        max_length=1,
        choices=JOB_CHOICES
    )
    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.CASCADE
    )
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    Habilidades = models.ManyToManyField(
        Habilidades
    )
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Mi Empresa'
        verbose_name_plural = 'Areas de los Empleados'
        ordering = ['first_name']
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
