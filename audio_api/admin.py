from django.contrib import admin
from .models import Song, Podcast, Audiobook
# Register your models here.
admin.site.register((Song, Podcast, Audiobook))