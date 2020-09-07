from django.db import models

'''Modello per gli oggetti UsoMateriale'''
class UsoMateriale(models.Model):
    materiale=models.ForeignKey(
            'Materiale', # modello della chiave esterna
            on_delete=models.CASCADE,
            help_text="Il materiale in uso",
            verbose_name="Materiale",
        )
    progetto=models.ForeignKey(
            'Progetto', # modello della chiave esterna
            on_delete=models.CASCADE,
            help_text="Il progetto per il quale si usa questo materiale",
            verbose_name="Progetto",
        )
