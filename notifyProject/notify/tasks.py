'''
Celery task module.
'''
from notify.celery import APP
from notify.utils import refresh_news_data
#from celery.utils.log import get_task_logger

#LOGGER = get_task_logger(__name__)

@APP.task(name="update_db")
def update_db():
    '''
    Updates db
    '''
    #LOGGER.info('Updating database')
    return refresh_news_data()
