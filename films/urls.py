from django.urls import path

from films.views.category_view import CategoryCreateListView

urlpatterns = [
    path('categories/', CategoryCreateListView.as_view())
]
