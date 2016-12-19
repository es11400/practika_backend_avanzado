from rest_framework.viewsets import ModelViewSet

from imagenes.models import Imagenes
from imagenes.serializers import ImagenesSerializer
from imagenes.utiles import generate_responsive_images


class ImagenesModelViewSet(ModelViewSet):

    queryset = Imagenes.objects.all()
    serializer_class = ImagenesSerializer

    def perform_create(self, serializer):
        imagen = serializer.save()
        generate_responsive_images(imagen)

    def perform_update(self, serializer):
        imagen = serializer.save()
        generate_responsive_images(imagen)
