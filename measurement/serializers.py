from dataclasses import field
from rest_framework.serializers import ModelSerializer

# TODO: опишите необходимые сериализаторы

from .models import Sensor, Measurement

class SensorSerializer(ModelSerializer):
    class Meta:
        model = Sensor
        fields = "__all__"

class MeasurementSerializer(ModelSerializer):
    class Meta:
        model = Measurement
        fields = fields = "__all__"

class SensorDetailSerializer(ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']