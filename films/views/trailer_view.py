from rest_framework import generics, status
from rest_framework.response import Response

from films.models import Trailer
from films.serializers.trailer_serializer import TrailerSerializer
from utils.response import prepare_create_success_response, prepare_error_response
from utils.role_util import allow_access_admin, allow_access_manager


class TrailerCreateListView(generics.ListCreateAPIView):
    queryset = Trailer.objects.filter(is_publish=True)
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
            return Response(prepare_error_response('You have no permission to create trailer.'))
