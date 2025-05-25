from rest_framework import serializers
from .models import HistorialMedico

class HistMedSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialMedico
        fields = '__all__'