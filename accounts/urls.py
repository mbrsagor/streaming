from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView

from accounts import views

urlpatterns = [
    # Accounts
    path('register/', views.UserRegistrationAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('logout/', views.LogoutAPIView.as_view()),
    path('chanage-password/<pk>/', views.ChangePasswordView.as_view()),
    path('password-reset/', views.PasswordResetView.as_view()),
    path('password-reset-confirm/', views.PasswordResetConfirmView.as_view()),
    path('profile/', views.ProfileAPIView.as_view()),
    path('profile/<pk>/', views.ProfileUpdateDeleteView.as_view()),
    path('message/', views.SendMessage.as_view()),
]
