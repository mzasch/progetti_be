from django.db import models

'''Modello per gli oggetti Materiale'''
class Materiale(models.Model):
    nome = models.CharField(max_length=30)
    descrizione = models.TextField(max_length=100) # max_length non ha valore a livello del db

    class Meta:
        ordering = ['nome']
        verbose_name = "Materiale"
        verbose_name_plural = "Materiali"


