from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'paciente': reverse('paciente-list', request=request, format=format),
        'historial_medico': reverse('historialmedico-list', request=request, format=format),
        'consulta_medica': reverse('consultamedica-list', request=request, format=format),
        'examen': reverse('examen-list', request=request, format=format),
        'documento': reverse('documento-list', request=request, format=format),
        'logs': reverse('logs-list', request=request, format=format),
    })
