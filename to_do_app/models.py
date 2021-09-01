from django.db import models

# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
