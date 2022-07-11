from django.urls import path

from films.views import category_view
from films.views import trailer_view
from films.views import film_view
from films.views import purchase_view

urlpatterns = [
    # Category
    path('categories/', category_view.CategoryCreateListView.as_view()),
    path('category/<pk>/', category_view.CategoryUpdateDeleteAPIView.as_view()),
    # Trailers
    path('trailer-list/', trailer_view.TrailerListView.as_view()),
    path('trailers/', trailer_view.TrailerCreateListView.as_view()),
    path('trailer/<pk>/', trailer_view.TrailerUpdateDeleteAPIView.as_view()),
    path('trailer/detail/<pk>/', trailer_view.TrailerDetailsView.as_view()),
    # Film
    path('create-film/', film_view.FilmCreateAPIView.as_view()),
    path('films/', film_view.FilmListView.as_view()),
    path('my-all-films/', film_view.DirectorOwnMovieList.as_view()),
    path('films/<slug>/', film_view.FilmDetailsView.as_view()),
    path('film/<pk>/', film_view.FilmUpdateDeleteAPIView.as_view()),
    # purchase
    path('purchase/', purchase_view.PurchaseCreateListView.as_view()),
    path('purchase/<pk>/', purchase_view.PurchaseUpdateAPIView.as_view()),
    path('purchase/detail/<pk>/', purchase_view.PurchaseDetailsView.as_view()),
]
