from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class ConfigViewSet(ViewSet):
    def list(self, request):
        from .models import SystemConfiguration
        from .serializers import SystemConfigurationSerializer
        config = SystemConfiguration.get_solo()  # django-solo usage
        serializer = SystemConfigurationSerializer(config)
        return Response(serializer.data)