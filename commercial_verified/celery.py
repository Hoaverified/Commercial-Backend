"""
Celery configuration for commercial_verified project
"""
import os
from celery import Celery
from decouple import config

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'commercial_verified.settings')

# Create Celery app instance
app = Celery('commercial_verified')

# Load task modules from all registered Django apps.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks from all installed apps
app.autodiscover_tasks()

# Celery configuration
app.conf.broker_url = config('CELERY_BROKER_URL', default='redis://redis-master:6379/0')
app.conf.result_backend = config('CELERY_RESULT_BACKEND', default='redis://redis-master:6379/0')
app.conf.task_serializer = 'json'
app.conf.result_serializer = 'json'
app.conf.accept_content = ['json']
app.conf.timezone = 'UTC'
app.conf.enable_utc = True

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
