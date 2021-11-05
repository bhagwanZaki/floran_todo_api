from django.contrib.auth.models import User
from django.db import models
from datetime import date as dt
from datetime import datetime as dtt
from django.utils import timezone
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    date_completed_by = models.DateField(default=timezone.now)
    completed_at= models.DateField(null=True)
    owner=models.ForeignKey(User,related_name="todos",on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title
        