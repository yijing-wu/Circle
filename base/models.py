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
