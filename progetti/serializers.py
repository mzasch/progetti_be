from rest_framework import serializers
from progetti.models import *

class UserSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    #progetti = serializers.CharField(source=)
    class Meta:
        model = User
        fields = ['id', 'username', 'last_name', 'first_name', 'url']

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
    perc_ore = serializers.FloatField(source='get_percentuale_prog', read_only=True)
    
    class Meta:
        model = Progetto
        fields = ['titolo', 'obiettivi', 'descr_destinatari',
                  'n_docenti_dest', 'n_studenti_dest',
                  'n_esterni', 'n_ore_previste', 'perc_ore', 'doc_referente',
                  'fs_referente', 'url', 'progettisti', 'realizzatori'
                 ]
        read_only_fields = ['id']
