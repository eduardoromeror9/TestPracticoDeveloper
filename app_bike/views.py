from django.shortcuts import render

# Create your views here.
from .utils import obtener_datos
from .models import Estacion


def bikes_view(request):
    datos = obtener_datos()  
    stations = datos['network']['stations'] # trae todas las estaciones de la red
    
    estaciones = Estacion.objects.order_by('name').distinct('name') # esto es para que no se repitan los nombres de las estaciones
    context = {'estaciones': estaciones}
    
    for station in stations:
        estacion = Estacion(
            name=station['name'],
            free_bikes=station['free_bikes'],
            empty_slots=station['empty_slots']
        )
        estacion.save()
    
    
    return render(request, 'bikes.html', context)
