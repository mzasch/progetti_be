# Generated by Django 3.1.1 on 2020-10-27 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progetti', '0004_progetto_descr_destinatari'),
    ]

    operations = [
        migrations.AddField(
            model_name='realizzazione',
            name='numeroOre',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='progetto',
            name='descr_destinatari',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Tutte le classi'), (2, 'Tutti i docenti'), (3, 'Tutte le classi del biennio'), (4, 'Tutte le classi del triennio'), (5, 'Tutte le classi del triennio informatica'), (6, 'Tutte le classi del triennio elettronica'), (7, 'Tutte le classi del triennio logistica'), (8, 'Tutte le classi prime'), (9, 'Tutte le classi seconde'), (10, 'Tutte le classi terze'), (11, 'Tutte le classi quarte'), (12, 'Tutte le classi quinte'), (13, 'Esterni (genitori, docenti altre scuole, studenti altre scuole)')], default=1, help_text='Tipologia di destinatari del progetto', verbose_name='Destinatari del progetto'),
        ),
    ]
