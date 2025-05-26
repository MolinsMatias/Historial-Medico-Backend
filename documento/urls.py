from django.contrib import admin
from django.urls import path
from documento import views

urlpatterns = [
    path('', views.DocumentoList.as_view()),
    path('<int:id_documento>', views.DocumentoDetail.as_view()),

    path('hist-medico/<int:hist_medico_id_hist>', views.DocumentoHistorialDetail.as_view()),
]