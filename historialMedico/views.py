from .models import HistorialMedico
from .serializer import HistMedSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

# Create your views here.

class HistMedList(ListCreateAPIView):
    queryset = HistorialMedico.objects.all()
    serializer_class = HistMedSerializer

class HistMedDetail(RetrieveUpdateDestroyAPIView):
    queryset = HistorialMedico.objects.all()
    lookup_field = 'id_hist'
    serializer_class = HistMedSerializer

class HistMedDetailPaciente(ListCreateAPIView):
    serializer_class = HistMedSerializer

    def get_queryset(self):
        paciente_id = self.kwargs.get('paciente')
        return HistorialMedico.objects.filter(paciente_id=paciente_id)
     