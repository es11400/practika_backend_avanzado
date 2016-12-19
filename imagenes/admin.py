from django.contrib import admin
from imagenes.models import Imagenes

# Register your models here.


class ImagenesAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'url', 'resized',)
admin.site.register(Imagenes, ImagenesAdmin)
