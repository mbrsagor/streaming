from django.urls import path

from films.views.category_view import CategoryCreateListView, CategoryUpdateDeleteAPIView
from films.views.trailer_view import TrailerCreateListView

urlpatterns = [
    path('categories/', CategoryCreateListView.as_view()),
    path('category/<pk>/', CategoryUpdateDeleteAPIView.as_view()),
    path('trailers/', TrailerCreateListView.as_view()),
]
