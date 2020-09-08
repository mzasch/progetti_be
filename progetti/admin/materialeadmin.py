from django.contrib import admin
from progetti.models import Materiale

@admin.register(Materiale)
class MaterialeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descrizione')

