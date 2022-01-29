from django.contrib import admin
from garage.models import Garage

class GarageData(admin.ModelAdmin):
    list_display=('id','rg','name','number','vieicle','model','license')
    list_display_links=('id','name')
    search_fields = ('name',)

admin.site.register(Garage,GarageData)
# Register your models here.
