from core.models.product import Category
from core.serializers.product_serializer import CategorySerializer

from rest_framework.viewsets import ModelViewSet


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
