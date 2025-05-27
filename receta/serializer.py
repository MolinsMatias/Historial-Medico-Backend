from rest_framework import serializers
from .models import Receta , DetalleReceta

class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = '__all__'

class DetalleRecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleReceta
        fields = '__all__'


