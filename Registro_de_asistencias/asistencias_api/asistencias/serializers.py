from rest_framework import serializers
from .models import Asistencia

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'

    def validate(self, data):
        if data.get('hora_entrada') and data.get('hora_salida'):
            raise serializers.ValidationError("Solo se puede registrar la hora de entrada o la hora de salida, no ambas.")
        return data
