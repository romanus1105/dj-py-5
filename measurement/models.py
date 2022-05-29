from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=256, unique=True)

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=3, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)