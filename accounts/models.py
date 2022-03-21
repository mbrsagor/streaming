from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

from utils.role_util import RoleEnum
from .manager import UserManager


class BaseEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(AbstractUser, BaseEntity):
    name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True, blank=True)
    phone_number = models.CharField(verbose_name='Phone Number', max_length=14, unique=True)
    role = models.IntegerField(choices=RoleEnum.get_choices(), default=RoleEnum.USER.value)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', ]
    objects = UserManager()

    def __str__(self):
        return self.name
