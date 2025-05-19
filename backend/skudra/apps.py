from django.apps import AppConfig
from django.db.models.signals import post_migrate
# skudra/apps.py

import os

scheduler_already_running = False

class SkudraConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'skudra'

    def ready(self):
        # Return if Django is not in the main process
        if os.environ.get('RUN_MAIN') != 'true':
            return

        global scheduler_already_running
        if scheduler_already_running:
            # If we've already started the scheduler in this process, skip
            return
        scheduler_already_running = True

        print('____________________________ SKUDRA APP IS READY ____________________________')

        from django_apscheduler.jobstores import DjangoJobStore, register_events
        from apscheduler.schedulers.background import BackgroundScheduler
        from skudra.tasks import update_sensor_status

        scheduler = BackgroundScheduler()
        scheduler.add_jobstore(DjangoJobStore(), "default")
        scheduler.add_job(
            update_sensor_status,
            trigger='interval',
            minutes=5,
            name='Update sensor status',
            replace_existing=True,
            max_instances=5
        )
        register_events(scheduler)
        scheduler.start()
