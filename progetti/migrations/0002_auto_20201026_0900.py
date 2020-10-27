# Generated by Django 3.1.1 on 2020-10-26 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('progetti', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Realizzazione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoOre', models.PositiveSmallIntegerField(choices=[(1, 'Ore non di insegnamento'), (2, 'Tipo 2'), (3, 'Tipo 3'), (4, 'Ore di insegnamento')], default=1)),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='realizzazione_doc', to=settings.AUTH_USER_MODEL)),
                ('progetto', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='realizzazione_prj', to='progetti.progetto')),
            ],
        ),
        migrations.CreateModel(
            name='Progettazione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoOre', models.PositiveSmallIntegerField(choices=[(1, 'Ore non di insegnamento'), (2, 'Tipo 2'), (3, 'Tipo 3')], default=1)),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='progettazione_doc', to=settings.AUTH_USER_MODEL)),
                ('progetto', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='progettazione_prj', to='progetti.progetto')),
            ],
        ),
        migrations.AddField(
            model_name='progetto',
            name='progettisti',
            field=models.ManyToManyField(related_name='list_progettisti', through='progetti.Progettazione', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='progetto',
            name='realizzatori',
            field=models.ManyToManyField(related_name='list_realizzatori', through='progetti.Realizzazione', to=settings.AUTH_USER_MODEL),
        ),
    ]
