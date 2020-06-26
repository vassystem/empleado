from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
#
from .models import Empleado

# forms

from .forms import EmpleadoForm


class ListAllEmpleado(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    model = Empleado
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        # icontains busca registro
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista


class ListAllEmpleadoAdmin(ListView):
    template_name = 'persona/list_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    model = Empleado
    context_object_name = 'empleados'


class ListByAreaEmpleado(ListView):
    """ Lista de empleados por area"""
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):

        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
            departamento__shor_name=area
        )
        return lista


class ListByTrabajoEmpleado(ListView):
    """ Lista de empleados por area"""
    template_name = 'persona/list_by_trabajo.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            job=palabra_clave
        )

        return lista


class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):

        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )

        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'Habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=4)

        return empleado.Habilidades.all()

# 1. Listar todos los empleados de la empresa
# 2. Listar todos los empleados que pertenecen a una area de la empresa
# 3. Listar empleados por trabajo
# 4. Listar los empleados por palabra clave
# 5. Listar habilidades de un empleado


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context["titulo"] = 'Empleado del mes'
        return context

# Clases para guardar un registro


class InicioView(TemplateView):
    # pagina de inicio
    template_name = "inicio.html"


class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_all_admin')

    def form_valid(self, form):
        # LOGICA DEL PROCESO
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = [
        'first_name',
        'last_name',
        'full_name',
        'job',
        'departamento',
        'Habilidades',
        'avatar'
    ]
    success_url = reverse_lazy('persona_app:empleados_all_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # LOGICA DEL PROCESO
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_all_admin')
