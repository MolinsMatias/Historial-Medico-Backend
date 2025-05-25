from django.shortcuts import render
from .models import Consulta
from .serializer import ConsultaMedSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
# Create your views here.

class ConsultaMedList(ListCreateAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaMedSerializer

class ConsultaMedDetail(RetrieveUpdateDestroyAPIView):
    queryset = Consulta.objects.all()
    lookup_field = 'id_cons'
    serializer_class = ConsultaMedSerializer

class ConsultaMedDetailHistorial(ListCreateAPIView):
    serializer_class = ConsultaMedSerializer

    def get_queryset(self):
        id_historial = self.kwargs.get('historial_medico')
        return Consulta.objects.filter(historial_medico=id_historial)
     