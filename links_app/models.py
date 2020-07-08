from django.db import models


class Link(models.Model):
    long_url = models.CharField(max_length=26000)
    short_url = models.CharField(max_length=256)

    def __str__(self):
        return self.short_url
