from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Sensor, Receiver, SensorSessionToken, SensorUptimeLog

@admin.register(Sensor)
class SensorAdmin(LeafletGeoAdmin):
    list_display = ('driver_name', 'ip', 'port', 'state', 'last_state_ready', 'user_has_access', 'location', 'updated_at')
    search_fields = ('driver_name', 'ip')
    list_filter = ('state', 'driver_name')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Admin-only call to sensor_first_init
        obj.sensor_first_init()
        obj.save()

@admin.register(SensorUptimeLog)
class SensorUptimeLogAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'state', 'updated_at')
    search_fields = ('sensor', 'state')
    list_filter = ('sensor__driver_name', 'state')
    
@admin.register(Receiver)
class ReceiverAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'receiver_id', 'name', 'state', 'type')
    search_fields = ('receiver_id', 'name')
    list_filter = ('state', 'sensor', 'name')

@admin.register(SensorSessionToken)
class SensorSessionTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'receiver', 'token', 'expires_at', 'revoked')
    search_fields = ('token', 'user__username', 'receiver__receiver_id')
    list_filter = ('revoked', 'receiver', 'user')
    readonly_fields = ('token', 'expires_at')