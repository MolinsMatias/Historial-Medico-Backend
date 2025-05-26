from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def api_overview(request):
    routes = {
        "Paciente": "/api/paciente/",
        "Historial Médico": "/api/hist-medico/",
        "Consulta Médica": "/api/consulta-medica/",
        "Examen": "/api/examen/",
        "Documento": "/api/documento/",
        "Logs": "/api/logs/",
    }
    return JsonResponse(routes)
