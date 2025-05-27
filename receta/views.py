from django.shortcuts import render
from .models import Receta , DetalleReceta
from .serializer import RecetaSerializer , DetalleRecetaSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
# Create your views here.

class RecetaList(ListCreateAPIView):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer
     

class RecetaDetail(RetrieveUpdateDestroyAPIView):
    queryset = Receta.objects.all()
    lookup_field = 'id_rece'
    serializer_class = RecetaSerializer

class RecetaConsultalDetail(ListCreateAPIView):
    serializer_class = RecetaSerializer

    def get_queryset(self):
        consulta_medica_id_cons = self.kwargs['consulta_medica_id_cons']
        return Receta.objects.filter(consulta_medica_id_cons=consulta_medica_id_cons)     
    
class DetalleRecetaListCreate(ListCreateAPIView):
    queryset = DetalleReceta.objects.all()
    serializer_class = DetalleRecetaSerializer

class DetalleRecetaDetail(RetrieveUpdateDestroyAPIView):
    queryset = DetalleReceta.objects.all()
    lookup_field = 'id_det'
    serializer_class = DetalleRecetaSerializer

class DetalleRecetaDetailReceta(ListCreateAPIView):
    serializer_class = DetalleRecetaSerializer

    def get_queryset(self):
        receta_id_rece = self.kwargs.get('receta_id_rece')
        return DetalleReceta.objects.filter(receta_id_rece=receta_id_rece)
