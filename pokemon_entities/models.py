from django.db import models


class PokemonElementType(models.Model):
    """Элемент"""
    title = models.TextField(max_length=100,
                             verbose_name='стихия')
    img = models.ImageField(
        upload_to='elem_images',
        verbose_name='Изображение элемента', null=True, blank=True)

    strong_against = models.ManyToManyField(
        "self", related_name='+',
        blank=True)

    def __str__(self):
        return self.title


class Pokemon(models.Model):
    """Покемон"""
    title_ru = models.TextField(default='завр',
                                max_length=100,
                                null=False,
                                verbose_name='Название покемона на русском')
    title_en = models.CharField(
        max_length=100,
        verbose_name='Название покемона на английском', blank=True)
    title_jp = models.CharField(
        max_length=100,
        verbose_name='Название  на японском', blank=True)
    image = models.ImageField(
        upload_to='poke_images',
        verbose_name='Изображение покемона', null=True, blank=True)
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание')
    previous_evolution = models.ForeignKey(
        "self",
        verbose_name='Из кого эволюционирует',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='next_evolutions')
    element_type = models.ManyToManyField(
        PokemonElementType,
        blank=True,
        verbose_name='Элемент')

    def __str__(self):
        return f"{self.title_ru}"


class PokemonEntity(models.Model):
    """Появление покемона"""
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(
        verbose_name='Появится',
        null=True,
        blank=True)
    disappeared_at = models.DateTimeField(
        verbose_name='Исчезнет',
        null=True,
        blank=True,
    )
    level = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Уровень покемона')
    health = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Здоровье покемона')
    strength = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Сила покемона')
    defence = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Защита покемона')
    stamina = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Выносливость покемона')
    pokemon = models.ForeignKey(Pokemon,
                                on_delete=models.CASCADE,
                                help_text='Note')

    def __str__(self):
        return f"{self.pokemon.title} lat:{self.lat} lot: {self.lot}"
