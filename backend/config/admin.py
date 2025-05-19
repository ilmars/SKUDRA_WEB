from django.contrib import admin
from solo.admin import SingletonModelAdmin  # Ensure django-solo is installed
from .models import SystemConfiguration

admin.site.register(SystemConfiguration, SingletonModelAdmin)