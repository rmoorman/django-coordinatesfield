"""
An example location model with one CoordinatesField

You need to specify two settings:
``MAP_API`` is one of the following: google, yahoo or yahooflash
``MAP_API_KEY`` is the API key provided by Google or Yahoo

"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from field import CoordinatesField

class Location (models.Model):
    name = models.CharField(maxlength=100)
    gps = CoordinatesField(_('GPS coordinates'), help_text=_("Please click on the marker."))

    def __str__(self):
        return self.name

    class Admin:
      pass