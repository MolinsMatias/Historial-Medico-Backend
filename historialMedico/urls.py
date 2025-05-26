from django.contrib import admin
from django.urls import path
from historialMedico import views

urlpatterns = [
    path('', views.HistMedList.as_view()),
    path('<int:id_hist>', views.HistMedDetail.as_view()),
    path('paciente/<int:paciente>', views.HistMedDetailPaciente.as_view()),
    path('medico/<int:paciente_medico>', views.HistMedDetailMedico.as_view()),
]