from django.contrib import admin
from .models import Progetto, Docente, FunzioneStrumentale, Esterno, Materiale, UsoMateriale

# Register your models here.
admin.site.register(Progetto)
admin.site.register(Docente)
admin.site.register(FunzioneStrumentale)
admin.site.register(Esterno)
admin.site.register(Materiale)
admin.site.register(UsoMateriale)
