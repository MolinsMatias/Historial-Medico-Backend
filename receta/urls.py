from django.contrib import admin
from django.urls import path
from receta import views

# receta/urls.py
urlpatterns = [
    path('', views.RecetaList.as_view()),
    path('<int:id_rece>', views.RecetaDetail.as_view()),
    path('consulta-medica/<int:consulta_medica_id_cons>', views.RecetaConsultalDetail.as_view()),
    path('detalle/', views.DetalleRecetaListCreate.as_view(), name='detalle-receta'),  # /api/receta/detalle/
    path('detalle/<int:receta_id_rece>', views.DetalleRecetaDetail.as_view(), name='detalle-receta'),  # /api/receta/detalle/
]