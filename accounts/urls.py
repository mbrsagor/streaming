from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView

from accounts import views

urlpatterns = [
    # Accounts
    path('register/', views.UserRegistrationAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
]
