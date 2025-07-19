import os 
from celery import Celery
# Set default Django setting
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.setting')

# Create a celery instance
app = Celery('alx_travel_app')

# Load configs from setting.py
app.config_from_object('django.conf:setting', namespace='CELERY')

# Auto-detect tasks in all apps
app.autodiscover_tasks()