# Introduction #

This is the first approach to give admins a nice interface for geographical
data. With the included CoordinatesFormField it is possible to add and edit
GPS coordinates using one of the popular map services from Google and Yahoo.

Since most of the work is done via Javascript it has a nice fallback with
a default TextField. The javascript code is written with generalisation in
mind to handle the differences between the map systems.

# Howto use CoordinatesField in your own django app #

  1. Copy "coordinates\_form.html" to a folder where it can be found by the template loader (hint: ```TEMPLATE_DIRS``` in your settings.py)
  1. Set in your settings.py:
    * ```MAP_API``` to "google", "yahoo" or "yahooflash"
    * ```MAP_API_KEY``` to the API key provided by Google or Yahoo
  1. Copy field.py to your django application folder, next to its models.py file
  1. At the top of your applications's models.py file add the following line: ` from field import CoordinatesField `
  1. Change the model of one of the form fields of you model, for example:
```
gps = models.CharField(maxlength=75) #OLD
gps = CoordinatesField() #NEW
```

# Howto use it on a testing/development server or locally #

### Google Maps ###
Please visit http://www.google.com/apis/maps/signup.html and request a new API key for the domain
http://localhost/ or any other valid URL (also e.g. http://192.168.1.1).

### Yahoo Maps ###
Please visit http://search.yahooapis.com/webservices/register_application  and request a new API key for the domain http://localhost/ or any other valid URL (also e.g. http://192.168.1.1).

