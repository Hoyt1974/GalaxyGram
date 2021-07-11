from django.db import models

class Body(models.Model):
    name = models.CharField(max_length=255)
    englishName = models.CharField(max_length=255)
    isPlanet = models.BooleanField()
    # maybe a has moons bool and number of int, and/or names of char
    hasMoons = models.BooleanField() # can check for moons in code/views
    numOfMoons = models.IntegerField()
    namesOfMoons = models.CharField(max_length=255) #most likely to go with
    mass = models.DecimalField(max_digits=5, decimal_places=5)
    volume = models.DecimalField(max_digits=5, decimal_places=5)
    density =models.DecimalField(max_digits=5, decimal_places=5)
    aroundPlanet = models.TextField() #not really sure textfield?  Treat same as moons
    discoveredBy = models.CharField(max_length=255)
    discoveryDate = models.DateField()
    axialTilt =models.DecimalField(max_digits=5, decimal_places=5)
    avgTemp =models.DecimalField(max_digits=5, decimal_places=5)





