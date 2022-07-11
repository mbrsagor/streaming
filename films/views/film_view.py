from rest_framework import generics, views, status, permissions
from rest_framework.response import Response
from django_filters import rest_framework as filters

from films.models import Film
from films.serializers.film_serializer import FilmSerializer
from utils.response import prepare_create_success_response, prepare_success_response, prepare_error_response
from utils.role_util import allow_access_admin, allow_access_director


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


class FilmUpdateDeleteAPIView(views.APIView):

    def get_object(self, pk):
        try:
            return Film.objects.get(id=pk)
        except Film.DoesNotExist:
            return None

    def put(self, request, pk):
        role = self.request.user.role
        if role == allow_access_admin or role == allow_access_director:
            films = self.get_object(pk)
            if films is not None:
                serializer = FilmSerializer(films, data=request.data)
                if serializer.is_valid():
                    serializer.save(director=self.request.user)
                    return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
                return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(prepare_error_response('No ID the found the films'))
        else:
            return Response(prepare_error_response('You have no permission to update the films.'),
                            status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, pk):
        role = self.request.user.role
        if role == allow_access_admin:
            film = self.get_object(pk)
            if film:
                film.delete()
                return Response(prepare_success_response('The films has been deleted'),
                                status=status.HTTP_404_NOT_FOUND)
            return Response(prepare_error_response('No ID found the film'))
        else:
            return Response(prepare_error_response('You have no permission to delete the films.'),
                            status=status.HTTP_401_UNAUTHORIZED)


class DirectorOwnMovieList(generics.ListAPIView):
    serializer_class = FilmSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name', 'is_publish', 'price')

    """
        def get(self, request, *args, **kwargs):
        films = Film.objects.filter(director=self.request.user)
        serializer = FilmSerializer(films, many=True)
        return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
    """

    def get_queryset(self):
        user = self.request.user
        return Film.objects.filter(director=user).order_by('-id')


class FilmListView(generics.ListAPIView):
    queryset = Film.objects.filter(is_publish=True)
    serializer_class = FilmSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name', 'category_name', 'release_date')


class FilmDetailsView(generics.RetrieveAPIView):
    queryset = Film.objects.filter(is_publish=True)
    serializer_class = FilmSerializer
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'slug'
