from django.apps import AppConfig
from django.db.models.signals import post_migrate
# skudra/apps.py

import os

scheduler_already_running = False

class SkudraConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'skudra'

    def ready(self):

        import skudra.signals
        
        # Return if Django is not in the main process
        if os.environ.get('RUN_MAIN') != 'true':
            return

        print('____________________________ SKUDRA APP IS READY ____________________________')
        
        # # Initialize scheduler
        # from .scheduler import SchedulerManager
        # SchedulerManager.initialize()
