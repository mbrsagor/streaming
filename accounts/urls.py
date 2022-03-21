from django.urls import path

from accounts import views

urlpatterns = [
    # Accounts
    path('register/', views.UserRegistrationAPIView.as_view())
]
