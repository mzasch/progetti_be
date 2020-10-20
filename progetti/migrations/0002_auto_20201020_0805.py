# Generated by Django 3.1.1 on 2020-10-20 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('progetti', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funzionestrumentale',
            name='docente_fs',
            field=models.OneToOneField(help_text='Docente incaricato per questa FS', on_delete=django.db.models.deletion.RESTRICT, to='progetti.docente', verbose_name='Docente'),
        ),
    ]