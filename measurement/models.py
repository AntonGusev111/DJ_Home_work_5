from django.db import models



class Sensor(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=150)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')
    temperature = models.DecimalField(max_digits=10, decimal_places=1)
    date_measurement = models.DateField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True)
