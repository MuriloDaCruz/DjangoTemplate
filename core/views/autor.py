from rest_framework.viewsets import ModelViewSet

from core.models import autor
from core.serializers import AutorSerializer

class AutorViewSet(ModelViewSet):
    queryset = autor.Autor.objects.all()
    serializer_class = AutorSerializer