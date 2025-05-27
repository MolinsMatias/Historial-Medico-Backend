from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import LogAuditoria
from .serializer import LogAuditoriaSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Solo lectura, ya que generalmente los logs no se crean desde frontend

class LogList(ListCreateAPIView):
    queryset = LogAuditoria.objects.all().order_by('-fecha_suceso')
    serializer_class = LogAuditoriaSerializer

class LogDetail(RetrieveUpdateDestroyAPIView):
    queryset = LogAuditoria.objects.all()
    lookup_field = 'id_log'
    serializer_class = LogAuditoriaSerializer

