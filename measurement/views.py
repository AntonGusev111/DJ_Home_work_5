from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from measurement.serializers import SensorSerializer, MeasurmentSerializer, SensorDetailSerializer
from measurement.models import Sensor, Measurement



class CreateSensor(APIView):

    def get(self, request):
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('sensor create!', status=status.HTTP_200_OK)

    def patch(self, request, pk):
        sensor = Sensor.objects.filter(id=pk)
        old_desc = sensor.values()[0].get("description")
        sensor.update(description=request.data.get('description'))
        return Response(
            f'датчик {sensor.values()[0].get("name")} изменен с {old_desc} на {request.data.get("description")}',
            status=status.HTTP_200_OK)


class Measurements(APIView):
    def get(self, request, pk):
        sensor = Sensor.objects.select_related().get(id=pk)
        serializer = SensorDetailSerializer(sensor)
        return Response(serializer.data)

    def post(self, request):
        measurement = MeasurmentSerializer(data=request.data)
        measurement.is_valid(raise_exception=True)
        measurement.save()
        return Response("measurement add")
