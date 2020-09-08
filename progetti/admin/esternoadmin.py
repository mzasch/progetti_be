from django.contrib import admin
from progetti.models import Esterno

@admin.register(Esterno)
class EsternoAdmin(admin.ModelAdmin):
    pass
