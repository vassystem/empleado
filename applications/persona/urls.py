from django.contrib import admin
from django.urls import path

from . import views

app_name = 'persona_app'


urlpatterns = [
    path(
        '',
        views.InicioView.as_view(),
        name='Pagina_Inicio'
    ),
    path(
        'listar-todo-empleados/',
        views.ListAllEmpleado.as_view(),
        name='empleados_all'
    ),
    path(
        'listar-empleado-admin/',
        views.ListAllEmpleadoAdmin.as_view(),
        name='empleados_all_admin'
    ),
    path(
        'lista-by-area/<shortname>',
        views.ListByAreaEmpleado.as_view(),
        name='empleados_area'
    ),
    path(
        'buscar-empleado/',
        views.ListEmpleadosByKword.as_view()
    ),
    path(
        'listar-habilidades-empleado/',
        views.ListHabilidadesEmpleado.as_view()
    ),
    path(
        'ver-empleado/<pk>',
        views.EmpleadoDetailView.as_view(),
        name='empleado_detail'
    ),
    path(
        'ver-empleado-trabajo/',
        views.ListByTrabajoEmpleado.as_view()
    ),
    path(
        'add-empleado/',
        views.EmpleadoCreateView.as_view(),
        name='empleado_add'
    ),
    path(
        'success/',
        views.SuccessView.as_view(),
        name='correcto'
    ),
    path(
        'update-empleado/<pk>/',
        views.EmpleadoUpdateView.as_view(),
        name='actualizar_empleado'
    ),
    path(
        'delete-empleado/<pk>/',
        views.EmpleadoDeleteView.as_view(),
        name='eliminar_empleado'
    ),
]
