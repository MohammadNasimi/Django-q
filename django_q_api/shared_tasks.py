# shared_tasks.py

from celery import shared_task ,Celery

app = Celery('change_runner')


def async_task_celery(func,*args,**kwargs):
    decorator_func = shared_task(func)
    return decorator_func.delay(*args,**kwargs)