import folium
import json
from pathlib import Path
from django.shortcuts import render
from pokemon_entities.models import Pokemon, PokemonEntity, PokemonElementType
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):

    pokemons = Pokemon.objects.all()
    pokemons_entities = PokemonEntity.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemons_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            pokemon_entity.pokemon.title_ru,
            request.build_absolute_uri(pokemon_entity.pokemon.image.url))

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url if pokemon.image else '',
            'title_ru': pokemon.title_ru,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def get_pokemon_info_for_render(pokemon, request):

    pokemon_for_render = {'img_url': pokemon.image.url,
                          'title_ru': pokemon.title_ru,
                          'title_jp': pokemon.title_jp,
                          'title_en': pokemon.title_ru,
                          'description': pokemon.description}

    pokemon_previous_evolution = pokemon.previous_evolution
    if pokemon_previous_evolution:
        pokemon_for_render['previous_evolution'] = {
            'pokemon_id': pokemon_previous_evolution.id,
            'img_url': request.build_absolute_uri(pokemon_previous_evolution.image.url),
            'title_ru': pokemon_previous_evolution.title_ru
        }

    pokemon_next_evolution = pokemon.next_evolutions.first()
    if pokemon_next_evolution:
        pokemon_for_render['next_evolution'] = {
            'pokemon_id': pokemon_next_evolution.id,
            'img_url': request.build_absolute_uri(
                pokemon_next_evolution.image.url),
            'title_ru': pokemon_next_evolution.title_ru}

    current_pokemon_elements = pokemon.element_type.all()
    if len(current_pokemon_elements) > 0:
        pokemon_for_render['element_type'] = []
        for element_type in current_pokemon_elements:
            strong_against = [
                element.title for element in element_type.strong_against.all()]
            pokemon_for_render['element_type'].append({
                'title': element_type.title,
                'strong_against': strong_against,
                'img': element_type.img.url if element_type.img else '',
            })

    return pokemon_for_render


def show_pokemon(request, pokemon_id):
    try:
        pokemon = Pokemon.objects.get(id=pokemon_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    current_pokemon_entities = pokemon.pokemon_entities.all()
    for current_pokemon_entity in current_pokemon_entities:
        add_pokemon(
            folium_map,
            current_pokemon_entity.lat,
            current_pokemon_entity.lon,
            current_pokemon_entity.pokemon.title_ru,
            request.build_absolute_uri(
                current_pokemon_entity.pokemon.image.url))
    return render(request, "pokemon.html",
                  context={'map': folium_map._repr_html_(),
                           'pokemon': get_pokemon_info_for_render(pokemon, request)})
