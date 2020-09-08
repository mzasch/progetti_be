from django.contrib import admin
from progetti.models import FunzioneStrumentale

@admin.register(FunzioneStrumentale)
class FunzioneStrumentaleAdmin(admin.ModelAdmin):
    list_display = ('nome', 'docente_fs')
