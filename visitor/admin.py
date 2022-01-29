from django.contrib import admin
from visitor.models import Visitor

class VisitorData(admin.ModelAdmin):
    list_display=('id','rg','cpf','telefone','name','block','apartament','expiration','create','updated','last_access')
    list_display_links=('id','name')
    search_fields = ('name',)

admin.site.register(Visitor,VisitorData)

# Register your models here.
