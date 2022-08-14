from django.urls import path
from blog.views.blog_view import BlogCreateListAPIView, AuthorCreateListView

urlpatterns = [
    path('blog/', BlogCreateListAPIView.as_view()),
    path('author/', AuthorCreateListView.as_view()),
]
