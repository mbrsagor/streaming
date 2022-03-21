from rest_framework import generics, status
from rest_framework.response import Response

from films.models import Category
from films.serializers.category_serializer import CategorySerializer
from utils.response import prepare_create_success_response, prepare_success_response, prepare_error_response
from utils.role_util import create_allow_access


class CategoryCreateListView(generics.ListCreateAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        if self.request.user.role == create_allow_access:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(creator=self.request.user)
                return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
            else:
                return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        return Response(prepare_error_response('You have no permission to create category'),
                        status=status.HTTP_401_UNAUTHORIZED)


class CategoryUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer

    def update(self, request, *args, **kwargs):
        if self.request.user.role == create_allow_access:
            instance = self.get_object()
            serializer = CategorySerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save(creator=self.request.user)
                return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
            return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(prepare_error_response('You have no permission to update category'),
                            status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        if self.request.user.role == create_allow_access:
            try:
                instance = self.get_object()
                if instance:
                    self.perform_destroy(instance)
                    return Response(prepare_success_response('The category has been deleted'),
                                    status=status.HTTP_200_OK)
                return Response(prepare_error_response('No ID found the category'))
            except Exception as e:
                return Response(prepare_error_response(str(e)))
        else:
            return Response(prepare_error_response('You have no permission to delete category'),
                            status=status.HTTP_401_UNAUTHORIZED)
