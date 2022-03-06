from rest_framework import generics, permissions

from .serializers import PaymentSerializer
from .models import Payment


class PaymentAPIView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (permissions.IsAuthenticated,)
