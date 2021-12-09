from django.urls import path, include
from core.views.publication_views import PublicationViewSet
from core.views.article import ArticleAPIView
from core.views.profile_views import *
from core.views.category_view import CategoryViewSet


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('publication', PublicationViewSet)
router.register('profile', ProfileViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('article/', ArticleAPIView.as_view(), name='article'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('', include(router.urls))
]
