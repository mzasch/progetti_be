from django.db import models

'''Modello per gli oggetti UsoMateriale'''
class UsoMateriale(models.Model):
    class Meta:
        ordering = ['progetto', 'materiale']
        verbose_name = "Utilizzo"
        verbose_name_plural = "Utilizzi"

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

    def __str__(self):
        return "UM_" + str(self.id)

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])


