from django.db import models

'''Modello per gli oggetti Esterno'''
class Esterno(models.Model):    
    class Meta:
        ordering = ['nome']
        verbose_name = "Esterno"
        verbose_name_plural = "Esterni"

    nome = models.CharField(max_length=30)
    descrizione = models.TextField(max_length=100) # max_length non ha valore a livello del db

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])


