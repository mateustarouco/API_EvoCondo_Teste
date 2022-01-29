from django.contrib import admin
from resident.models import Resident

class ResidentData(admin.ModelAdmin):
    list_display=('id','rg','cpf','telefone','name','block','apartament','expiration','create','updated','last_access','familyID')
    list_display_links=('id','name')
    search_fields = ('name',)

admin.site.register(Resident,ResidentData)