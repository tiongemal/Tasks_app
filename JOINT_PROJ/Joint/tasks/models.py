from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=30)
    priority = models.IntegerField()
    completed = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)

class Data(models.Model):
    user = models.CharField(max_length=30)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

