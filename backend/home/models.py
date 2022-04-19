from django.conf import settings
from django.db import models


class Location(models.Model):
    "Generated Model"
    streetName = models.CharField(
        max_length=256,
    )
    city = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    state = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
