from django.shortcuts import render
from planetmodel.models import Body
import requests



def planet_view(request):
    planets = Body.objects.all()
    if not planets:
        r = requests.get('https://api.le-systeme-solaire.net/rest/bodies/', params=request.GET)
        data = r.json()
        for i in data['bodies']:
            try:
                Body.objects.create(
                    name = i['name'],
                    englishName = i['englishName'],
                    isPlanet = i['isPlanet'],
                    # hasMoons = i['hasMoons'],
                    # numOfMoons = i['numOfMoons'],
                    # namesOfMoons = i['namesOfMoons'],
                    mass = i['mass']['massValue'],
                    volume = i['vol']['volValue'],
                    density = i['density'],
                    # aroundPlanet = i['aroundPlanet'],
                    discoveredBy = i['discoveredBy'],
                    discoveryDate = i['discoveryDate'],
                    axialTilt = i['axialTilt'],
                    avgTemp = i['avgTemp'],
            )
            except TypeError:
                    Body.objects.create(
                    name = i['name'],
                    englishName = i['englishName'],
                    isPlanet = i['isPlanet'],
                    # hasMoons = i['hasMoons'],
                    # numOfMoons = i['numOfMoons'],
                    # namesOfMoons = i['namesOfMoons'],
                    density = i['density'],
                    # aroundPlanet = i['aroundPlanet'],
                    discoveredBy = i['discoveredBy'],
                    discoveryDate = i['discoveryDate'],
                    axialTilt = i['axialTilt'],
                    avgTemp = i['avgTemp'],
            )
        planets = Body.objects.all()
        

    return render(request, 'planet.html', {'planets': planets})


# {
# "id":"phobos",
# "name":"Phobos",
# "englishName":"Phobos",
# "isPlanet":false,
# "moons":null,
# "semimajorAxis":9376,
# "perihelion":9234,
# "aphelion":9518,
# "eccentricity":0.01510,
# "inclination":1.07500,
# "mass":{"massValue":1.06000,"massExponent":16},
# "vol":{"# {
# "id":"phobos",
# "name":"Phobos",
# "englishName":"Phobos",
# "isPlanet":false,
# "moons":null,
# "semimajorAxis":9376,
# "perihelion":9234,
# "aphelion":9518,
# "eccentricity":0.01510,
# "inclination":1.07500,
# "mass":{"massValue":1.06000,"massExponent":16},
# "vol":{"volValue":5.78361,"volExponent":3},
# "density":1.90000,
# "gravity":0.00570,
# "escape":11.39000,
# "meanRadius":33.00000,
# "equaRadius":13.00000,
# "polarRadius":9.10000,
# "flattening":0.00000,
# "dimension":"26.8 × 22.4 × 18.4",
# "sideralOrbit":0.31891,
# "sideralRotation":0.76530,
# "aroundPlanet":{"planet":"mars","rel":"https://api.le-systeme-solaire.net/rest/bodies/mars"},"discoveredBy":"Asaph Hall",
# "discoveryDate":"12/08/1877",
# "alternativeName":"",
# "axialTilt":0,
# "avgTemp":0,
# "mainAnomaly":0.00000,
# "argPeriapsis":0.00000,
# "longAscNode":0.00000,
# "rel":"https://api.le-systeme-solaire.net/rest/bodies/phobos"},":5.78361,"volExponent":3},
# "density":1.90000,
# "gravity":0.00570,
# "escape":11.39000,
# "meanRadius":33.00000,
# "equaRadius":13.00000,
# "polarRadius":9.10000,
# "flattening":0.00000,
# "dimension":"26.8 × 22.4 × 18.4",
# "sideralOrbit":0.31891,
# "sideralRotation":0.76530,
# "aroundPlanet":{"planet":"mars","rel":"https://api.le-systeme-solaire.net/rest/bodies/mars"},"discoveredBy":"Asaph Hall",
# "discoveryDate":"12/08/1877",
# "alternativeName":"",
# "axialTilt":0,
# "avgTemp":0,
# "mainAnomaly":0.00000,
# "argPeriapsis":0.00000,
# "longAscNode":0.00000,
# "rel":"https://api.le-systeme-solaire.net/rest/bodies/phobos"},



    