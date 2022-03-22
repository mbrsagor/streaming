from django.urls import path

from films.views.category_view import CategoryCreateListView, CategoryUpdateDeleteAPIView
from films.views.trailer_view import TrailerCreateListView, TrailerListView, TrailerUpdateDeleteAPIView, \
    TrailerDetailsView
from films.views.film_view import FilmCreateAPIView, FilmListView, DirectorOwnMovieList, FilmDetailsView, \
    FilmUpdateDeleteAPIView
from films.views.purchase_view import PurchaseCreateListView

urlpatterns = [
    # Category
    path('categories/', CategoryCreateListView.as_view()),
    path('category/<pk>/', CategoryUpdateDeleteAPIView.as_view()),
    # Trailers
    path('trailers/', TrailerCreateListView.as_view()),
    path('trailer/<pk>/', TrailerUpdateDeleteAPIView.as_view()),
    path('trailer/detail/<pk>/', TrailerDetailsView.as_view()),
    path('trailer-list/', TrailerListView.as_view()),
    # Film
    path('create-film/', FilmCreateAPIView.as_view()),
    path('films/', FilmListView.as_view()),
    path('my-all-films/', DirectorOwnMovieList.as_view()),
    path('films/<slug>/', FilmDetailsView.as_view()),
    path('film/<pk>/', FilmUpdateDeleteAPIView.as_view()),
    # purchase
    path('purchase/', PurchaseCreateListView.as_view()),
]
