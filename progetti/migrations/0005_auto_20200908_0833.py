# Generated by Django 3.1.1 on 2020-09-08 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progetti', '0004_auto_20200908_0829'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='docente',
            options={'ordering': ['cognome', 'nome'], 'verbose_name': 'Docente', 'verbose_name_plural': 'Docenti'},
        ),
        migrations.AlterModelOptions(
            name='esterno',
            options={'ordering': ['nome'], 'verbose_name': 'Esterno', 'verbose_name_plural': 'Esterni'},
        ),
        migrations.AlterModelOptions(
            name='funzionestrumentale',
            options={'ordering': ['nome'], 'verbose_name': 'Funzione Strumentale', 'verbose_name_plural': 'Funzioni Strumentali'},
        ),
        migrations.AlterModelOptions(
            name='materiale',
            options={'ordering': ['nome'], 'verbose_name': 'Materiale', 'verbose_name_plural': 'Materiali'},
        ),
        migrations.AlterModelOptions(
            name='usomateriale',
            options={'ordering': ['progetto', 'materiale'], 'verbose_name': 'Utilizzo', 'verbose_name_plural': 'Utilizzi'},
        ),
    ]