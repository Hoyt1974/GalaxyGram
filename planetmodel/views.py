from django.shortcuts import render
from planetmodel.models import Body
from django.shortcuts import get_object_or_404


def planet_view(request):
    planet = Body.objects.all()
    return render(request, 'planet.html', {'planet': planet})






    