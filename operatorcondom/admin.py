from django.contrib import admin
from operatorcondom.models import OperatorCondom


class OperatorCondomData(admin.ModelAdmin):
    list_display=('id','rg','cpf','telefone','name','birthday','create','updated','permissions','administratorSystem')
    list_display_links=('id','name')
    search_fields = ('name',)

admin.site.register(OperatorCondom,OperatorCondomData)
