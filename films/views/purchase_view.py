from rest_framework import views, status, generics
from rest_framework.response import Response

from films.models import Purchase
from utils.message import PURCHASE, PERMISSION, WARNING
from utils.role_util import allow_access_admin, allow_access_manager
from films.serializers.purchase_serializer import PurchaseSerializer, PurchaseUpdateSerializer
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
            return Response(prepare_error_response(PURCHASE))

        except Exception as e:
            return Response(prepare_error_response(str(e)))


class PurchaseUpdateAPIView(views.APIView):
    """
        Here,the view only can access the management for update some basic information.
        In cause, If something went to wrong admin will be update status.
    """

    def put(self, request, pk):
        try:
            role = self.request.user.role
            if role == allow_access_admin or role == allow_access_manager:
                purchase = Purchase.objects.get(id=pk)
                serializer = PurchaseUpdateSerializer(purchase, data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save(customer=self.request.user)
                    return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
                return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
            return Response(prepare_error_response(PERMISSION),
                            status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(prepare_error_response(str(e)))


class PurchaseDetailsView(generics.RetrieveAPIView):
    serializer_class = PurchaseSerializer

    def get_queryset(self):
        user = self.request.user
        if user is not None:
            return Purchase.objects.filter(customer=user)
        else:
            return Response(prepare_error_response(WARNING), status=status.HTTP_404_NOT_FOUND)
