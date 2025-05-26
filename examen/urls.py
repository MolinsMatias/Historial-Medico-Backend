from django.contrib import admin
from django.urls import path
from examen import views

urlpatterns = [
    path('', views.ExamenList.as_view()),
    path('<int:hist_medico_id_hist>', views.ExamenDetail.as_view()),
]