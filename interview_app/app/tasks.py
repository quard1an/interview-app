from celery import shared_task
import logging

@shared_task
def add(x, y):
    return x + y
