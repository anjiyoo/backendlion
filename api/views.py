from rest_framework import viewsets
from .serializers import FoodSerializer
from .models import Food

class FoodViewSet(viewsets.ModelViewSet):
    queryset=Food.objects.all()
    serializer_class=FoodSerializer