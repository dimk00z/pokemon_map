# Generated by Django 2.2.3 on 2020-04-17 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_auto_20200417_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='lot',
            new_name='lon',
        ),
    ]
