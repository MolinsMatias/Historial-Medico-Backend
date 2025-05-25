from django.contrib import admin
from django.urls import path
from historialMedico import views

urlpatterns = [
    path('hist-medico/', views.HistMedList.as_view()),
    path('hist-medico/<int:id_hist>', views.HistMedDetail.as_view()),
    path('hist-medico/paciente/<int:paciente>', views.HistMedDetailPaciente.as_view()),
]