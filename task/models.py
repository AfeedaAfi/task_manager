from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Staff(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    is_team_lead = models.BooleanField(max_length=100)


class ModelWithTimestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Task(ModelWithTimestamp):
    STATUS = (
        (1, 'inprogress'),
        (2, 'pending'),
        (3, 'completed'),
    )

    title = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(max_length=25, choices=STATUS, null=True, blank=True)
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='assigned_to'
    )
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_by')
    assigned_team = models.ForeignKey(Team, on_delete=models.CASCADE)

    # object.user

    # def get_status(self):
    #     return self.status.get_display_name()


# class TaskHistory(ModelWithTimestamp):
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     action = models.JSONField()
