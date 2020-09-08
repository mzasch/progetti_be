from django.contrib import admin
from progetti.models import Progetto

@admin.register(Progetto)
class ProgettoAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'doc_referente', 'fs_referente')
    fieldsets = (
        ('Dati generali', {
            'fields': (('titolo', 'n_ore_previste'), 'obiettivi')
            }),
        ('Referenti', {
            'fields': (('doc_referente', 'fs_referente'),)
            }),
        ('Soggetti coinvolti', {
            'fields': (('n_docenti_dest', 'n_studenti_dest', 'n_esterni'),)
            }),
    )
