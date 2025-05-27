from django.contrib import admin
from django.urls import path
from receta import views

urlpatterns = [
    path('', views.RecetaList.as_view()),
    path('<int:id_rece>', views.RecetaDetail.as_view()),

    path('consulta-medica/<int:consulta_medica_id_cons>', views.RecetaConsultalDetail.as_view()),
]