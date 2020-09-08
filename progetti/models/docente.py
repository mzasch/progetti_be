from django.db import models

'''Modello per gli oggetti Docente'''
class Docente(models.Model):
    class Meta:
        ordering = ['cognome', 'nome']
        verbose_name = "Docente"
        verbose_name_plural = "Docenti"

    nome = models.CharField(max_length=50) 
    cognome = models.CharField(max_length=50) 

    def __str__(self):
        return self.cognome + ", " + self.nome[0] + "."

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])


