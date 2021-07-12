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
                    mass = i['mass']['massValue'],
                    volume = i['vol']['volValue'],
                    density = i['density'],
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
                    density = i['density'],
                    discoveredBy = i['discoveredBy'],
                    discoveryDate = i['discoveryDate'],
                    axialTilt = i['axialTilt'],
                    avgTemp = i['avgTemp'],
            )
        planets = Body.objects.all()
        

    return render(request, 'planet.html', {'planets': planets})



def planet_detail_view(request, planet_id):
    planet = Body.objects.get(id=planet_id)
    print(planet.id)
    return render(request, 'planet_detail.html', {'planet': planet})




    