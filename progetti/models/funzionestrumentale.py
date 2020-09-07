from django.db import models

'''Modello per gli oggetti FunzioneStrumentale'''
class FunzioneStrumentale(models.Model):
    nome=models.CharField(
            max_length=30,
            help_text="Nome della funzione strumentale",
            verbose_name="Funzione Strumentale",
        )
    descrizione=models.TextField(
            max_length=200, # max_length non ha valore a livello del db
            help_text="Descrizione della funzione strumentale",
            verbose_name="Descrizione FS",
        )
    docente_fs=models.ForeignKey(
            'Docente', # modello della chiave esterna
            on_delete=models.RESTRICT,
            help_text="Docente incaricato per questa FS",
            verbose_name="Docente",
        )
