from .models import Sensor, Receiver, SensorSessionToken
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.gis.geos import Point
from django.db import transaction
from django.db.models import Q

def update_sensor_state(sensor_data):
    sensor, _ = Sensor.objects.update_or_create(
        ip=sensor_data["ip"],
        port=sensor_data["port"],
        defaults={
            "driver_name": sensor_data["driver_name"],
            "user_has_access": sensor_data["user_has_access"],
            "location": Point(sensor_data["longitude"], sensor_data["latitude"], srid=4326)
        }
    )

    # Then update each receiver
    for r in sensor_data["receivers"]:
        Receiver.objects.update_or_create(
            sensor=sensor,
            receiver_id=r["id"],
            defaults={
                "name": r["name"]["value"],
                "state": r["state"],
                "type": r["type"],
            }
        )

