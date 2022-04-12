from django.urls import path
from measurement.views import CreateSensor, Measurements

urlpatterns = [
    path('sensors/', CreateSensor.as_view()),
    path('sensorspk/<pk>', CreateSensor.as_view()),
    path('measurements/', Measurements.as_view()),
    path('sensorsmeasur/<pk>', Measurements.as_view()),
]
