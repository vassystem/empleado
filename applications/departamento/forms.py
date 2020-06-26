from django import forms


class NewDepartamentoForm(forms.Form):
    """NewDepartamentoForm definition."""

    # TODO: Define form fields here
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    shorname = forms.CharField(max_length=20)
