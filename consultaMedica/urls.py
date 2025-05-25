from django.contrib import admin
from django.urls import path
from consultaMedica import views

urlpatterns = [
    path('consulta-medica/', views.ConsultaMedList.as_view()),
    path('consulta-medica/<int:id_cons>', views.ConsultaMedDetail.as_view()),
    path('consulta-medica/historial/<int:historial_medico>', views.ConsultaMedDetailHistorial.as_view()),
]