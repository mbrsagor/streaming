from core.models.base import BaseEntity
from django.db import models


class Category(BaseEntity):
    title = models.CharField(max_length=120)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='category_set')

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.title[:20]
