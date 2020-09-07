from django.db import models

'''Modello per gli oggetti Docente'''
class Docente(models.Model):
    nome = models.CharField(max_length=50) 
    cognome = models.CharField(max_length=50) 

