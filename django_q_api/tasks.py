# tasks.py
from celery import shared_task ,Celery
from time import sleep


@shared_task
def sleep_for_celery(second):
    sleep(second)
    print("hello")

app = Celery('change_runner')

## run celery
##celery -A queue_config worker --loglevel=INFO --pool gevent