from rest_framework import serializers
from .models import LogAuditoria
from medico.models import Medico
from medico.serializer import MedicoSerializer

class LogAuditoriaSerializer(serializers.ModelSerializer):
    usuario = serializers.SerializerMethodField()  # <- Aquí cambiamos "medico" por "usuario"

    class Meta:
        model = LogAuditoria
        fields = ['id_log', 'fecha_suceso', 'operacion', 'id_usuario', 'usuario']  # <- También aquí

    def get_usuario(self, obj):  # <- Nombre del método debe ser get_<nombre_del_campo>
        try:
            medico = obj.medico
            return MedicoSerializer(medico).data if medico else None
        except:
            return None
