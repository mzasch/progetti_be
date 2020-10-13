from rest_framework import serializers
from progetti.models import Docente, Esterno, FunzioneStrumentale, Materiale, Progetto, UsoMateriale

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = ['id', 'nome', 'cognome']

class EsternoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Esterno
        fields = ['id', 'nome', 'descrizione']

class FunzioneStrumentaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunzioneStrumentale
        fields = ['id', 'nome', 'descrizione', 'docente']

class MaterialeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materiale
        fields = ['id', 'nome', 'descrizione']

class ProgettoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progetto
        fields = ['id', 'titolo', 'obiettivi',
                  'n_docenti_dest', 'n_studenti_dest',
                  'n_esterni', 'n_ore_previste', 'doc_referente',
                  'fs_referente',
                 ]
