# Generated by Django 3.1.1 on 2020-09-08 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progetti', '0003_auto_20200907_1253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='progetto',
            options={'ordering': ['titolo'], 'verbose_name': 'Progetto', 'verbose_name_plural': 'Progetti'},
        ),
    ]
