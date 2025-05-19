from django.urls import path
from .views import ConfigViewSet

urlpatterns = [
    path('init/', ConfigViewSet.as_view({'get': 'list'}), name='config-list')
]