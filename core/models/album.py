from core.models.base import BaseEntity
from django.db import models


class Album(BaseEntity):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="album")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='photo_set')
    
    def __str__(self):
      return self.title
