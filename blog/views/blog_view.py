from rest_framework import status, generics
from rest_framework.response import Response

from utils.response import prepare_create_success_response, prepare_error_response
from blog.serializers.blog_serializer import BlogSerializer, AuthorSerializer
from utils.role_util import allow_access_admin, allow_access_director
from utils.message import PERMISSION, NOID, DELETED
from blog.models import Blog, Author


class BlogCreateListAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def create(self, request, *args, **kwargs):
        role = self.request.user.role
        if role == allow_access_admin or role == allow_access_director:
            serializer = BlogSerializer(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
            return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        return Response(prepare_error_response(PERMISSION), status=status.HTTP_403_FORBIDDEN)


class AuthorCreateListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def create(self, request, *args, **kwargs):
        role = self.request.user.role
        if role == allow_access_admin or request.user.is_superuser:
            serializer = AuthorSerializer(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
            return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        return Response(prepare_error_response(PERMISSION), status=status.HTTP_403_FORBIDDEN)
