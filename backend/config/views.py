from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CurrentUserSerializer


class ConfigViewSet(ViewSet):
    def list(self, request):
        from .models import SystemConfiguration
        from .serializers import SystemConfigurationSerializer
        config = SystemConfiguration.get_solo()  # django-solo usage
        serializer = SystemConfigurationSerializer(config)
        return Response(serializer.data)

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        data = CurrentUserSerializer(request.user).data
        return Response(data)