from django.contrib import admin
from progetti.models import Docente

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('cognome', 'nome')


