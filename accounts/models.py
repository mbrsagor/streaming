from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from datetime import date, datetime

from utils.role_util import RoleEnum
from .manager import UserManager


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, Timestamp):
    username = None
    name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True, blank=True)
    phone_number = models.CharField(verbose_name='Phone Number', max_length=14, unique=True)
    role = models.IntegerField(choices=RoleEnum.get_choices(), default=RoleEnum.USER.value)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', ]
    objects = UserManager()

    def __str__(self):
        return self.name


class Profile(Timestamp):
    auth = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile/%y/%m', blank=True, null=True)
    date_of_birth = models.DateField(default=datetime.now)
    address = models.TextField(default='')

    def __str__(self):
        return self.auth.name

    @property
    def current_age(self):
        today = date.today()
        return (today - self.date_of_birth).days

    @property
    def get_photo_url(self):
        if self.profile_picture and hasattr(self.profile_picture, 'url'):
            return self.profile_picture.url
        else:
            return "https://static.productionready.io/images/smiley-cyrus.jpg"


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Profile.objects.get_or_create(auth=instance)
        return profile


post_save.connect(create_user_profile, sender=User)
