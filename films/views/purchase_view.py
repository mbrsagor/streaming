from rest_framework import views, status
from rest_framework.response import Response

from films.models import Purchase
from films.serializers.purchase_serializer import PurchaseSerializer
from utils.response import prepare_create_success_response, prepare_success_response, prepare_error_response


class PurchaseCreateListView(views.APIView):

    def post(self, request):
        try:
            serializer = PurchaseSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(customer=self.request.user)
                return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
            return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(prepare_error_response(str(e)))

    def get(self, request):
        try:
            purchase = Purchase.objects.filter(customer=self.request.user)
            if purchase:
                serializer = PurchaseSerializer(purchase, many=True)
                return Response(prepare_success_response(serializer.data), status=status.HTTP_201_CREATED)
            return Response(prepare_error_response('No purchase history found.'))

        except Exception as e:
            return Response(prepare_error_response(str(e)))
