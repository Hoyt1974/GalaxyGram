from django.db import models

class Body(models.Model):
    name = models.CharField(max_length=255)
    englishName = models.CharField(max_length=255)
    isPlanet = models.BooleanField()
    mass = models.FloatField(default=1.0)
    volume = models.FloatField(default=1.0)
    density = models.FloatField(default=1.0)
    discoveredBy = models.CharField(max_length=255)
    discoveryDate = models.CharField(max_length=255)
    axialTilt = models.FloatField(default=1.0)
    avgTemp = models.FloatField(default=1.0)

    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name




