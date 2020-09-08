from django.contrib import admin
from progetti.models import Progetto

@admin.register(Progetto)
class ProgettoAdmin(admin.ModelAdmin):
    pass
