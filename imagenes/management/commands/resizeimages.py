from django.core.management import BaseCommand

from imagenes.models import Imagenes
from imagenes.utiles import generate_responsive_images


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Fetching images to resize its images")
        imagenes = Imagenes.objects.filter(resized=False)
        self.stdout.write("{0} images to resize its images".format(imagenes.count()))
        for imagen in imagenes:
            self.stdout.write("Resizing imagenes {0} image".format(imagen.pk))
            generate_responsive_images(imagen)
            imagen.resized = True
            imagen.save()
            self.stdout.write(self.style.SUCCESS("Image {0}'s image realized succefully".format(imagen.pk)))