# Generated by Django 2.2.3 on 2020-04-18 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0014_pokemonelementtype_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonelementtype',
            name='title',
            field=models.TextField(max_length=100, verbose_name='стихия'),
        ),
    ]
