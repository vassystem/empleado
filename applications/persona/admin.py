from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.

admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )
   #

    def full_name(self, obj):
        # toda la operacion que necesite
        # print(obj.first_name)
        return obj.first_name + ' ' + obj.last_name

    #
    search_fields = ('first_name',)
    list_filter = ('departamento', 'job', 'Habilidades')
    #
    filter_horizontal = ('Habilidades',)


admin.site.register(Empleado, EmpleadoAdmin)
