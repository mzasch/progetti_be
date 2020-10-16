from rest_framework import serializers
from progetti.models import Docente, Esterno, FunzioneStrumentale, Materiale, Progetto, UsoMateriale

class DocenteSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    class Meta:
        model = Docente
        fields = ['nome', 'cognome', 'url']
        read_only_fields = ['id']

class EsternoSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    class Meta:
        model = Esterno
        fields = ['nome', 'descrizione', 'url']
        read_only_fields = ['id']

class FunzioneStrumentaleSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    docente_fs = serializers.HyperlinkedRelatedField(read_only=True, view_name='docenti-detail')
    class Meta:
        model = FunzioneStrumentale
        fields = ['nome', 'descrizione', 'docente_fs', 'url']
        read_only_fields = ['id', 'docente_fs']

class MaterialeSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    class Meta:
        model = Materiale
        fields = ['nome', 'descrizione', 'url']
        read_only_fields = ['id']

class ProgettoSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    class Meta:
        model = Progetto
        fields = ['titolo', 'obiettivi',
                  'n_docenti_dest', 'n_studenti_dest',
                  'n_esterni', 'n_ore_previste', 'doc_referente',
                  'fs_referente', 'url'
                 ]
        read_only_fields = ['id']
