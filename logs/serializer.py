from rest_framework import serializers
from .models import LogAuditoria
from medico.models import Medico
from medico.serializer import MedicoSerializer

class LogAuditoriaSerializer(serializers.ModelSerializer):
    usuario = serializers.SerializerMethodField()  # <- Aquí cambiamos "medico" por "usuario"

    class Meta:
        model = LogAuditoria
        fields = '__all__'


