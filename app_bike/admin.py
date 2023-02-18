from django.contrib import admin

# Register your models here.
from .models import Estacion

class EstacionAdmin(admin.ModelAdmin):
    list_display = ('name', 'free_bikes', 'empty_slots')
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(Estacion, EstacionAdmin)
