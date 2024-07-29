from rest_framework import serializers
from .models import FlightStatus

class FlightStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightStatus
        fields = '__all__'
