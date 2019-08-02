import pdb

from django.contrib.auth.models import User
from django.db import models


class Movie(models.Model):
    title = models.CharField('título', max_length=254)

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'

    def __str__(self):
        return self.title


class Session(models.Model):
    language_choices = (
        ("Legendado em português", "Legendado em português"),
        ("Dublado em português", "Dublado em português")
    )
    movie_choices = (
        ("3D", "3D"),
        ("2D", "2D")
    )
    type_language = models.CharField(max_length=100, choices=language_choices, default="Legendado em português")
    type_movie = models.CharField(max_length=10, choices=movie_choices, default="2D")
    movie = models.ForeignKey(Movie, models.CASCADE, 'session', blank=True, null=True)

    class Meta:
        verbose_name = 'Sessão'
        verbose_name_plural = 'Sessões'

    def __str__(self):
        return f'{self.movie.title} / {self.type_language} / {self.type_movie}'


class Showtime(models.Model):
    start_at = models.DateTimeField(blank=True, null=True)
    session = models.ForeignKey(Session, models.CASCADE, 'showtime', blank=True, null=True)

    class Meta:
        verbose_name = 'Horário'
        verbose_name_plural = 'Horários'

    def __str__(self):
        return self.start_at.strftime("%d-%m-%y %H:%M")

    @property
    def time(self):
        return self.start_at.time()

    @property
    def date(self):
        return self.start_at.date().strftime('%d-%m-%y')


class Seat(models.Model):
    description = models.CharField('descrição', max_length=254)

    class Meta:
        verbose_name = 'Poltrona'
        verbose_name_plural = 'Poltronas'

    def __str__(self):
        return self.description

    @property
    def is_available(self):
        return False if self.item.all() else True


class ItemSeat(models.Model):
    seat = models.ForeignKey(Seat, models.CASCADE, 'item', blank=True, null=True)
    showtime = models.ForeignKey(Showtime, models.CASCADE, 'item', blank=True, null=True)
    user = models.ForeignKey(User, models.CASCADE, 'item', blank=True, null=True)

    class Meta:
        verbose_name = 'Poltrona no horário'
        verbose_name_plural = 'Poltronas no horário'

    def __str__(self):
        return f'{self.seat.description} | {self.showtime.start_at.strftime("%d-%m-%y")}'
