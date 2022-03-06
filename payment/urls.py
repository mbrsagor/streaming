from django.urls import path

from .views import PaymentAPIView

urlpatterns = [
    path('pay/', PaymentAPIView.as_view())
]
