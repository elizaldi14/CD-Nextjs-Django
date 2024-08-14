from django.db import models

# Create your models here.

#Creo el modelo de la bd de la tabla Task con sus campos

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
