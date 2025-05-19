from django.db import models
from solo.models import SingletonModel  # if using django-solo

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
    
