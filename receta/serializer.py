from rest_framework import serializers
from .models import Medicamento, Receta , DetalleReceta

class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = '__all__'

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'

class DetalleRecetaSerializer(serializers.ModelSerializer):  
    nombre_medicamento = serializers.SerializerMethodField()
    class Meta:
        model = DetalleReceta
        fields = '__all__'
        extra_fields = ['nombre_medicamento']

    def get_nombre_medicamento(self, obj):
        if obj.medicamento_id_medica:
            return f"{obj.medicamento_id_medica.nom_medica}"
        return None



