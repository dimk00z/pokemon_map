# Generated by Django 2.2.3 on 2020-04-18 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0013_pokemonelementtype_strong_against'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonelementtype',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='elem_images', verbose_name='Изображение элемента'),
        ),
    ]
