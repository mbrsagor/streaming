from django.urls import path, include
from core.views.article import ArticleAPIView
from core.views import auth_view
from core.views.category_view import CategoryViewSet


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category', CategoryViewSet)

urlpatterns = [
    path('article/', ArticleAPIView.as_view(), name='article'),
    path('login/', auth_view.LoginAPIView.as_view(), name='login'),
    path('me/', auth_view.ProfileView.as_view(), name='profile'),
    path('password-change/', auth_view.ChangePasswordView.as_view(), name='change_password'),
    path('logout/', auth_view.LogoutAPIView.as_view(), name='logout'),
    path('', include(router.urls))
]
