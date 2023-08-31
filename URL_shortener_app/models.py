"""
URL shortener model
"""
from django.db import models
from .utils import create_shortened_url
# Create your models here.

class Shortener(models.Model):
    """
    Creates a short URL based on original longer URL

    created        : Date a shortener was created
    times_followed : No. of times shortend URL has been followed
    long_url       : Original URL link
    short_url      : Shortened link --> https://domain/(short_url)

    """
    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)
    long_url = models.URLField(max_length=264)
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.long_url} to {self.short_url}"

    def save(self, *args, **kwargs):
        # if short_url wasn't specified
        if not self.short_url:
            self.short_url = create_shortened_url(self)

            super().save(*args, **kwargs)
