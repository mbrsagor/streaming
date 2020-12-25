from core.models.base import BaseEntity
from django.db import models
from core.models.category import Category


class Publication(BaseEntity):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="publicationCategory")
    body = models.TextField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title[:30]
