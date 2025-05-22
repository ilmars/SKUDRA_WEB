import atexit
from django_apscheduler.jobstores import DjangoJobStore, register_events
from apscheduler.schedulers.background import BackgroundScheduler
from .tasks import update_sensor_status

class SchedulerManager:
    _instance = None
    _scheduler = None
    _is_running = False

    @classmethod
    def initialize(cls):
        if not cls._instance:
            cls._instance = cls()
            cls._instance._setup_scheduler()
        return cls._instance

    def _setup_scheduler(self):
        if not self._is_running:
            try:
                self._scheduler = BackgroundScheduler()
                self._scheduler.add_jobstore(DjangoJobStore(), "default")
                
                # Add jobs
                self._scheduler.add_job(
                    update_sensor_status,
                    trigger='interval',
                    minutes=5,
                    name='Update sensor status',
                    replace_existing=True,
                    max_instances=5
                )

                register_events(self._scheduler)
                self._scheduler.start()
                self._is_running = True

                # Register shutdown handler
                atexit.register(self.shutdown)
                
                print('Scheduler initialized successfully')
            except Exception as e:
                print(f"Failed to initialize scheduler: {e}")

    def shutdown(self):
        if self._scheduler and self._is_running:
            self._scheduler.shutdown()
            self._is_running = False
            print('Scheduler shut down successfully')

    @property
    def scheduler(self):
        return self._scheduler