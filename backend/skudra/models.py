from setup.model_mixins import TimeStampMixin, TimeStampUserMixin
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from google.protobuf.json_format import MessageToDict

from django.contrib.auth import get_user_model
# from skudra.grpc.main import handshake
from skudra.grpc.main import firstInit
from django.utils import timezone
import uuid

User = get_user_model()

class Sensor(TimeStampUserMixin):
    """
    Represents a physical sensor device.
    """
    ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=True)
    port = models.PositiveIntegerField()
    driver_name = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=50, blank=True)  # e.g. READY, DISABLED, etc.
    last_state_ready = models.DateTimeField(auto_now_add=True)
    
    # GeoDjango field to store location as a Point (lat, lon)
    # e.g., Point(21.77461111, 56.501169444, srid=4326)
    location = models.PointField(srid=4326, null=True, blank=True)
    
    # This might reflect whether the *current* user in context can access it,
    # or you can store it if the handshake returns user_has_access at a device level
    user_has_access = models.BooleanField(default=False)
    token = models.CharField(max_length=200)
    analysis_credentials = models.JSONField(null=True, blank=True)
    
    def longitude(self):
        """
        Returns the longitude of the sensor location.
        """
        return self.location.x if self.location else None
    longitude.short_description = 'Longitude'
    longitude.admin_order_field = 'location__x'
    def latitude(self):
        """
        Returns the latitude of the sensor location.
        """
        return self.location.y if self.location else None
    latitude.short_description = 'Latitude'
    latitude.admin_order_field = 'location__y'
    
    

    def get_coordinates(self):
        """
        Returns the coordinates of the sensor location as a tuple (longitude, latitude).
        """
        return (self.longitude(), self.latitude()) if self.location else (None, None)

    def sensor_first_init(self):
        sensor_fields = firstInit(self)
        print(f"Initializing sensor: {sensor_fields}")
        
        self.state = sensor_fields['state']
        
        if sensor_fields['state'] == 'READY':
            self.last_state_ready = timezone.now()
            self.driver_name = sensor_fields['driver_name']
            self.user_has_access = sensor_fields['user_has_access']
            self.token = sensor_fields['frontendToken']
            self.analysis_credentials = sensor_fields['analysisCredentials']
            self.location = Point(
                float(sensor_fields['longitude']), 
                float(sensor_fields['latitude']), 
                srid=4326
            )
            receivers = self.receivers
            # Process receivers data
            if 'receivers' in sensor_fields:
                # Create or update receiver objects using update_or_create method
                current_receiver_ids = []
                
                for receiver_data in sensor_fields['receivers']:
                    receiver_id = receiver_data['id']
                    current_receiver_ids.append(receiver_id)
                    
                    # Update or create receiver
                    print('—_____________________ receiver_data', receiver_data)
                    recivertype=receiver_data.get('type', '')
                    receiver, created = Receiver.objects.update_or_create(
                        sensor=self,
                        receiver_id=receiver_id,
                        defaults={
                            'name': receiver_data['name'],
                            'state': receiver_data['state'],
                            'type': recivertype
                        }
                    )
                
                # Remove receivers that no longer exist in the sensor_fields
                self.receivers.exclude(receiver_id__in=current_receiver_ids).delete()

    def save(self, *args, **kwargs):
        if not self.pk and self.state:
            self.sensor_first_init()
        super().save(*args, **kwargs)

    class Meta:
        # Ensure unique combo of IP + port
        unique_together = ('ip', 'port')
    
    def __str__(self):
        return f"Sensor {self.driver_name} ({self.ip}:{self.port})"
    
class Receiver(TimeStampMixin):
    """
    Represents each 'receiver' from the handshake data for a given sensor.
    e.g. EB500, ESMD, ESMB with ID, state, type, etc.
    """
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='receivers')
    receiver_id = models.PositiveIntegerField()
    name = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=50, blank=True)  # e.g. READY, DISABLED, etc.
    type = models.CharField(max_length=50, blank=True)   # e.g. EB500, ESMD

    class Meta:
        # If 'receiver_id' is unique only per sensor, add a uniqueness constraint:
        unique_together = ('sensor', 'receiver_id')

    def __str__(self):
        return f"Receiver {self.name} (ID: {self.receiver_id}) - {self.sensor}"
    
class SensorSessionToken(TimeStampMixin):
    """
    A per-user, per-receiver token with an expiration.
    Multiple tokens can exist for the same receiver if multiple users 
    or the same user opens multiple sessions (your call).
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sensor_tokens')
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE, related_name='session_tokens')
    
    token = models.CharField(max_length=200)
    expires_at = models.DateTimeField(null=True, blank=True)
    
    # Optionally track if revoked
    revoked = models.BooleanField(default=False)
    revoked_forced = models.BooleanField(default=False)
    revoked_forced_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='revodekd_tokens', null=True, blank=True)
    revoked_forced_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        # If you want to allow multiple tokens for the same user+receiver, remove this.
        # If you only allow one active token per user+receiver, use unique_together:
        # unique_together = ('user', 'receiver')
        pass

    def __str__(self):
        return f"Token for {self.user} on Receiver {self.receiver_id}"

class SensorUptimeLog(TimeStampMixin):
    """
    Represents a log entry for sensor uptime status.
    """
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='uptime_logs')
    state = models.CharField(max_length=50, blank=True)  # e.g. READY, DISABLED, etc.

    def __str__(self):
        return f"{self.state} - {self.sensor}"