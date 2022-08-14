from django.db import models
from datetime import date


from accounts.models import BaseEntity, User


class Blog(BaseEntity):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(BaseEntity):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(BaseEntity):
    body_text = models.TextField()
    pub_date = models.DateField()
    rating = models.IntegerField(default=5)
    authors = models.ManyToManyField(Author)
    headline = models.CharField(max_length=255)
    mod_date = models.DateField(default=date.today)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
