from django.urls import path

from films.views.category_view import CategoryCreateListView, CategoryUpdateDeleteAPIView

urlpatterns = [
    path('categories/', CategoryCreateListView.as_view()),
    path('category/<pk>/', CategoryUpdateDeleteAPIView.as_view()),
]
