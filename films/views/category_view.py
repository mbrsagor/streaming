from rest_framework import generics, status
from rest_framework.response import Response

from films.models import Category
from films.serializers.category_serializer import CategorySerializer
from utils.response import prepare_create_success_response, prepare_success_response, prepare_error_response


class CategoryCreateListView(generics.ListCreateAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        return Response(prepare_create_success_response(serializer), status=status.HTTP_201_CREATED)


class CategoryUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer

    def perform_update(self, serializer):
        serializer.save(creator=self.request.user)
        return Response(prepare_create_success_response(serializer), status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if instance:
                self.perform_destroy(instance)
                return Response(prepare_success_response('The category has been deleted'), status=status.HTTP_200_OK)
            return Response(prepare_error_response('No ID found the category'))
        except Exception as e:
            return Response(prepare_error_response(str(e)))
