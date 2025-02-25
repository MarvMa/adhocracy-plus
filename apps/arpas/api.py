from rest_framework import viewsets
from rest_framework.parsers import FormParser
from rest_framework.parsers import MultiPartParser

from .models import Object3D
from .serializers import Object3DSerializer


class Object3DViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for listing, creating, retrieving, updating,
    and deleting ThreeDObject instances.
    """

    queryset = Object3D.objects.all()
    serializer_class = Object3DSerializer
    parser_classes = (MultiPartParser, FormParser)
