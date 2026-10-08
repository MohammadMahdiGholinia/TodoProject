from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length=100)
    description = models.TextField()
    completed   = models.BooleanField(default=False)
    created_at  = models.TimeField(auto_now_add=True)
    due_date    = models.IntegerField()

    



