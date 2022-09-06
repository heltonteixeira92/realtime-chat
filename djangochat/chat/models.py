from django.db import models


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Message(models.Model):
    value = models.CharField(max_length=100000)
    user = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)
    room = models.CharField(max_length=256)

    def __str__(self):
        return self.value
