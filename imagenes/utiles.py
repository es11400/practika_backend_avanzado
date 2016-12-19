from celery import shared_task
from easy_thumbnails.files import generate_all_aliases

@shared_task
def generate_responsive_images(imagen):
    generate_all_aliases(imagen.url, True)
    imagen.resized = True
    imagen.save()