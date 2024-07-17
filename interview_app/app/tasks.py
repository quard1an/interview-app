from celery import shared_task
import logging

@shared_task
def add(x, y):
    try:
        return int(x + y)
    except ValueError as e:
        return "Values should be integers."