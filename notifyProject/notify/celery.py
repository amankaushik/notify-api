'''
Celery Module
'''
from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notifyProject.settings')
APP = Celery('notify')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
APP.config_from_object('django.conf:settings')
APP.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@APP.task(bind=True)
def debug_task(self):
    '''
    debug task
    '''
    print 'Request: {0!r}'.format(self.request)
