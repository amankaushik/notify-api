'''
All scheduled tasks using celery
'''
from notify.tasks import update_db

def schedule_update_db():
    '''
    update api db
    '''
    update_db.delay()
