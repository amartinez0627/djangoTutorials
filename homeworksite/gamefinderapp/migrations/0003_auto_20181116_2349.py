# Generated by Django 2.1.3 on 2018-11-17 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamefinderapp', '0002_auto_20181116_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='age_restriction',
            field=models.CharField(choices=[('Ao', 'AdultsOnly'), ('M', 'Mature'), ('T', 'Teen'), ('E', 'Everyone'), ('eC', 'EarlyChildhood')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='console',
            field=models.CharField(choices=[('PC', 'Personal Computer'), ('PS4', 'Play Station 4'), ('XB1', 'XBox One')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.CharField(choices=[('act', 'Action'), ('adv', 'Adventure'), ('sp', 'Sports'), ('sho', 'Shooting'), ('mus', 'Musical'), ('fig', 'Fighting'), ('rac', 'Racing')], default='', max_length=100),
        ),
    ]