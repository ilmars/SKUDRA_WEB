from django.contrib import admin
from solo.admin import SingletonModelAdmin  # Ensure django-solo is installed
from .models import SystemConfiguration, EnvoyConfigLog

admin.site.register(SystemConfiguration, SingletonModelAdmin)
class EnvoyConfigLogAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'status', 'triggered_by_sensor')
    list_filter = ('status',)
    search_fields = ('message',)
admin.site.register(EnvoyConfigLog, EnvoyConfigLogAdmin)