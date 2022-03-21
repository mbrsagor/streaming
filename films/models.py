from django.db import models
from django.db.models import JSONField

from accounts.models import BaseEntity, User


class Category(BaseEntity):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categoryCreator')
    name = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='category/%y/%m', blank=True, null=True)

    def __str__(self):
        return self.name[:30]

    def creator_name(self):
        return self.creator.name


class Actor(BaseEntity):
    name = models.CharField(max_length=35)

    def __str__(self): return self.name


class Trailer(BaseEntity):
    name = models.CharField(max_length=150)
    trailer_url = models.URLField(max_length=250)
    is_publish = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Film(BaseEntity):
    name = models.CharField(max_length=120)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='filmsCategory')
    actors = models.ManyToManyField(Actor, related_name='movieActors', blank=True)
    director = models.ForeignKey(User, on_delete=models.CASCADE, related_name='filmsDirector')
    producers = JSONField(blank=True, null=True, default=None)

    Type = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    types = models.CharField(max_length=1, choices=Type)
    is_publish = models.BooleanField(default=True)
    release_date = models.DateTimeField()
    description = models.TextField()
    price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    discount_price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    image = models.ImageField(upload_to='films/%y/%m', blank=True, null=True)
    video = models.URLField(max_length=250, blank=True)
    is_watchable = models.BooleanField(default=False)

    def __str__(self):
        return self.name
