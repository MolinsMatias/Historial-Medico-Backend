from django.shortcuts import render
from .models import Paciente
from .serializer import PacienteSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
# Create your views here.

class PacienteList(ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteDetail(RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    lookup_field = 'id_pac'
    serializer_class = PacienteSerializer      