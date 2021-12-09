from django.contrib.auth.models import Userfrom drf_role.models import Rolefrom django.db import modelsfrom core.helpers.enums import GenderEnumfrom core.models.base import BaseEntityclass Profile(BaseEntity):    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)    date_of_birth = models.DateField(verbose_name="Birth Date", null=True)    gender = models.CharField(choices=GenderEnum.choices(), default=GenderEnum.MALE.value, max_length=10)    mobile = models.CharField(max_length=16, unique=True, null=True, blank=False)    address = models.CharField(max_length=255, null=True, blank=True)    def __str__(self):        return self.user.username    @property    def name(self):        try:            return self.user.username        except AttributeError:            return 'N/A'