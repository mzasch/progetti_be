from django.db import models
from django.urls import reverse

'''Modello per gli oggetti Materiale'''
class Materiale(models.Model):
    class Meta:
        ordering = ['nome']
        verbose_name = "Materiale"
        verbose_name_plural = "Materiali"

    nome = models.CharField(max_length=30)
    descrizione = models.TextField(max_length=100) # max_length non ha valore a livello del db

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('materiali-detail', args=[str(self.id)])
