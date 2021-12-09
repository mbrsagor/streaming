from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

from core.models.base import BaseEntity
from core.models.category import Category
from core.helpers.enums import TaskStatus


class Task(BaseEntity):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='task_category')
    task_image = models.ImageField(upload_to='task/%y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.name[:30]


class AddTask(BaseEntity):
    title = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_owner')
    tasks = models.ManyToManyField(Task, related_name='task')
    assign_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assign_user')
    is_active = models.BooleanField(default=True)
    status = models.CharField(choices=TaskStatus.choices(), default=TaskStatus.PROGRESS.value, max_length=12)
    start_date = models.DateField(default=datetime.now, blank=True)
    end_date = models.DateField()

    def __str__(self):
        return self.title

    def calculate_date(self):
        return self.start_date - self.end_date
