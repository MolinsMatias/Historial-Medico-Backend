from django.contrib import admin
from django.urls import path
from examen import views

urlpatterns = [
    path('examen/', views.ExamenList.as_view()),
    path('examen/<int:hist_medico_id_hist>', views.ExamenDetail.as_view()),
]