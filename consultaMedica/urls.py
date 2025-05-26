from django.contrib import admin
from django.urls import path
from consultaMedica import views

urlpatterns = [
    path('', views.ConsultaMedList.as_view()),
    path('<int:id_cons>', views.ConsultaMedDetail.as_view()),
    path('historial/<int:historial_medico>', views.ConsultaMedDetailHistorial.as_view()),
]