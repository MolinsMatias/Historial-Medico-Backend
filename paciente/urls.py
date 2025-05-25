from django.contrib import admin
from django.urls import path
from paciente import views

urlpatterns = [
    path('paciente/', views.PacienteList.as_view()),
    path('paciente/<int:id_pac>', views.PacienteDetail.as_view()),
]