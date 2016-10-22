web: sh -c 'cd ./notifyProject/ && exec gunicorn notifyProject.wsgi:application --log-file=-'
worker: sh -c 'cd ./notifyProject/ && exec celery worker --app=notify --beat --loglevel=INFO --hostname=notify-worker.%h --without-heartbeat --schedule=/tmp/celerybeat-schedule'
