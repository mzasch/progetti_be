from django.db import models

'''Modello per gli oggetti Progetto'''
class Progetto(models.Model):
    titolo = models.CharField(
            max_length=50, 
            help_text="Titolo del progetto",
            verbose_name="Titolo Progetto",
        )
    obiettivi = models.TextField(
            max_length=200, # max_length non ha valore a livello del db
            help_text="Obiettivi del progetto",
        )
    n_docenti_dest = models.PositiveSmallIntegerField(
            help_text="Numero di docenti destinatari",
            verbose_name="Docenti destinatari",
        )
    n_studenti_dest = models.PositiveSmallIntegerField(
            help_text="Numero di studenti destinatari",
            verbose_name="Studenti destinatari",
        )
    n_esterni = models.PositiveSmallIntegerField(
            help_text="Numero di esterni coinvolti",
            verbose_name="Esterni coinvolti",
        )
    n_ore_previste = models.PositiveSmallIntegerField(
            help_text="Numero totale di ore previste", 
            verbose_name="Ore previste",
        )
    doc_referente = models.ForeignKey(
            'Docente', # modello della chiave esterna
            on_delete=models.RESTRICT,
            help_text="Docente responsabile del progetto", 
            verbose_name="Docente referente",
        )
    fs_referente = models.ForeignKey(
            'FunzioneStrumentale', # modello della chiave esterna
            on_delete=models.RESTRICT,
            help_text="Funzione stumentale referente del progetto", 
            verbose_name="FS referente",
            # limit_choices_to={'is_funz_strum': True},
        )

    class Meta:
        ordering = ['titolo']
        verbose_name = "Progetto"
        verbose_name_plural = "Progetti"


