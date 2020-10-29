from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices

'''Modello per gli oggetti Progetto'''
class Progetto(models.Model):
    class Meta:
        ordering = ['titolo']
        verbose_name = "Progetto"
        verbose_name_plural = "Progetti"

    titolo = models.CharField(
            max_length=50,
            help_text="Titolo del progetto",
            verbose_name="Titolo Progetto",
        )
    obiettivi = models.TextField(
            max_length=200, # max_length non ha valore a livello del db
            help_text="Obiettivi del progetto",
        )

    STATUS = Choices(
       (1, 'presentato',    _('Presentato')),
       (2, 'approvato_fs',  _('Approvato dalla Funzione strumentale')),
       (3, 'approvato_ds',  _('Approvato da DS / DSGA')),
       (4, 'approvato',     _('Tutte le classi del triennio')),
    )
    stato_progetto = models.PositiveSmallIntegerField(
            choices=STATUS,
            default=STATUS.presentato,
            verbose_name="Stato del progetto",
            help_text="Situazione dell'approvazione del progetto",
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
    doc_referente = models.ForeignKey(
            'User', # modello della chiave esterna
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

    TIPO_DESTINATARI = Choices(
       (1, 'all_classi',       _('Tutte le classi')),
       (2, 'all_docenti',      _('Tutti i docenti')),
       (3, 'all_biennio',      _('Tutte le classi del biennio')),
       (4, 'all_triennio',     _('Tutte le classi del triennio')),
       (5, 'all_informatica',  _('Tutte le classi del triennio informatica')),
       (6, 'all_elettronica',  _('Tutte le classi del triennio elettronica')),
       (7, 'all_logistica',    _('Tutte le classi del triennio logistica')),
       (8, 'all_prime',        _('Tutte le classi prime')),
       (9, 'all_seconde',      _('Tutte le classi seconde')),
       (10, 'all_terze',       _('Tutte le classi terze')),
       (11, 'all_quarte',      _('Tutte le classi quarte')),
       (12, 'all_quinte',      _('Tutte le classi quinte')),
       (13, 'esterni',         _('Esterni (genitori, docenti altre scuole, studenti altre scuole)')),
    )
    descr_destinatari = models.PositiveSmallIntegerField(
            choices=TIPO_DESTINATARI,
            default=TIPO_DESTINATARI.all_classi,
            verbose_name="Destinatari del progetto",
            help_text="Tipologia di destinatari del progetto",
        )

    materiali = models.ManyToManyField('Materiale')
    progettisti = models.ManyToManyField('User',
                                         through='Progettazione',
                                         related_name='prog_progettati')
    realizzatori = models.ManyToManyField('User',
                                          through='Realizzazione',
                                          related_name='prog_realizzati')

    def __str__(self):
        return "P_" + str(self.id) + ":" + self.titolo

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('progetti-detail', args=[str(self.id)])

    def get_ore_progettazione(self):
        return sum([p.numeroOre for p in Progettazione.objects.filter(progetto=self)])

    def get_ore_realizzazione(self):
        return sum([p.numeroOre for p in Realizzazione.objects.filter(progetto=self)])

    def get_totale_ore_previste(self):
        """Restituisce il monte ore totale previsto per il progetto."""
        return (self.get_ore_progettazione() + self.get_ore_realizzazione())

    def get_percentuale_prog(self):
        """Restituisce la percentuale di ore di progettazione
        rispetto al monte ore totale previsto."""
        ore_totali = self.get_totale_ore_previste()
        return (self.get_ore_progettazione() / ore_totali) if ore_totali else 0

class Progettazione(models.Model):
    TIPO_ORE = Choices(
       (1, 'retribuita', _('Ore retribuite')),
       (2, 'in_obbligo', _('Ore in obbligo')),
    )

    unique_together = ['progetto', 'docente']

    progetto = models.ForeignKey('Progetto',
                                 on_delete=models.RESTRICT,
                                 related_name='info_progettazione_prj')
    docente = models.ForeignKey('User',
                                on_delete=models.RESTRICT,
                                related_name='info_progettazione_doc')
    tipoOre = models.PositiveSmallIntegerField(
       choices=TIPO_ORE,
       default=TIPO_ORE.retribuita,
    )

    numeroOre = models.PositiveSmallIntegerField(default=1)

class Realizzazione(models.Model):
    TIPO_ORE = Choices(
       (1, 'ins_retribuita', _('Docenza retribuita')),
       (2, 'ins_obbligo', _('Docenza in obbligo')),
       (3, 'ass_retribuita', _('Assistenza/Tutoraggio retribuita')),
       (4, 'ass_obbligo', _('Assistenza/Tutoraggio in obbligo'))
    )

    unique_together = ['progetto', 'docente']

    progetto = models.ForeignKey('Progetto',
                                 on_delete=models.RESTRICT,
                                 related_name='info_realizzazione_prj')
    docente = models.ForeignKey('User',
                                on_delete=models.RESTRICT,
                                related_name='info_realizzazione_doc')
    tipoOre = models.PositiveSmallIntegerField(
       choices=TIPO_ORE,
       default=TIPO_ORE.ins_retribuita,
    )

    numeroOre = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return "R(" + str(self.docente) + "," + str(self.progetto) + "," + str(self.numeroOre) + ")"
