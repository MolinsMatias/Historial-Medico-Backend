from django.contrib import admin
from django.urls import path
from documento import views

urlpatterns = [
    path('documento/', views.DocumentoList.as_view()),
    path('documento/<int:hist_medico_id_hist>', views.DocumentoDetail.as_view()),
]