from .models import Sensor, Receiver, SensorSessionToken
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.gis.geos import Point
from django.db import transaction
from django.db.models import Q

def update_sensor_state(sensor_data):
    print("____________________________ update_sensor_state ____________________________", sensor_data)
    "{'ip': '10.0.50.162', 'port': 19010, 'driver_name': 'Grobina', 'user_has_access': False, 'state': 'READY', 'location': 'SRID=4326;POINT (21.077461111 56.501169444)'}"
    if 'longitude' not in sensor_data or 'latitude' not in sensor_data:
        if 'location' in sensor_data:
            try:
                # Parse the WKT string to extract coordinates
                wkt = sensor_data['location']
                # Extract numbers between parentheses
                coords = wkt.split('POINT (')[1].split(')')[0].split()
                longitude = float(coords[0])  # 21.077461111
                latitude = float(coords[1])   # 56.501169444
            except (IndexError, ValueError) as e:
                print(f"Error parsing location coordinates: {e}")
                longitude = None
                latitude = None
        else:
            longitude = None
            latitude = None
    else:
        longitude = sensor_data['longitude']
        latitude = sensor_data['latitude']
    sensor, _ = Sensor.objects.update_or_create(
        ip=sensor_data["ip"],
        port=sensor_data["port"],
        defaults={
            "driver_name": sensor_data["driver_name"],
            "user_has_access": sensor_data["user_has_access"] if 'user_has_access' in sensor_data and sensor_data["user_has_access"] is not None else False,
            "location": Point(longitude, latitude, srid=4326)
        }
    )
    print(f"Sensor updated or created: {sensor}")

    # Then update each receiver
    if 'receivers' in sensor_data:
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
    print(f"Receivers updated or created for sensor: {sensor}")
    return sensor

