from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Room(models.Model):
    # host =
    # topic =
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants =
    updated = models.DateTimeField(
        auto_now=True
    )  # update timeStamp every time when updating the instance
    created = models.DateTimeField(
        auto_now_add=True
    )  # update timeStamp only when the instance is created

    def __str__(self):
        return self.name


class Message(models.Model):
    # user =
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE
    )  # Cascade means, when room is deleted, all children wil also be deleted
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]  # return first 50 characters of body
