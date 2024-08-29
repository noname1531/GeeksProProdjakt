from rest_framework import viewsets
from .models import Produkt
from .serializers import ProduktSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer
