# Create your tasks here

from films.models import Trailer

from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_trailers():
    return Trailer.objects.count()


@shared_task
def rename_trailer(trailer_id, name):
    w = Trailer.objects.get(id=trailer_id)
    w.name = name
    w.save()
