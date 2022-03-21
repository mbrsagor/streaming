from rest_framework import generics, status
from rest_framework.response import Response

from films.models import Category
from films.serializers.category_serializer import CategorySerializer
from utils.response import prepare_create_success_response


class CategoryCreateListView(generics.ListCreateAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        return Response(prepare_create_success_response(serializer), status=status.HTTP_201_CREATED)
