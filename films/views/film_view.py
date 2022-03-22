from rest_framework import generics, views, status, permissions
from rest_framework.response import Response

from films.models import Film
from films.serializers.film_serializer import FilmSerializer
from utils.response import prepare_create_success_response, prepare_success_response, prepare_error_response
from utils.role_util import allow_access_admin, allow_access_director, allow_access_manager


class FilmCreateAPIView(views.APIView):

    def post(self, request):
        role = self.request.user.role
        if role == allow_access_admin or role == allow_access_director:
            try:
                serializer = FilmSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save(director=self.request.user)
                    return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
                return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response(prepare_error_response(str(e)))
        else:
            return Response(prepare_error_response('You no permission to upload film.'),
                            status=status.HTTP_401_UNAUTHORIZED)


class DirectorOwnMovieList(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def list(self, request, *args, **kwargs):
        films = Film.objects.filter(director=self.request.user)
        serializer = FilmSerializer(films, many=True)
        return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)


class FilmListView(generics.ListAPIView):
    queryset = Film.objects.filter(is_publish=True)
    serializer_class = FilmSerializer
    permission_classes = (permissions.AllowAny,)
