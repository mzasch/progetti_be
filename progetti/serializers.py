from rest_framework import serializers
from progetti.models import *

class UserSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    prog_progettati = serializers.HyperlinkedRelatedField(
                                    many=True,
                                    read_only= True,
                                    view_name='progetti-detail'
                                )
    prog_realizzati = serializers.HyperlinkedRelatedField(
                                    many=True,
                                    read_only= True,
                                    view_name='progetti-detail'
                                )
    class Meta:
        model = User
        fields = ['id', 'username', 'last_name', 'first_name', 'url',
                  'prog_progettati', 'prog_realizzati',
        ]

class EsternoSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    class Meta:
        model = Esterno
        fields = ['nome', 'descrizione', 'url']
        read_only_fields = ['id']

class FunzioneStrumentaleSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    docente_fs = serializers.HyperlinkedRelatedField(read_only=True, view_name='docenti-detail')

    progetti_assegnati = serializers.HyperlinkedRelatedField(
                                many=True,
                                read_only= True,
                                view_name='progetti-detail'
                            )

    class Meta:
        model = FunzioneStrumentale
        fields = ['nome', 'descrizione', 'docente_fs', 'url', 'progetti_assegnati']
        read_only_fields = ['id', 'docente_fs']

class MaterialeSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    class Meta:
        model = Materiale
        fields = ['nome', 'descrizione', 'url']
        read_only_fields = ['id']

class ProgettoSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    progettisti = serializers.HyperlinkedRelatedField(
                                    many=True,
                                    read_only= True,
                                    view_name='docenti-detail'
                                )

    realizzatori = serializers.HyperlinkedRelatedField(
                                    many=True,
                                    read_only= True,
                                    view_name='docenti-detail'
                                )

    perc_ore = serializers.FloatField(source='get_percentuale_prog', read_only=True)
    n_ore_previste = serializers.IntegerField(source='get_totale_ore_previste', read_only=True)
    n_ore_progettazione = serializers.IntegerField(source='get_ore_progettazione', read_only=True)
    n_ore_realizzazione = serializers.IntegerField(source='get_ore_realizzazione', read_only=True)

    class Meta:
        model = Progetto
        fields = ['titolo', 'obiettivi', 'stato_progetto', 'url', 'descr_destinatari',
                  'n_docenti_dest', 'n_studenti_dest', 'n_esterni',
                  'n_ore_previste', 'n_ore_progettazione', 'n_ore_realizzazione', 'perc_ore',
                  'doc_referente', 'fs_referente', 'progettisti', 'realizzatori'
                 ]
        read_only_fields = ['id', 'stato_progetto']
