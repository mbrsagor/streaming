from core.models.category import Category
from core.serializers.category_serializer import CategorySerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, ]
