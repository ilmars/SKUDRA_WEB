from django.contrib.gis.db import models
from django.contrib.auth.models import User
from rest_framework.decorators import action

from datetime import datetime  

class TimeStampUserMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, related_name='created_%(app_label)s_%(class)s', on_delete=models.CASCADE, default=1)
    updated_by = models.ForeignKey(User, related_name='updated_%(app_label)s_%(class)s', on_delete=models.CASCADE, default=1)
    
    class Meta:
        abstract = True

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True