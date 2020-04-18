# Generated by Django 2.2.3 on 2020-04-17 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0009_auto_20200417_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonElementType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200, verbose_name='стихия')),
            ],
        ),
        migrations.AddField(
            model_name='pokemon',
            name='element_type',
            field=models.ManyToManyField(blank=True, to='pokemon_entities.PokemonElementType'),
        ),
    ]