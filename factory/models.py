from django.db import models
from django.utils import timezone

class Tarea(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    deadline = models.DateTimeField(default = timezone.now)
    duration = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

    def publish(self):
        self.save()

class Project(models.Model):
    name = models.CharField(max_length = 200)
    tareas = models.ManyToManyField(Tarea)

    def __str__(self):
        return self.name

    def publish(self):
        self.save()
'''
class User():
    name...
    projects = models.ManyToManyField(Project)
'''
