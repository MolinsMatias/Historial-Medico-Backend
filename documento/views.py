from django.shortcuts import render
from .models import Documento
from .serializer import DocumentoSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
# Create your views here.

class DocumentoList(ListCreateAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
     

class DocumentoDetail(ListCreateAPIView):
    serializer_class = DocumentoSerializer

    def get_queryset(self):
        hist_medico_id = self.kwargs['hist_medico_id_hist']
        return Documento.objects.filter(hist_medico_id_hist=hist_medico_id)     