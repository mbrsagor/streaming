from rest_framework import generics, views, status, permissions
from rest_framework.response import Response
from django_filters import rest_framework as filters

from films.models import Trailer
from utils.message import PERMISSION, NOID, DELETED
from films.serializers.trailer_serializer import TrailerSerializer
from utils.role_util import allow_access_admin, allow_access_manager
from utils.response import prepare_create_success_response, prepare_success_response, prepare_error_response


class TrailerCreateListView(generics.ListCreateAPIView):
    queryset = Trailer.objects.all()
    serializer_class = TrailerSerializer

    def post(self, request, *args, **kwargs):
        role = self.request.user.role
        if role == allow_access_admin or role == allow_access_manager:
            try:
                serializer = TrailerSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
                return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response(prepare_error_response(str(e)))
        else:
            return Response(prepare_error_response(PERMISSION))


class TrailerUpdateDeleteAPIView(views.APIView):

    def get_object(self, pk):
        try:
            return Trailer.objects.get(id=pk)
        except Trailer.DoesNotExist:
            return None

    def put(self, request, pk):
        role = self.request.user.role
        if role == allow_access_admin or role == allow_access_manager:
            trailer = self.get_object(pk)
            if trailer is not None:
                serializer = TrailerSerializer(trailer, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
                return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(prepare_error_response(NOID), status=status.HTTP_200_OK)
        else:
            return Response(prepare_error_response(PERMISSION),
                            status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, pk):
        role = self.request.user.role
        if role == allow_access_admin or role == allow_access_manager:
            trailer = self.get_object(pk)
            if trailer is not None:
                trailer.delete()
                return Response(prepare_success_response(DELETED), status=status.HTTP_200_OK)
            return Response(prepare_error_response(NOID), status=status.HTTP_200_OK)
        else:
            return Response(prepare_error_response(PERMISSION),
                            status=status.HTTP_401_UNAUTHORIZED)


class TrailerDetailsView(generics.RetrieveAPIView):
    queryset = Trailer.objects.filter(is_publish=True)
    serializer_class = TrailerSerializer
    permission_classes = (permissions.AllowAny,)


class TrailerListView(generics.ListAPIView):
    queryset = Trailer.objects.filter(is_publish=True)
    serializer_class = TrailerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name',)
    permission_classes = (permissions.AllowAny,)
