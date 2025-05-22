import requests
from django.utils import timezone
from .models import Sensor, SensorUptimeLog
from skudra.grpc.main import update_regular_sensor_states

def update_sensor_status():
    print('____________________________ update_sensor_status ____________________________')
    sensors = Sensor.objects.all()

    # Create a list to store SensorUptimeLog instances
    uptime_logs = []
    for sensor in sensors:
        data = update_regular_sensor_states(sensor.ip, sensor.port)
        sensor.state = data.get("state", "UNKNOWN")
        sensor.updated_at = timezone.now()
        sensor.save()
        print(sensor.driver_name, sensor.ip, sensor.port, data)
        
        # Add to the list instead of creating immediately
        uptime_logs.append(SensorUptimeLog(
            sensor=sensor, state=data.get('state', 'UNKNOWN'), updated_at=timezone.now()
        ))
    if uptime_logs:
        SensorUptimeLog.objects.bulk_create(uptime_logs)
    

    uptime_logs.clear()
        
        
        # SensorUptimeLog.objects.create(
        #     sensor=sensor, state=data['state'], updated_at=timezone.now()
        # try:
        #     # Set a timeout (e.g., 5 seconds) to avoid long hangs
        #     response = requests.get(url, timeout=5)
        #     response.raise_for_status()  # Raise an exception for HTTP errors
        #     data = response.json()
        #     # Update sensor fields based on the response; adjust field names accordingly
        #     sensor.state = data.get("state", "UNKNOWN")
        #     sensor.updated_at = timezone.now()
        #     sensor.save()
        # except requests.Timeout:
        #     # If a timeout occurs, mark sensor as unreachable
        #     sensor.state = "UNREACHABLE"
        #     sensor.save()
        # except requests.RequestException as e:
        #     # Log other errors and mark as error
        #     sensor.state = "ERROR"
        #     sensor.save()
