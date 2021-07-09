from django.db import models

class Body(models.Model):
    name = models.CharField(max_length=255)
    englishName = models.CharField(max_length=255)
    isPlanet = models.BooleanField()
    # maybe a has moons bool and number of int, and/or names of char
    # hasMoons = models.BooleanField() # can check for moons in code/views
    # numOfMoons = models.IntegerField(default=0)
    # namesOfMoons = models.CharField(max_length=255, blank=True) #most likely to go with
    mass = models.FloatField(default=1.0)
    volume = models.FloatField(default=1.0)
    density = models.FloatField(default=1.0)
    # aroundPlanet = models.TextField() #not really sure textfield?  Treat same as moons
    discoveredBy = models.CharField(max_length=255)
    discoveryDate = models.CharField(max_length=255)
    axialTilt = models.FloatField(default=1.0)
    avgTemp = models.FloatField(default=1.0)


    def __str__(self):
        return self.name




