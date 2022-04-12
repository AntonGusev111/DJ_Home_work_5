from rest_framework import serializers
from measurement.models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('name', 'description')


class MeasurmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ('sensor','temperature', 'date_measurement')


class SensorDetailSerializer(serializers.ModelSerializer):
    measurement = MeasurmentSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ('id', 'name', 'description','measurement')
