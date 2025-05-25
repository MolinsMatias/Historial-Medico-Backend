from django.shortcuts import render
from .models import Examen
from .serializer import ExamenSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
# Create your views here.

class ExamenList(ListCreateAPIView):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer

class ExamenDetail(ListCreateAPIView):
    serializer_class = ExamenSerializer

    def get_queryset(self):
        hist_medico_id = self.kwargs['hist_medico_id_hist']
        return Examen.objects.filter(hist_medico_id_hist=hist_medico_id)     