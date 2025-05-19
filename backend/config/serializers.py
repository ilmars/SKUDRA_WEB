from rest_framework import serializers
from config.models import SystemConfiguration

class SystemConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemConfiguration
        fields = '__all__'