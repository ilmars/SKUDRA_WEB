from rest_framework import serializers

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import transaction

from rest_framework.exceptions import ValidationError
from django.db.models import Q

from .models import Sensor, Receiver, SensorSessionToken
from .helpers import update_sensor_state

class ReceiverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Receiver
        fields = ('guid', 'name', 'state', 'type', 'sensor_id')
        read_only_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

    def create(self, validated_data):
        return super().create(validated_data)
        # Create the sensor instance
        
class SensorSerializer(serializers.HyperlinkedModelSerializer):

    coordinates = serializers.SerializerMethodField()
    receivers = ReceiverSerializer(many=True, read_only=True)
    
    class Meta:
        model = Sensor
        fields = ('url', 'id', 'ip', 'port', 'driver_name', 'user_has_access', 'state', 
                  'location', 'coordinates', 'receivers')
        read_only_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
        
    def get_longitude(self, obj):
        return obj.longitude()
    def get_latitude(self, obj):
        return obj.latitude()

    def get_coordinates(self, obj):
        return obj.get_coordinates()

    def create(self, validated_data):
        update_sensor_state(validated_data)
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        # Update the sensor instance with the new data
        update_sensor_state(validated_data)
        return super().update(instance, validated_data)
        


class SensorSessionTokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorSessionToken
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

    def create(self, validated_data):
        return super().create(validated_data)
        # Create the sensor instances