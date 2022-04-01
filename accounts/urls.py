from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import views as auth_view

from accounts import views

urlpatterns = [
    # Accounts
    path('register/', views.UserRegistrationAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('logout/', views.LogoutAPIView.as_view()),
    # Password change
    path('chanage-password/<pk>/', views.ChangePasswordView.as_view()),
    path('password-reset/', views.PasswordResetView.as_view()),
    path('password-change-confirm/', views.PasswordResetConfirmView.as_view()),
    path('password-reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(), name='password-reset'),
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(), name='password-reset-complete'),
    # Profile
    path('profile/', views.ProfileAPIView.as_view()),
    path('profile/<pk>/', views.ProfileUpdateDeleteView.as_view()),
    path('message/', views.SendMessage.as_view()),
]
