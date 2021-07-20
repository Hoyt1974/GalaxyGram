from django.core import paginator
from django.shortcuts import render
from planetmodel.models import Body
from planetpost.models import Planet_Post
from django.views import View
from django.core.paginator import Paginator, EmptyPage
import requests



class PlanetView(View):


    def get(self, request):
        planets = Body.objects.all()
        
        paginator = Paginator(planets, 30)
        
        page_num = request.GET.get('page', 1)
        print(page_num)
        
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(1)


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
            

        return render(request, 'planet.html', {'planets': page, 'page_number': int(page_num), 'paginator': paginator})



class PlanetDetailView(View):


    def get(self, request, planet_id):
        planet = Body.objects.get(id=planet_id)
        post = Planet_Post.objects.filter(body=planet)
        print(planet.id)
        return render(request, 'planet_detail.html', {'planet': planet, 'posts': post})




    