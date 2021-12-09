from rest_framework.viewsets import ModelViewSet

from core.models.category import Category
from core.serializers.product_serializer import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
