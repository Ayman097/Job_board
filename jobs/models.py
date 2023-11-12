from django.db import models

# Create your models here.

class JobPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    campany = models.CharField(max_length=100)
    salary = models.IntegerField(default=None)
    is_active = models.BooleanField(default=False)