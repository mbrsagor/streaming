from rest_framework import status, generics
from rest_framework.response import Response

from blog.serializers.blog_serializer import BlogSerializer, AuthorSerializer
from blog.models import Blog, Author


class BlogCreateListAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class AuthorCreateListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
