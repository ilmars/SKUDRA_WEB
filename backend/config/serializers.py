from rest_framework import serializers
from config.models import SystemConfiguration
from django.contrib.auth.models import User

class SystemConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemConfiguration
        fields = '__all__'



class CurrentUserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="get_full_name", read_only=True)
    groups     = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )
    isAdmin    = serializers.BooleanField(source="is_staff", read_only=True)

    class Meta:
        model  = User
        fields = ("username", "full_name", "groups", "isAdmin")