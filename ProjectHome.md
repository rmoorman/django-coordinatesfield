This is the first approach to give admins a nice interface for geographical
data. With the included CoordinatesFormField it is possible to add and edit
GPS coordinates using one of the popular map services from Google and Yahoo.

Since most of the work is done via Javascript it has a nice fallback with
a default TextField. The javascript code is written with generalisation in
mind to handle the differences between the map systems.

Example:

```
from django.db import models
from field import CoordinatesField

class Location (models.Model):
    name = models.CharField(maxlength=100)
    gps = CoordinatesField()
```

Please watch the Subversion [repository](http://django-coordinatesfield.googlecode.com/svn/) for changes