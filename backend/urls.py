
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('api/', include('api.urls')),
    path('api/paciente/', include('paciente.urls')),
    path('api/hist-medico/', include('historialMedico.urls')),
    path('api/consulta-medica/', include('consultaMedica.urls')),
    path('api/examen/', include('examen.urls')),
    path('api/documento/', include('documento.urls')),
    path('api/logs/', include('logs.urls')),
]
