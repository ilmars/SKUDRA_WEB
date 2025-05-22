from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from skudra.models import Sensor
from config.services.envoy import EnvoyConfigManager

@receiver([post_save, post_delete], sender=Sensor)
def handle_sensor_changes(sender, instance=None, created=False, **kwargs):
    """
    Update Envoy configuration when Sensors are modified
    """
    # Generate new config
    print('_____________________________ handle_sensor_changes _____________________________')
    config = EnvoyConfigManager.generate_config()
    
    # Update Envoy with new config
    success, message = EnvoyConfigManager.update_config(
        config,
        triggered_by_sensor=instance if not kwargs.get('raw', False) else None
    )
    if not success:
        # You might want to add additional error handling here
        print(f"Failed to update Envoy config: {message}")