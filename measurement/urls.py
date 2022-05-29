from django.urls import path

from .views import SensorsAPIListCreate, SensorAPIRetrieveUpdate, MeasurementAPICreate

urlpatterns = [
    path('sensors/', SensorsAPIListCreate.as_view()),
    path('sensors/<pk>/', SensorAPIRetrieveUpdate.as_view()),
    path('measurements/', MeasurementAPICreate.as_view())
]
