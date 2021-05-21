from django.db import models
from django.core.exceptions import ValidationError
import json

# Create your models here.
class Song(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(auto_now_add=True)


class Podcast(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(auto_now_add=True)
    host = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    paticipant = models.CharField(
        max_length=1000,
        null=True,
        blank=True
    )

    def set_paticipant(self, x):
        self.paticipant = json.dumps(x)

    def get_paticipant(self, x):
        if x:
            return ast.literal_eval(x)
        else:
            return x 

class Audiobook(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    author_of_title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    narrator = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(auto_now_add=True)