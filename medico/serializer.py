from rest_framework import serializers
from medico.models import Medico

class MedicoSerializer(serializers.ModelSerializer):
    especialidad_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Medico
        fields = ['id_med', 'nombre', 'apellido', 'especialidad_nombre']  # Incluye el campo calculado

    def get_especialidad_nombre(self, obj):
        if obj.especialidad:
            return obj.especialidad.nombre
        return None
