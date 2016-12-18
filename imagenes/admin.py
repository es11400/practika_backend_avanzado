from django.contrib import admin
from imagenes.models import Imagenes

# Register your models here.


class ImagenesAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'url')
admin.site.register(Imagenes, ImagenesAdmin)
