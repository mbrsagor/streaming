from rest_framework import generics, status, permissions
from rest_framework.response import Response

from films.models import Notification
from films.serializers.notification_serializer import NotificationSerializer
from utils.response import prepare_create_success_response, prepare_error_response


class NotificationCreateListView(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.filter(is_publish=True)
    permission_classes = (permissions.IsAdminUser, permissions.IsAuthenticated)

    def post(self, request, *args, **kwargs):
        try:
            serializer = NotificationSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(prepare_error_response(prepare_create_success_response(serializer.data)),
                            status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response(prepare_error_response((str(ex))), status=status.HTTP_400_BAD_REQUEST)
