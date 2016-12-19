from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

from cuentame.settings import MEDIA_URL, DEFAULT_IMAGE_SIZE, THUMBNAIL_HIGH_RESOLUTION


class Imagenes(models.Model):

    # url = models.FileField(upload_to=MEDIA_URL)
    # url = ThumbnailerImageField(upload_to=MEDIA_URL, resize_source={'size': DEFAULT_IMAGE_SIZE, 'crop': THUMBNAIL_HIGH_RESOLUTION})
    url = models.ImageField()
    nombre = models.CharField(max_length=250)
    resized = models.BooleanField(default=False)
