from django.db import models

# Create your models here.
class Estacion(models.Model):
    name = models.CharField(max_length=200)
    free_bikes = models.IntegerField()
    empty_slots = models.IntegerField()
    

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = "Estaciones"

    search_fields = ['name', 'free_bikes']