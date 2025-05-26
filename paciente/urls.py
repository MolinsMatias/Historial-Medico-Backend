from django.contrib import admin
from django.urls import path
from paciente import views

urlpatterns = [
    path('', views.PacienteList.as_view()),
    path('<int:id_pac>', views.PacienteDetail.as_view()),
]