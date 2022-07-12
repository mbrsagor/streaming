from films.models import Trailer, Film


def trailer_processor(request):
    trailer = Trailer.objects.filter(is_publish=True).order_by('created_at')
    return {'trailer': trailer}


def film_processor(request):
    films = Film.objects.filter(is_publish=True)
    return {'films': films}
