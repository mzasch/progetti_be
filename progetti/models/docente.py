from django.db import models

'''Modello per gli oggetti Docente'''
class Docente(models.Model):
    nome = models.CharField(max_length=50) 
    cognome = models.CharField(max_length=50) 

    class Meta:
        ordering = ['cognome', 'nome']
        verbose_name = "Docente"
        verbose_name_plural = "Docenti"


