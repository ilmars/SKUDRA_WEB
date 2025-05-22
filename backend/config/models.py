from django.db import models
from setup.model_mixins import TimeStampMixin
from solo.models import SingletonModel  # if using django-solo
from skudra.models import Sensor

class SystemConfiguration(SingletonModel):
    site_name = models.CharField(max_length=100, default="SWEB App")
    maintenance_mode = models.BooleanField(default=False)
    map_tile_url = models.URLField(null=True, blank=True)
    max_sensor_lines = models.PositiveIntegerField(default=10)
    oauth2_client_id = models.CharField(max_length=255, null=True, blank=True)
    oauth2_client_secret = models.CharField(max_length=255, null=True, blank=True)
    oauth2_redirect_uri = models.URLField(null=True, blank=True)
    oauth2_authorization_url = models.URLField(null=True, blank=True)
    oauth2_token_url = models.URLField(null=True, blank=True)
    oauth2_scope = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "System Configuration"
    


class EnvoyConfigLog(TimeStampMixin):
    """
    Logs Envoy configuration changes and restart attempts
    """
    SUCCESS = 'SUCCESS'
    FAILED = 'FAILED'
    VALIDATED = 'VALIDATED'
    STATUS_CHOICES = [
        (SUCCESS, 'Success'),
        (FAILED, 'Failed'),
        (VALIDATED, 'Validated'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    message = models.TextField(blank=True)
    config_snapshot = models.JSONField(null=True, blank=True)
    triggered_by_sensor = models.ForeignKey(
        Sensor, 
        on_delete=models.deletion.SET_NULL,
        null=True, 
        related_name='envoy_logs'
    )

    def __str__(self):
        return f"Envoy Config Change {self.created_at} - {self.status}"