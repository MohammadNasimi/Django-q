from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django_q.tasks import async_task
from time import sleep
import random
from celery import shared_task
from django_q_api.tasks import sleep_for_celery 
from django_q_api.shared_tasks import async_task_celery

def sleep_for(second):
    sleep(second)





def queue_celery_q(request):
    sleep_for_celery.delay(10) 
    now = datetime.now()
    html = "<html><body>It is rrrrr %s.</body></html>" % now
    return HttpResponse(html)

def queue_django_q(request):
    async_task_celery(sleep_for,10)
    now = datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)