from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('prueba/', views.PrubaView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ListarPrueba.as_view()),
    path('add/', views.PruebaCreateView.as_view()),
    path('eliminar-home', views.PruebaDeleteView.as_view()),
    path('resumen-foundation', views.ResumenFoundationView.as_view()),
    path('home1', views.Home1View.as_view()),
]
