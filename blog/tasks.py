from celery import shared_task
from time import sleep

@shared_task
def example_task(seconds):
    sleep(seconds)
    return f"Task completed after {seconds} seconds"