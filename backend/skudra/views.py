from django.shortcuts import render
from .models import Sensor, Receiver, SensorSessionToken
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import transaction
from .serializers import SensorSerializer, ReceiverSerializer, SensorSessionTokenSerializer

# Create your views here.
class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    # permission_classes = [IsAuthenticated]
    # Remove the permission_classes requirement to allow any request
    permission_classes = []
    

    @action(detail=True, methods=['get'])
    def get_receivers(self, request, pk=None):
        sensor = self.get_object()
        receivers = sensor.receivers.all()
        serializer = ReceiverSerializer(receivers, many=True)
        return Response(serializer.data)

class ReceiverViewSet(viewsets.ModelViewSet):
    queryset = Receiver.objects.all()
    serializer_class = ReceiverSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = []
    def get_queryset(self):
        queryset = super().get_queryset()
        sensor_id = self.request.query_params.get('sensor_id', None)
        if sensor_id:
            queryset = queryset.filter(sensor_id=sensor_id)
        return queryset

class SensorSessionTokenViewSet(viewsets.ModelViewSet):
    queryset = SensorSessionToken.objects.all()
    serializer_class = SensorSessionTokenSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    def get_queryset(self):
        queryset = super().get_queryset()
        sensor_id = self.request.query_params.get('sensor_id', None)
        if sensor_id:
            queryset = queryset.filter(sensor_id=sensor_id)
        return queryset
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update']:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = []
        return super().get_permissions()
