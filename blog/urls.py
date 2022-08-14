from django.urls import path
from blog.views.blog_view import BlogCreateListAPIView, AuthorCreateListView

urlpatterns = [
    path('blog-create-list/', BlogCreateListAPIView.as_view()),
    path('author/', AuthorCreateListView.as_view()),
]
