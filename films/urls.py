from django.urls import path

from films.views.category_view import CategoryCreateListView, CategoryUpdateDeleteAPIView
from films.views.trailer_view import TrailerCreateListView
from films.views.film_view import FilmCreateAPIView, FilmListView, DirectorOwnMovieList

urlpatterns = [
    # Category
    path('categories/', CategoryCreateListView.as_view()),
    path('category/<pk>/', CategoryUpdateDeleteAPIView.as_view()),
    # Trailers
    path('trailers/', TrailerCreateListView.as_view()),
    # Film
    path('create-film/', FilmCreateAPIView.as_view()),
    path('films/', FilmListView.as_view()),
    path('my-all-films/', DirectorOwnMovieList.as_view()),
]
