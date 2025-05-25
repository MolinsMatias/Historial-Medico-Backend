from rest_framework import serializers
from .models import Consulta

class ConsultaMedSerializer(serializers.ModelSerializer):
    nombre_medico = serializers.SerializerMethodField()
    run_paciente = serializers.SerializerMethodField()
    class Meta:
        model = Consulta
        fields = '__all__'  # Incluye todos los campos del modelo
        # Agrega el campo personalizado:
        extra_fields = ['nombre_medico', 'run_paciente']

    def get_nombre_medico(self, obj):
        if obj.medico:
            return f"{obj.medico.nombre} {obj.medico.apellido}"
        return None
    
    def get_run_paciente(self, obj):
        if obj.historial_medico and obj.historial_medico.paciente:
            return obj.historial_medico.paciente.id_pac 
        return None

