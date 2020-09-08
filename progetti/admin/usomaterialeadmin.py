from django.contrib import admin
from progetti.models import UsoMateriale

@admin.register(UsoMateriale)
class UsoMaterialeAdmin(admin.ModelAdmin):
    list_display = ('progetto', 'materiale')
