from django.urls import include,  re_path
from rest_framework.routers import DefaultRouter
from .views import SensorViewSet, ReceiverViewSet, SensorSessionTokenViewSet


router = DefaultRouter()
router.register(r'instances', SensorViewSet)
router.register(r'receivers', ReceiverViewSet)
router.register(r'sensor_session_tokens', SensorSessionTokenViewSet)


urlpatterns = [
    re_path(r'^', include(router.urls)),
]
